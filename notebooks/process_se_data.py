# Databricks notebook source
import dlt
import json
from pyspark.sql.functions import *
from datetime import datetime

# COMMAND ----------

dbutils.widgets.text("paramsJson", "")

# COMMAND ----------

testParams = """[
    {
        "schemaName": "pos",
        "tableName": "order_coupon_dom",
        "landingZonePath": "/edw/files/input/pos/extract_type/OC2/",
        "format": "csv",
        "includesHeader": "true",
        "encoding": "UTF-16",
        "delimiter": "\\t",
        "bronzeTableSettings": {
            "name": "order_coupon_dom"
        },
        "primaryKeys" : ["OrdCpnNbr"]
    },
    {
        "schemaName": "pos",
        "tableName": "order_coupon_dom",
        "landingZonePath": "/edw/files/input/pos/extract_type/OCX/",
        "format": "csv",
        "includesHeader": "true",
        "encoding": "UTF-16",
        "delimiter": "\\t",
        "bronzeTableSettings": {
            "name": "order_coupon_intl"
        },
        "primaryKeys" : ["OrdCpnNbr"]
    }
]"""

passedParams =  dbutils.widgets.get("paramsJson") 
datasets = json.loads(passedParams or testParams)

# COMMAND ----------

for dataset in datasets:
   

# COMMAND ----------


