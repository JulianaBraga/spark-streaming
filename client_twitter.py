from pyspark.sql import SparkSession
from pyspark.sql import functions as f

spark = SparkSession \
        .builder \
        .appName("SparkStreaming") \
        .getOrCreate()

# Código para criação do DF
lines = spark.readStream \
    .format('socket') \
    .option('host', 'localhost') \
    .option('port', 9009) \
    .load()

# Pega palavras para a construção da nuvem
# A função explode é responsável por colocar cada palavra em uma linha

words = lines.select(f.explode(f.split(lines.value, ' ')).alias('word'))
word_count = words.groupBy('word').count()

print("*"*50)
print(words)
print("*"*50)

query = word_count.writeStream \
    .outputMode('complete') \
    .format('console') \
    .start()

# Para esperar a gente encerrar o fluxo
query.awaitTermination()
