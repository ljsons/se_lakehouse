# Databricks notebook source
import dlt
import json
from pyspark.sql.functions import *
from datetime import datetime


# COMMAND ----------

#get this from Key Vault 
dataLakeAcct = "abfss://datalake@lsyckdemodatalake.dfs.core.windows.net"

# COMMAND ----------

dbutils.widgets.text("paramsJson", "")

# COMMAND ----------



# COMMAND ----------

testParams = """[{
    "source": "bikeshare",
    "tableName": "divvystations_bundle",
    "landingZonePath": "/divvy/",
    "format": "csv",
    "includesHeader": "true",
    "encoding": "UTF-8",
    "delimiter": ",",
    "bronzeTableSettings": {
        "name": "divvystations"
    }
}]"""

passedParams =  dbutils.widgets.get("paramsJson") 
datasets = json.loads(passedParams or testParams)

# COMMAND ----------

def load_bronze_table(params):
    tableName = params.get('tableName')
    schemaName = params.get('schemaName')
    dataPath = f"{dataLakeAcct}{params.get('landingZonePath')}"
    primaryKeys = params.get("primaryKeys")

    cloudFile = {
        "cloudFiles.format": f"{params.get('format')}",
        "delimiter": f"{params.get('delimiter')}",
        "header": f"{params.get('includesHeader')}",
        "encoding": f"{params.get('encoding')}",
        "cloudFiles.inferColumnTypes": "true",
        "cloudFiles.schemaHints": "online_date string"
    }

    driftConf = {
        "cloudFiles.schemaEvolutionMode": "rescue",
        "rescuedDataColumn": "_rescued_data"
    }

    @dlt.table(
        name = f"bronze_{schemaName}_{tableName}"
    )
    def incremental_bronze():
        df = (spark.readStream
                .format("cloudFiles")
                .options(**cloudFile)
                .options(**driftConf)
                .load(dataPath)
        )
        
        ## Currenlty not working on first run.
        ##df = df.withColumn("sourceFile", col(source_metadata.file_path) )
        df = df.withColumn("_load_date", lit(datetime.now()))
        return (
            df
        )

# COMMAND ----------

for dataset in datasets:
    load_bronze_table(dataset)

# COMMAND ----------


