# https://francoismichonneau.net/2022/10/import-big-csv/?fbclid=IwAR335iAvUuUOrY4rHDMJwhx8vvTvCiA0k6LImRxebLGV14m_pkcbq8CBD68#single-file-api-in-python
# from <https://stackoverflow.com/a/68563617/1113276>
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.csv
import csv
import time

in_path = '/home/r10942129/Downloads/census_a.csv'
out_path = '/home/r10942129/Downloads/census_a.parquet'
start_time = time.time()

# convert_options = pyarrow.csv.ConvertOptions()
# convert_options.column_types = {
# #@    'rate_code': pa.utf8(),
#     'Notes: Profile of Census Subdivisions (2247)': pa.utf8()
# }
def parquet_batch_convert(in_path, out_path):
    writer = None
    total_row = 0
    batch_chunk = []
    with pyarrow.csv.open_csv(in_path) as reader:
        for next_chunk in reader:
            if next_chunk is None:
                break
            if writer is None:
                schema = next_chunk.schema
                writer = pq.ParquetWriter(out_path, schema)
            if total_row >= 20000:
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

def without_batch(csv_in, pq_out):
    '''
    convert csv header name to C0~Ci without using batch
    the size of parquet may be a little larger
    '''
    writer = None
    with pyarrow.csv.open_csv(csv_in) as reader:
        for next_chunk in reader:
            if next_chunk is None:
                break
            table_dict = {}
            for i, col in enumerate(next_chunk.columns):
                table_dict['C{}'.format(i)] = col
            table = pa.table(table_dict)
            if writer is None:
                writer = pq.ParquetWriter(pq_out, table.schema)
            #next_table = pa.Table.from_batches([next_chunk])
            writer.write_table(table, row_group_size=20000)
    writer.close()

without_batch(in_path, out_path)
end_time = time.time()
print('execution time is:{}'.format(end_time - start_time))