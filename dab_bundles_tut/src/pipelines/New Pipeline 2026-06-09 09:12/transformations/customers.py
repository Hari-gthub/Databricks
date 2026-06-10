from pyspark import pipelines as dp

@dp.materialized_view(
    table_properties = {"quality":"bronze"},
    name = "customers_tbl_bronze_2",
    comment = "customers bronze tbl is created ."
)
def mat_view () :
    df = spark.read.table("workspace.default.customers_bronze")
    return df  