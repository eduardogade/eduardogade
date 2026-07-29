
from __future__ import annotations

""" Module 1
from __future__ import annotations

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("test").getOrCreate()

df = spark.read.csv("world.csv", header=True)

# Assume df is your dataframe and "country" is the column with duplicates
key_col = "country"

# All other columns
other_cols = [c for c in df.columns if c != key_col]

# Build aggregations: collect distinct values per column
agg_exprs = [
    F.collect_set(c).alias(c)
    for c in other_cols
]

debug_df = (
    df
    .groupBy(key_col)
    .agg(*agg_exprs)
)

# Show only countries that have duplicates
duplicates_df = (
    df
    .groupBy(key_col)
    .count()
    .filter(F.col("count") > 1)
)

result = (
    debug_df
    .join(duplicates_df, on=key_col)
)

result.show(truncate=False)
"""

"""
from __future__ import annotations

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()

df = spark.read.csv("world.csv", header=True)
df = df.filter("population > 100000000")

df.show()  # ← ACTION triggers execution
"""

""" Module 2
from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("test").getOrCreate()

input_path = "world.csv"
output_path = "world_cleaned"

key_col = "name"  # change to "country" if your country column is named country

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(input_path)
)

cols_to_check = [c for c in df.columns if c != key_col]

missing_score = sum(
    F.when(
        F.col(c).isNull() | (F.trim(F.col(c).cast("string")) == ""),
        1,
    ).otherwise(0)
    for c in cols_to_check
)

df_scored = df.withColumn("_missing_count", missing_score)

window = Window.partitionBy(key_col).orderBy(
    F.col("_missing_count").asc(),
    F.col("gdp").desc_nulls_last(),
)

world_cleaned = (
    df_scored
    .withColumn("_rank", F.row_number().over(window))
    .filter(F.col("_rank") == 1)
    .drop("_missing_count", "_rank")
)

world_cleaned.show(truncate=False)

world_cleaned.write.mode("overwrite").option("header", True).csv(output_path)
"""

# from pyspark.sql.types import StructType, StructField, StringType, FloatType, DoubleType, IntegerType, LongType
# from pyspark.sql import SparkSession
# from pyspark.sql import functions as F

# schema = StructType([
#     StructField("country", StringType(), True),
#     StructField("name", StringType(), True),
#     StructField("continent", StringType(), True),
#     StructField("area", FloatType(), True),
#     StructField("population", IntegerType(), True),
#     StructField("gdp", DoubleType(), True),
#     StructField("capitalLabel", StringType(), True),
#     StructField("tld", StringType(), True),
#     StructField("flag", StringType(), True),
# ])

# spark = SparkSession.builder.appName("test").getOrCreate()

# df = spark.read.csv("world.cleaned.csv", schema=schema, header=True)
# df = df.filter("population > 100000000")

# df = df.select(
#     F.col("name").alias("country"),
#     F.col("continent"),
#     F.col("area"),
#     F.col("population"),
#     F.col("gdp"),
# )

# df = df.withColumn("gdp", F.col("gdp") / 1_000_000_000)

# df.show()  # ← ACTION triggers execution


""" Module 3
from pyspark.sql.types import StructType, StructField, StringType, FloatType, DoubleType, IntegerType, LongType
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F

schema = StructType([
    StructField("country", StringType(), True),
    StructField("name", StringType(), True),
    StructField("continent", StringType(), True),
    StructField("area", FloatType(), True),
    StructField("population", IntegerType(), True),
    StructField("gdp", DoubleType(), True),
    StructField("capitalLabel", StringType(), True),
    StructField("tld", StringType(), True),
    StructField("flag", StringType(), True),
])

spark = SparkSession.builder.appName("test").getOrCreate()

df: DataFrame = spark.read.csv("world.cleaned.csv", schema=schema, header=True)

# Selection -> Projection -> Column Selection
df = df.select(
    F.col("name").alias("country"),
    F.col("continent"),
    F.col("area"),
    F.col("population"),
    F.col("gdp"),
)

# Filter / Where -> Row Selection
df = df.filter("population > 100000000")
# or
# df = df.where("population > 100000000")

# withColumn -> Feature Engineering
df = df.withColumn("gdp_per_capita", F.col("gdp") / F.col("population"))

# when / otherwise -> Conditional logic
df = df.withColumn(
    "country_status",
    F.when(F.col("gdp_per_capita") > 20_000, "rich").otherwise("poor")
)

# groupBy -> Aggregation -> Shuffle event (triggers Shuffle)
df = df.groupBy("country_status").agg(
    F.avg("gdp_per_capita").alias("avg_gdp_per_capita"),
    F.count("*").alias("n")
)

# OrderBy -> Ordering
df = df.orderBy(F.col("avg_gdp_per_capita").desc())

# Column Expressions -> Builds a single expression
df.withColumn(
    "complex",
    (F.col("age") * 2 + 10) / 3
)

df.show()  # ← ACTION triggers execution
"""


from pyspark.sql.types import StructType, StructField, StringType, FloatType, DoubleType, IntegerType, LongType
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F

schema_world = StructType([
    StructField("country", StringType(), True),
    StructField("name", StringType(), True),
    StructField("continent", StringType(), True),
    StructField("area", FloatType(), True),
    StructField("population", IntegerType(), True),
    StructField("gdp", DoubleType(), True),
    StructField("capitalLabel", StringType(), True),
    StructField("tld", StringType(), True),
    StructField("flag", StringType(), True),
])

schema_cities = StructType([
    StructField("cityLabel", StringType(), True),
    StructField("population", IntegerType(), True),
    StructField("countryCode", StringType(), True),
    StructField("country", StringType(), True),
])

schema_hdi = StructType([
    StructField("countryCode", StringType(), True),
    StructField("currencyLabel", StringType(), True),
    StructField("hdi", FloatType(), True),
    StructField("neighborCode", StringType(), True),
    StructField("country", StringType(), True),
])

spark = SparkSession.builder.appName("test").getOrCreate()

df_world: DataFrame = spark.read.csv("world.cleaned.csv", schema=schema_world, header=True)
df_cities: DataFrame = spark.read.csv("cities.cleaned.csv", schema=schema_cities, header=True)
df_hdi: DataFrame = spark.read.csv("hdi.neighborhood.cleaned.csv", schema=schema_hdi, header=True)

# Joins also require shuffle
# Shuffle -> network I/O, disk spill, repartitioning, and possible skew.

df_world = df_world.select(
    F.col("country").alias("cid"),
    F.col("name").alias("country"),
    (F.col("population").cast(FloatType()) / 1_000_000).alias("population_M"),  # ← cálculo inline
    F.col("continent"),
    F.col("area"),
    F.col("gdp"),
).filter("population_M > 100")

df_cities = df_cities.select(


)

joined_df = df_world.join(
    df_cities,
    on="cid",
    how="inner",
)

joined_df.show()  # ← ACTION triggers execution

# Exercícios práticos pra você fazer (do mais fácil ao mais pica)
# Com as duas tabelas carregadas no Spark, tente:

# Nível 1 (Fácil)
# INNER JOIN entre world e cities pelo código do país. Conte quantas cidades por país.
# LEFT JOIN entre world e cities. Quais países têm null no número de cidades?

# Nível 2 (Médio)
# RIGHT JOIN entre world e cities. Quais cidades estão em países que não estão na sua tabela world? (Isso mostra dados sujos no Wikidata.)
# Faça JOIN do world com country_indicators duas vezes: uma pra pegar a moeda, outra pra pegar o IDH.

# Nível 3 (Difícil - aí você vira senior)
# SELF-JOIN na world usando a coluna continent. Mostre pares de países do mesmo continente onde um tem população > dobro do outro.
# Usando country_indicators, faça GROUP BY countryCode e crie uma coluna com array de vizinhos. Depois junte com world e filtre países que fazem fronteira com Alemanha (DE).
# Por que isso é tão bom pra você treinar?

# Dado real e sujo — O Wikidata tem inconsistências (países sem código, cidades sem país). Você vai lidar com nulls e OPTIONAL que viram LEFT JOIN.
# Escala real — A query de cidades já vem com LIMIT 5000. No Spark você pode remover esse limite e ver a memória chorar. Aí aprende a otimizar.
# Múltiplas fontes — Você não tem um banco de dados relacional bonitinho. Tem que extrair do Wikidata e depois juntar. É exatamente o que Data Engineer faz.
# Se quiser algo ainda mais próximo do mundo real

# No lugar de LIMIT, use OFFSET pra particionar os dados (técnica de paginação). Exemplo: roda a mesma query 4 vezes com OFFSET 0, OFFSET 5000, OFFSET 10000... e depois faz UNION no Spark. Isso treina leitura paralela de APIs.
