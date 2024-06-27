from utils.session import create_spark_session
from utils.functions import rename_columns
from utils.tableschema import COL_NAME_MAP, SELECTED_COLUMNS
from pathconfig import create_path_snapshot, PATH_TOY_GAME_DATA
from sys import exit

def main():

    spark = create_spark_session()
    print('Session Started')

    # Read the data from the JSON file
    spark.conf.set("spark.sql.caseSensitive", "true")
    try: 
        raw_sdf = spark.read.json(PATH_TOY_GAME_DATA)
        raw_sdf.show()
        print('Data loaded', raw_sdf)
    except Exception as e:
        print('Error: Path not found', e)
        exit_program()

    # re-naming the columns
    raw_sdf = rename_columns(raw_sdf, COL_NAME_MAP)

    # select columns
    raw_sdf = raw_sdf.select(*SELECTED_COLUMNS)
    print(raw_sdf.show())
    
    PATH_SNAPSHOT = create_path_snapshot()
    raw_sdf = (
    raw_sdf
        .repartition("asin")
        .sortWithinPartitions("unix_review_time")
    )
    
    # Write data with partition and sorted
    # (
    # raw_sdf
    #     .write.partitionBy("asin")
    #     .mode("overwrite")
    #     .parquet(PATH_SNAPSHOT)
    # )

    # raw_sdf = spark.read.parquet(PATH_SNAPSHOT)

    spark.stop()
    print('Code Executed Successfully')

def exit_program():
    print("Exiting the program")
    exit(0)

if __name__ == "__main__":
    main()
