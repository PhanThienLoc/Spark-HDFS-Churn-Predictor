from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Spark_HDFS_Integration") \
    .master("spark://spark-master:7077") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://namenode:9000") \
    .getOrCreate()

# Đọc dữ liệu từ HDFS
hdfs_path = "hdfs://namenode:9000/project/churn_analysis/data.csv"
df = spark.read.csv(hdfs_path, header=True, inferSchema=True)

# THÊM CÁC DÒNG NÀY ĐỂ XEM KẾT QUẢ
print("--- Đang lấy dữ liệu từ HDFS ---")
df.show(5)

print(f"Tổng số dòng dữ liệu trên HDFS: {df.count()}")