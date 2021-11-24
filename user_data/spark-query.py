#!/usr/local/bin/python3

import findspark
# Inicializando Spark
findspark.init("/usr/spark-3.0.0/spark-3.0.0-bin-hadoop2.7/")

import pandas as pd
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType

def main():

    spark = (
        SparkSession.builder.appName("sparksubmit_test_app")
        .config("spark.sql.warehouse.dir", "hdfs:///user/hive/warehouse")
        .config("spark.sql.catalogImplementation", "hive")
        .getOrCreate()
    )

    df = spark.read.format("parquet").\
        load("hdfs://spark-master:9000/datasets/events.parquet")

    df.show()

    df.printSchema()

    # ToDo - Implemente o que tem que fazer


if __name__ == "__main__":
    main()
