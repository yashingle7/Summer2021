provider "aws" {
  access_key = ""
  secret_key = ""
  region     = "ap-south-1"
}

resource "aws_instance" "example" {
  ami           = "ami-04db49c0fb2215364"
  instance_type = "t2.micro"
}
