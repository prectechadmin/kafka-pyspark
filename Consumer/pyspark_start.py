from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
import time

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.1.0,org.apache.spark:spark-sql-kafka-0-10_2.11:2.1.0 pyspark-shell'

time.sleep(50)

spark = SparkSession \
    .builder \
    .appName("Starlizard Kafka Data Pipeline") \
    .getOrCreate()

prices_df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka_cluster:9092") \
  .option("subscribe", "prices-topic") \
  .load()

# send the data on the topic to the console
query = prices_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
