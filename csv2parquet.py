# https://francoismichonneau.net/2022/10/import-big-csv/?fbclid=IwAR335iAvUuUOrY4rHDMJwhx8vvTvCiA0k6LImRxebLGV14m_pkcbq8CBD68#single-file-api-in-python
# from <https://stackoverflow.com/a/68563617/1113276>
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.csv
import csv
import time

start_time = time.time()

# convert_options = pyarrow.csv.ConvertOptions()
# convert_options.column_types = {
# #@    'rate_code': pa.utf8(),
#     'Notes: Profile of Census Subdivisions (2247)': pa.utf8()
# }
def parquet_batch_convert(in_path, out_path, row_group_size=20000):
    writer = None
    total_row = 0
    batch_chunk = []
    with pyarrow.csv.open_csv(in_path) as reader:
        for next_chunk in reader:
            if writer is None:
                schema = next_chunk.schema
                writer = pq.ParquetWriter(out_path, schema)
            if total_row >= row_group_size:
                next_table = pa.Table.from_batches(batch_chunk, schema=schema)
                writer.write_table(next_table, row_group_size=total_row)
                total_row = 0
                batch_chunk = []
            else:
                batch_chunk.append(next_chunk)
                total_row += next_chunk.num_rows

        next_table = pa.Table.from_batches(batch_chunk, schema=schema)
        writer.write_table(next_table, row_group_size=total_row)

    writer.close()

def without_batch(csv_in, pq_out, column_name=False):
    """
    - convert csv without using batch, the size of parquet may be a little larger
    - check the csv header (column) name before using. If the column name is weird, set column_name=False
    """
    writer = None
    with pyarrow.csv.open_csv(csv_in) as reader:
        for next_chunk in reader:
            if not column_name:
                table_dict = {}
                for i, col in enumerate(next_chunk.columns):
                    if isinstance(col, pa.Date32Array):
                        col = col.cast(pa.string())
                    table_dict['C{}'.format(i)] = col
                table = pa.table(table_dict)
            else:
                table = pa.Table.from_batches([next_chunk])
            if writer is None:
                writer = pq.ParquetWriter(pq_out, table.schema)
            writer.write_table(table, row_group_size=20000)
    writer.close()

def convert_zillow(in_path='./data/zillow.csv', out_path='./data/zillow.parquet'):
    without_batch(in_path, out_path)
    end_time = time.time()
    print('execution time is:{}'.format(end_time - start_time))

def convert_flights(in_path='./data/flights.csv', out_path='./data/flights.parquet'):
    without_batch(in_path, out_path)
    end_time = time.time()
    print('execution time is:{}'.format(end_time - start_time))

# convert_flights()
convert_zillow()