import boto3
from botocore.exceptions import NoCredentialsError
import os

def upload_to_s3(file_path, bucket_name, object_name=None):
    s3_client = boto3.client('s3')
    
    if object_name is None:
        object_name = os.path.basename(file_path)
    
    try:
        s3_client.upload_file(
            file_path, 
            bucket_name, 
            object_name, 
            ExtraArgs={'ObjectLockMode': 'GOVERNANCE'}
        )
        print(f"{file_path} başarıyla S3'e yüklendi ve Object Lock ile korundu.")
    except NoCredentialsError:
        print("AWS kimlik bilgileri bulunamadı.")
    except Exception as e:
        print(f"Yükleme sırasında bir hata oluştu: {e}")

if __name__ == "__main__":
    upload_to_s3("important_data.txt.enc", "my-s3-bucket")
