#!/usr/local/bin/python3

import findspark
# Inicializando Spark
findspark.init("/usr/spark-3.0.0/spark-3.0.0-bin-hadoop2.7/")

import pandas as pd
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType

spark = (
    SparkSession.builder.appName("sparksubmit_test_app") \
    .master("yarn") \
    .config("spark.submit.deployMode", "client") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()
)


df = spark.read.format("delta").load("hdfs://10.1.1.20:9000/datasets/events")

df.show()

df.printSchema()

# ToDo - Implemente o que tem que fazer
