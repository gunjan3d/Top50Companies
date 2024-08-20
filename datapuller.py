import boto3
import pandas as pd

# S3 configuration
s3 = boto3.client('s3',
                  aws_access_key_id='AKIA4MTWJLROOCGSRAMY',
                  aws_secret_access_key='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',
                  region_name='ap1-south-1')

# Specify the S3 bucket and filepip 
bucket_name = 'gunjan-companies'
file_key = 'https://gunjan-companies.s3.ap-south-1.amazonaws.com/companies.csv'

# Download the file from S3
s3.download_file(bucket_name, file_key, 'companies.csv')

# Load the data into a pandas DataFrame
df = pd.read_csv('companies.csv')
