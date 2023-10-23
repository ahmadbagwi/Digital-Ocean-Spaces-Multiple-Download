from spaces import Client
from slugify import Slugify
from decouple import config
import requests
import glob
import sys

def getByCat(a, b):
    url = f"http://localhost:8001/export/administrasi-download/{a}/4/terkirim"
    response = requests(url)
    list = response.json()
    slug_name = Slugify(to_lower=True)
    slug_name.separator = '_'
    for j in list:
        for key, val in j.items():
            if (key == 'name'):
                download(slug_name(val), b)

def download(slug, b):
    if (b == 'di'):
        dir = 'di'
    elif (b == 'sm'):
        dir = 'sm'
    elif (b=='pkki'):
        dir = 'pkki'
    elif (b== 'prp'):
        dir = 'prp'

    client = Client(
        region_name = config('REGION_NAME'),
        space_name = config('SPACE_NAME'),
        public_key = config('PUBLIC_KEY'),
        secret_key = config('SECRET_KEY')
    )

    files = client.list_files(
        path='2023/'+slug+'/'
    )
    # print(type(files))
    # print(files[0])
    for list in files:
        #print (list)
        for key, val in list.items():
            if (key == 'Key'):
               # print(val)
                client.download_file(
                    file_name=val,
                    destination='/home/ahmad-wsl22/web/python/dani/'+dir+'/',
                    space_name=None
                )
    print (f"berhasil download ({a})")

if __name__ == "__main__":
    getByCat(sys.argv[1])