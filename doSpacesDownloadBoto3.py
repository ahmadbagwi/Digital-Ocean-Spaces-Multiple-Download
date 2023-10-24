import requests
import boto3
import botocore
import os
from decouple import config
from slugify import Slugify

class Download:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def getByCat(self):
        url = f"{config('URL')}/{self.b}/{self.c}/{self.d}"
        response = requests.get(url)
        list = response.json()
        slug_name = Slugify(to_lower = True)
        slug_name.separator = '_'
        for j in list:
            for key, val in j.items():
                if (key == 'name'):
                    # print(slug_name(val))
                    self.downloadFiles(slug_path = f"2023/{slug_name(val)}")

    def downloadFiles(self, slug_path):
        if (self.a == 'di'):
            dir = 'di'
        elif (self.a == 'sm'):
            dir = 'sm'
        elif (self.a=='pkki'):
            dir = 'pkki'
        elif (self.a== 'prp'):
            dir = 'prp'
        
        new_dir_path = f"/home/ahmad-wsl22/web/python/dani/{dir}/{slug_path}"
        if os.path.isdir(new_dir_path) == False:
            os.mkdir(new_dir_path)

        session = boto3.session.Session()
        client = session.client('s3',
                    config=botocore.config.Config(s3={'addressing_style': 'virtual'}),
                    region_name=config('REGION_NAME'),
                    endpoint_url='https://sgp1.digitaloceanspaces.com',
                    aws_access_key_id=config('PUBLIC_KEY'),
                    aws_secret_access_key=config('SECRET_KEY')
                )
        response = client.list_objects(Bucket=config('SPACE_NAME'), Prefix = slug_path, MaxKeys = 1000)
        for obj in response['Contents']:
            if (os.path.isfile( f"/home/ahmad-wsl22/web/python/dani/{dir}/{obj['Key']}")):
                print(f"file sudah ada, lewati {obj['Key']}")
            else:
                client.download_file(config('SPACE_NAME'),
                    obj['Key'],
                    f"/home/ahmad-wsl22/web/python/dani/{dir}/{obj['Key']}"
                )
                print(f"berhasil download {obj['Key']}")
