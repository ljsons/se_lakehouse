# Databricks notebook source
import dlt
from pyspark.sql import functions as F

# COMMAND ----------

jsonPath = "abfss://"

# COMMAND ----------

def cleanse_column_names(df):
    """
    Cleanses the column names in a dataframe of all spaces.
    
    Args:
        df : DataFrame : Input data frame
        
    Returns:
        DataFrame : Data frame with cleansed column names
    """    
    # Cleanse the column names
    cleaned_columns = df.select([F.col(col).alias(col.replace(' ', '_')) for col in df.columns])
    
    # Rename the columns in the data frame
    df = df.toDF(*cleaned_columns)
    
    return df

# COMMAND ----------

@dlt.table(
    name = "bronze_results",
    comment = "raw data ingeste from object store"
)
def create_bronze_table():
    return (
        cleanse_column_names(spark.readStream.format("cloudFiles")
            .option("cloudFiles.format", "csv")
            .load("abfss://datalake@lsyckdemodatalake.dfs.core.windows.net/landing/deerharvest/"))
        

    )

# COMMAND ----------



# COMMAND ----------


