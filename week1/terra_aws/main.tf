terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"

    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "eu-central-1"
  profile = "default-adachypay"
}

resource "aws_instance" "app_server" {
  ami           = "ami-066866b740d9ce5a7"
  instance_type = "t2.micro"
  tags = {
    Name = var.instance_name
  }
}