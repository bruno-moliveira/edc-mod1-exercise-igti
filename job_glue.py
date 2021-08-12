import sys
from pyspark.context import SparkContext
from awsglue.utils import getResolverdOptions
from awsglue.context import GlueContext
from awsglue.jo import Job

args = gerResolvedOptions(sys.argv,['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#A partir daqui, mesmo codigo do emr

#ler os dados do enem 2019
enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-bruno-361571665651/raw_data/enem/")
)

(
   enem
   .write
   .mode("overwrite")
   .format("parquet")
   .partitionBy("year")
   .save("s3://datalake-bruno-361571665651/staging/enem-glue/")
)