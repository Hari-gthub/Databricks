from pyspark import pipelines as dp

@dp.materialized_view(
    table_properties = {"quality":"bronze"},
    name = "orders_tbl_bronze_2",
    comment = "Orders bronze tbl is created ."
)
def mat_view () :
    df = spark.read.table("workspace.default.orders_bronze")
    return df  





@dp.materialized_view(
    table_properties = {"quality":"silver"},
    name = "joined_both_tbls_1",
    comment = "joined silver tbl is created ."
)
def joined_bth_tbls () :
    df_orders = spark.read.table("orders_tbl_bronze_2")
    df_customers = spark.read.table("customers_tbl_bronze_2")

    df_join = df_orders.join(df_customers, how = "left_outer", on = df_orders.o_custkey == df_customers.c_custkey)
    return df_join  