# Digital Ocean Spaces Multiple Download
### doSpacesDownloadBoto3.py
Script Python untuk mengunduh file dari Digital Ocean Spaces berdasarkan kategori tertentu.

## Konsep
Saya memiliki layanan pada website dimana setiap pengguna mendaftar akun dan mengunggah file. Kemudian saya butuh unduh file-file tersebut berdasarkan kriteria tertentu.

## Alur
1. Tentukan parameter yang dibutuhkan (baris 10-13)
```
a = direktori kategori
b = program_id
c = periode_id
d = status
```
2. Panggil data akun yang akan diunduh filenya (baris 15)
3. Ubah nama akun menjadi slug, hal ini karena direktori pada spaces pun dinamakan menggunakan slug (16-19)
4. Looping proses unduh dengan memanggil fungsi downloadFiles (baris 24)
5. Periksa dimana direktori lokal tempat penyimpanan hasil unduh berdasarkan kategori (sm, di, pkki) (baris 27-46)
6. Cek direktori lokal yang memuat kategori dan slug, jika belum ada buat baru (baris 48-50)
7. Inisiasi boto3 (baris 52-59)
8. Looping proses unduh file berdasarkan kategori dan slug, cek file di lokal, unduh jika belum ada (baris 61-69)

## Cara Kerja
```
$ python3
from doSpacesDownloadBoto3 import Download
di = Download('di', '3', '4', 'terkirim')
prosesDi = di.getByCat()
```
## File env
Isi file .env
```
URL=http://localhost:8001/data/download
REGION_NAME = "sgp1"
SPACE_NAME = "myspaces"
PUBLIC_KEY = "xxxyyyzzz"
SECRET_KEY = "mysecretkey"
BASE_PATH = "/home/ahmad-wsl22/web/python/dani"
```