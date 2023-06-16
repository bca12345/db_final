select load_extension("./libparquet");
create virtual table vt using parquet("./data/census_a.parquet");
select avg(C13) from vt where C3 = "Canada";
