provider "aws" {
  region = var.aws_region
}

#Centralizar o arquivo de controle de estado do terrafom
terraform {
  backed "s3" {
    bucket = "terraform-state-igti-bru"
    key = "state/igti/edc/mod1/terraform.tfstate"
    region = "us-east-2"
  }
}