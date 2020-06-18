# Test Frisidea DRF Auth

Program test Login dan Register untuk interview di Frisidea menggunakan Django Rest Framework.

## Prasyarat
Selama development menggunakan:
- Python 3.6
- MariaDB 10.4.11 (juga support untuk MySQL)
- Django 3.0.7
- Django Rest Framework 3.11.0


## Instalasi
> Sangat direkomendasikan untuk menggunakan 
virtual environment. 

Clone project ini dan masuk ke direktori hasil clone.
Selanjutnya buat database di MariaDB (MySQL) dengan 
nama **db_frisidea**.

> Jika ingin mengubah pengaturan database, silahkan buka
file **database.cnf**.

Jika sudah, jalankan perintah berikut untuk melakukan instalasi
dependensi package yang dibutuhkan:

```
pip install -r requirements.txt
```

Setelah itu, lakukan migrasi:

```
python manage.py migrate
```

Setelah selesai migrasi, jalankan development
server dengan perintah:

```
python manage.py runserver
```
    
Server berjalan di **http://localhost:8000** sebagai 
base url API.

## API Endpoint
Melakukan Registrasi:

```
Endpoint:
/users/register/

Method:
POST

Headers:
Content-Type: application/json

Body:
{
    "username": "usernameanda",
    "password": "passwordanda",
    "email": "emailanda@mail.com"
}
```

Melakukan Login:

```
Endpoint:
/users/login/

Method:
POST

Headers:
Content-Type: application/json

Body:
{
    "username": "usernameanda",
    "password": "passwordanda"
}
```

Untuk menguji apakah authentication dan permission berhasil
saya juga sediakan endpoint untuk menampilkan pesan 
**"Halo usernameanda!"**:

```
Endpoint:
/users/

Method:
GET

Headers:
Content-Type: application/json
Authorization: Token {tokenanda}
```

