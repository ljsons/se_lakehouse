# Databricks notebook source
#import dlt
import json

# COMMAND ----------

dbutils.widgets.text("paramsJson", "")

# COMMAND ----------

testParams = """{
    "source": "pos",
    "tableName": "order_coupon_dom",
    "landingZonePath": "edw/files/input/pos/extract_type/OC2/",
    "format": "csv",
    "includesHeader": "true",
    "encoding": "UTF-16",
    "delimiter": "t",
    "bronzeTableSettings": {
        "name": "order_coupon_dom"
    }
}"""

# COMMAND ----------

passedParams =  dbutils.widgets.get("paramsJson") 
params = json.loads(passedParams or testParams)

print(params.get("source"))

print(f"bronze_{params.get('source')}_{params.get('tableName')}")

print(f"_{params.get('tableName')}")

# COMMAND ----------

def generate_bronze_table(params):
    tableProperties = {"quality": "bronze"}
    
    additionalTableProperties = params.get('BronzeSettings', {}).get('tableProperties')

    if additionalTableProperties: 
        tableProperties.update(additionalTableProperties)
    
    @dlt.table(
        name = f"
    )

# COMMAND ----------

""
