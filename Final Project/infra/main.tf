provider "aws" {
  region = "us-west-2"
}

resource "aws_vpc" "app_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = {
    Name = "app_vpc"
  }
}

resource "aws_subnet" "app_subnet" {
  vpc_id            = aws_vpc.app_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-west-2a"
  tags = {
    Name = "app_subnet"
  }
}

resource "aws_security_group" "app_sg" {
  name        = "app_sg"
  description = "Allow web traffic to app"
  vpc_id      = aws_vpc.app_vpc.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "app_sg"
  }
}

resource "aws_instance" "app_instance" {
  ami           = "ami-0c55b159cbfafe1f0" # Example AMI for Amazon Linux 2
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.app_subnet.id
  security_groups = [aws_security_group.app_sg.name]

  tags = {
    Name = "FlaskAppInstance"
  }
}

resource "aws_db_instance" "app_db" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "postgres"
  engine_version       = "12.4"
  instance_class       = "db.t2.micro"
  name                 = "appdb"
  username             = "admin"
  password             = "securepassword"
  parameter_group_name = "default.postgres12"
  db_subnet_group_name = aws_db_subnet_group.app_db_subnet_group.name
  vpc_security_group_ids = [aws_security_group.app_sg.id]

  tags = {
    Name = "AppDBInstance"
  }
}

resource "aws_db_subnet_group" "app_db_subnet_group" {
  name       = "app_db_subnet_group"
  subnet_ids = [aws_subnet.app_subnet.id]

  tags = {
    Name = "app_db_subnet_group"
  }
}
