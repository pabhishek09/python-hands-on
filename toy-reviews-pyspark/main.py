from pyspark.sql import SparkSession
from sys import exit

def main():

    def create_spark_session():
        """Create a Spark Session"""
        return (
            SparkSession
            .builder
            .appName("SparkApp")
            .master("local[5]")
            .getOrCreate()
        )
    # Create a spark session
    spark = create_spark_session()
    print('Session Started')

    # Read the data from the JSON file
    spark.conf.set("spark.sql.caseSensitive", "true")
    try: 
        PATH_BIGDATA = './toy-reviews-pyspark/dataset/Toys_and_Games_5.json'
        raw_sdf = spark.read.json(PATH_BIGDATA)
        raw_sdf.show()
        print('Data loaded', raw_sdf)
    except Exception as e:
        print('Error: Path not found', e)
        exit_program()

    # Renaming the columns
    COL_NAME_MAP = {
        "overall": "overall",
        "verified": "verified",
        "reviewTime": "review_time",
        "reviewerID": "reviewer_id",
        "asin": "asin",
        "reviewerName": "reviewer_name",
        "reviewText": "review_text",
        "summary": "summary",
        "unixReviewTime": "unix_review_time",
        "style": "style",
        "vote": "vote",
        "image": "image"
    }
    def rename_columns(df, column_map):
        for old, new in column_map.items():
                df = df.withColumnRenamed(old, new)
        return df
    raw_sdf = rename_columns(raw_sdf, COL_NAME_MAP)

    # select columns
    SELECTED_COLUMNS = [
        "reviewer_id",
        "asin",
        "review_text",
        "summary",
        "verified",
        "overall",
        "vote",
        "unix_review_time",
        "review_time",
    ]
    raw_sdf = raw_sdf.select(*SELECTED_COLUMNS)
    print(raw_sdf.show())

    spark.stop()
    print('Code Executed Successfully')

def exit_program():
    print("Exiting the program")
    exit(0)

if __name__ == "__main__":
    main()

