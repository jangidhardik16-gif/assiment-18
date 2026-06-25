from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PartitionExample") \
    .getOrCreate()

df = spark.range(0, 5_000_000)

print(f"Initial number of partitions: {df.rdd.getNumPartitions()}")

df_repartitioned = df.repartition(12)
print(f"Number of partitions after repartition(12): {df_repartitioned.rdd.getNumPartitions()}")

df_coalesced = df_repartitioned.coalesce(3)
print(f"Number of partitions after coalesce(3): {df_coalesced.rdd.getNumPartitions()}")

print(f"Total records: {df_coalesced.count()}")

spark.stop()