import boto3
import pandas as pd 

s3_client = boto3.client('s3')

##//s3_client.download_file("datalake-bruno-igti-edc","data/geoMap.csv","geoMap.csv")

##df = pd.read_csv("D:/Documentos/Treinamento/IGTI/Engenharia de Dados Cloud/1 Módulo - Fundamentos em arquitetura de dados e soluções em Nuvem/1.Code/geoMap.csv", sep=",")
##print(df)


s3_client.upload_file("D:/Documentos/Treinamento/IGTI/Engenharia de Dados Cloud/1 Módulo - Fundamentos em arquitetura de dados e soluções em Nuvem/1.Code/MICRODADOS_ENEM_2019.csv",
                    "datalake-bruno-361571665651",
                    "raw_data/enem/year=2019/MICRODADOS_ENEM_2019.csv")
                    