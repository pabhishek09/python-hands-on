from pyspark.sql import SparkSession

def create_spark_session():
    """Create a Spark Session"""
    return (
        SparkSession
        .builder
        .appName("SparkApp")
        .master("local[4]")
        .getOrCreate()
    )
