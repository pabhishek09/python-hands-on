from pyspark.sql import DataFrame as SparkDf

def rename_columns(df: SparkDf, column_map):
    for old, new in column_map.items():
            df = df.withColumnRenamed(old, new)
    return df
