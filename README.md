# Reference

YeSQL: https://github.com/athenarc/YeSQL/tree/main

sqlite-parquet-vtable: https://github.com/cldellow/sqlite-parquet-vtable/tree/master

In this repo, we simply support the YeSQLite. 

# Main Commit
- `csv2parquet.py`
  - Usage: `python3 csv2parquet.py`. Only support for converting the CSV file in `data/zillow.csv`. Require some workarounds to convert another CSV files.
- `YeSQLite/pypylib/apsw.py`
  - Enable load extension here
- `data/census_a.parquet`: We have already converted this [census_a.csv](https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/prof/details/download-telecharger/comp/GetFile.cfm?Lang=E&FILETYPE=CSV&GEONO=044_ATLANTIC) to the Parquet file. Due to the size limit, we didn't upload the large `census.parquet` here.

# Installation
Clone the current repository and run
```
./exec.sh
```
This script contains the list of commands to install packages in YeSQLite and sqlite-parquet-vtable library

run end-to-end experiments with
```
pypy2.7-v7.3.6-linux64/bin/pypy YeSQLite/mterm.py -f udfs -d data.db
```
Paste query at `sql_queries/census_parquet.sql` in the terminal.

The terminal also executes any other queries using the SQLite's SQL dialect.

## Notes

If you encounter the bug like
```
libcrypto.so.1.0.0: cannot open shared object file: No such file or 
directory
```
It's probably because the version of the sqlite-parquet-vtable extension is developed on Ubuntu 16.04

We fix this error through [this advice](https://askubuntu.com/questions/1116133/ubuntu-18-04-libcrypto-so-1-0-0-cannot-open-shared-object-file-no-such-file-o?fbclid=IwAR1Ivjl9Wj3zOvLh4H7cJwy-Q0W64_9YgnbbjJ5wiUx39CA_e1LGWJzWNxo)

(It works for any error like lib*.so.1.0.0)

```commandline
search for libcrypto.so.1.0.0
$ for l in $(sudo locate libcrypto.so.1.0.0); do md5sum $l; done
829091982233166cdaa55b41fb353609  /snap/core/7713/lib/x86_64-linux-gnu/libcrypto.so.1.0.0
829091982233166cdaa55b41fb353609  /snap/core/7917/lib/x86_64-linux-gnu/libcrypto.so.1.0.0
18403538a12facf8aced1dcfcccef1ba  /snap/core18/1192/usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0
18403538a12facf8aced1dcfcccef1ba  /snap/core18/1223/usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0
829091982233166cdaa55b41fb353609  /snap/gnome-3-26-1604/92/lib/x86_64-linux-gnu/libcrypto.so.1.0.0
829091982233166cdaa55b41fb353609  /snap/gnome-3-26-1604/97/lib/x86_64-linux-gnu/libcrypto.so.1.0.0
md5sum: /usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0: No such file or directory

we copy the file in /snap/core/.... to /usr/lib/x86_64-linux-gnu/
$ sudo cp -p /snap/core/14946/lib/x86_64-linux-gnu/libcrypto.so.1.0.0 /usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0
```
