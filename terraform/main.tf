provider "aws" {
  region = "us-west-2"
}

resource "aws_rds_instance" "asset_db" {
  engine           = "postgres"
  instance_class   = "db.t3.micro"
  allocated_storage = 20
  db_name          = var.db_name
  username         = var.db_username
  password         = var.db_password
  instance_identifier = "asset-db"
  publicly_accessible = true
}

resource "aws_s3_bucket" "asset_data_bucket" {
  bucket = "asset-management-data-bucket"
}

resource "aws_iam_role" "s3_access_role" {
  name = "s3-access-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_policy" "s3_access_policy" {
  name        = "s3-access-policy"
  description = "Allow EC2 to access the S3 bucket"
  policy      = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action   = "s3:GetObject",
      Effect   = "Allow",
      Resource = "${aws_s3_bucket.asset_data_bucket.arn}/*"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "role_policy_attachment" {
  role       = aws_iam_role.s3_access_role.name
  policy_arn = aws_iam_policy.s3_access_policy.arn
}