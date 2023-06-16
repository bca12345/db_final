sudo apt-get install bison
tar -xf pypy_v.7.3.6.tar.gz
python3 -m pip install apsw
python3 -m pip install pymonetdb 
tar -xf pypy_v.7.3.6.tar.gz
wget https://s3.amazonaws.com/cldellow/public/libparquet/libparquet.so.xz
xz -d libparquet.so.xz
export LD_LIBRARY_PATH="$PWD/udfs/;$PWD/pypy2.7-v7.3.6-linux64/bin;$PWD/YeSQL_MonetDB/cffi_wrappers/"
export PYTHONPATH="$PWD/udfs"
export CURRENT=$PWD
