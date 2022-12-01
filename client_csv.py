from pyspark.sql import SparkSession
from pyspark.sql import functions as f
import shutil

for item in ['/.csv', './check']:
    try:
        shutil.rmtree(item)
    except OSError as err:
        print(f'ALERT: {err.strerror}')

spark = SparkSession \
        .builder \
        .appName("SparkStreaming") \
        .getOrCreate()

# Código para criação do DF
tweets = spark.readStream \
    .format('socket') \
    .option('host', 'localhost') \
    .option('port', 9009) \
    .load()


query = tweets.writeStream \
    .outputMode('append') \
    .option('enconding', 'utf-8') \
    .format('csv') \
    .option('path', './csv') \
    .option('checkpointLocation', './check') \
    .start()

# Para esperar a gente encerrar o fluxo
query.awaitTermination()
