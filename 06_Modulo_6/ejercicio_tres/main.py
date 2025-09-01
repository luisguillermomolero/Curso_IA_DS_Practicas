from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, length, regexp_replace, upper, trim
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
import requests

