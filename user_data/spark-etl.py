#!/usr/local/bin/python3

import findspark
from datetime import datetime
# Inicializando Spark
findspark.init("/usr/spark-3.0.0/spark-3.0.0-bin-hadoop2.7/")

import pandas as pd
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType

spark = (
    SparkSession.builder.appName("sparksubmit_test_app")
    .master("yarn")
    .config("spark.sql.warehouse.dir", "hdfs:///user/hive/warehouse")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()
)


dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
pd_df = pd.read_csv("/user_data/events.csv", parse_dates=['date'], date_parser=dateparse)

schema = StructType([ StructField(pd_df.columns[0], TimestampType(), True)\
                   ,StructField(pd_df.columns[1], IntegerType(), True)\
                   ,StructField(pd_df.columns[2], StringType(), True)\
                   ,StructField(pd_df.columns[3], StringType(), True)])

df = spark.createDataFrame(data=pd_df, schema=schema)

df.write.format("delta").mode("overwrite").save("hdfs://spark-master:9000/datasets/events")  # noqa: F841

df.show()

# ToDo - Implemente o que tem que fazer
