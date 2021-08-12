#HCL - Hashicorp Configuration Languade
# Linguagem declarativa

resource "aws_s3_bucket" "datalake" {
  #parametros de configuração
  bucket = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}"
  acl    = "private"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    IES   = "IGTI"
    CURSO = "EDC"
  }

}

resource "aws_s3_bucket_object" "codigo_spark" {
  bucket = aws_s3_bucket.datalake.id
  key    = "emr-code/pyspark/job_spark_from_tf.py"
  acl    = "private"
  source = "D:/Documentos/Treinamento/IGTI/Engenharia de Dados Cloud/1 Módulo - Fundamentos em arquitetura de dados e soluções em Nuvem/1.Code/job_spark_emr.py"
  etag   = filemd5("D:/Documentos/Treinamento/IGTI/Engenharia de Dados Cloud/1 Módulo - Fundamentos em arquitetura de dados e soluções em Nuvem/1.Code/job_spark_emr.py")

}

provider "aws" {
  region = "us-east-2"
}


