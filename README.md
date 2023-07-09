# Readme

## Projenin lokalinizde çalışması için gerekli olan yüklemeler

pip install django
pip install djangorestframework
pip install psycopg2

## Proje ve uygulama oluşturma komutları

django-admin startproject <project name>
python manage.py startapp <REST API>

## Projenin veritabanı bağlantısı

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'IHA_DEV',
'USER': 'ihaDevUser',
'PASSWORD': 'Dev_PaSSw0rd',
'HOST': 'localhost',
'PORT': '5435',
}
}

## Projenin docker ile çalıştırılması

docker-compose -f docker-compose-dev.yml up -d

## Model (veritabanı tablolarını) oluşturma adımları

python manage.py makemigrations <API APP name>
python manage.py migrate

## Projeyi lokalinizde çalıştırmak için gerekli komutlar

python manage.py runserver

## Projenin test kodlarını çalıştırmak için gerekli komutlar

python manage.py test

## Projenin frontend tarafının ayaklandırılması

npm install && npm start 

## Projenin Postman üzerinden test edilmesi için gerekli adımlar;

### 1- Github üzerinden indirilen postman collection’ı projeye import edilir.

![Untitled](https://github.com/rozdemir96/baykar_odev/assets/92824318/33c14b6b-9f93-4e3e-ab01-bda738fe75cf)


### 2- Users klasörü altındaki signup request’ine tıklanır ve açılan ekrandan body kısmına parametreler girilerek Send isteği atılır.

![Untitled](https://github.com/rozdemir96/baykar_odev/assets/92824318/d6d18c55-3ef6-43b4-9252-6bf6edef1212)


### 2.1-Başarıyla kayıt olduktan sonra veritabanı tablosundan kontrol edilir.

![1](https://github.com/rozdemir96/baykar_odev/assets/92824318/bb8ff557-6739-4f4f-8cbf-5ded01dea026)


### 2.2- Sistemde kayıtlı olan bir username ile kayıt olunmaya çalışıldığında *“A user with that username already exists.”* hatası kullanıcıya döndülür ve kayıt olamaz.

![22](https://github.com/rozdemir96/baykar_odev/assets/92824318/a5df749a-02c6-4393-a5db-b77dda896ab6)


### 2.3- Kullanıcının login olması için Users klasörü altındaki login request’ine tıklanır ve açılan ekrandan body kısmına parametreler girilerek Send isteği atılır.

![23](https://github.com/rozdemir96/baykar_odev/assets/92824318/da38f8c1-091b-4400-8629-6f0bb88c2bd1)


### 3- Kullanıcının iha oluşturması için Ihas klasörü altındaki create request’ine tıklanır ve açılan ekrandan body kısmına parametreler girilerek Send isteği atılır. Atılan istek sonucunda response olarak oluşturulan veriler id bilgisiyle birlikte kullanıcıya döndürülür.

![3](https://github.com/rozdemir96/baykar_odev/assets/92824318/11b35107-ab2f-4ea5-86f2-dd037977f3ec)


### 3.1- İlgili kayıt veritabanından kontrol edilir.

![31](https://github.com/rozdemir96/baykar_odev/assets/92824318/dfb14651-7275-4fae-b7be-90c0f82918dc)


### 3.2- Kullanıcının mevcut bir ihayı güncellemesi için Ihas klasörü altındaki update request’ine tıklayarak ilgili parametleri girer ve url kısmının sonuna güncellemek isteği iha’nın id bilgisini ekler ve response olarak güncellenmiş halini kullanıcıya döndürür.

![32](https://github.com/rozdemir96/baykar_odev/assets/92824318/9ffccbaa-5eeb-45b6-9b76-2a4d60094faa)


### 3.3- Güncellenen iha’nın veritabanındaki güncellendikten sonraki hali.

![33](https://github.com/rozdemir96/baykar_odev/assets/92824318/ca30bdf7-979a-471d-90e9-522bc9ab26cd)


### 3.4- Sistemdeki bütün ihaları görmek için Ihas klasörü altındaki get request’ine tıklanır ve Send isteği atılır. İstek sonucunda veritabanında bulunan bütün ihaları response olarak döner.

![34](https://github.com/rozdemir96/baykar_odev/assets/92824318/b3c28f83-4b8e-4ac9-b9ee-e39dc29290d5)


### 3.5- ihas tablosundaki kayıtlı olan bütün ihaların listesi;

![35](https://github.com/rozdemir96/baykar_odev/assets/92824318/e7000151-6c71-469c-a2ed-39a0a32b53b9)


### 3.6- Sistemde olan mevcut bir iha’yı silmek için Ihas klasörü altında bulunan delete request’ine tıklanır ve url’e silinmek istenen iha’nın id’si girilerek Send isteği gönderilir. Response olarak kullanıcıya mesaj döndürülür.

![36](https://github.com/rozdemir96/baykar_odev/assets/92824318/e5c1f72c-c493-4876-9278-9a4e8b3c1d14)


### 3.7- Delete isteği sonrasında ihas tablosunun son hali;

![37](https://github.com/rozdemir96/baykar_odev/assets/92824318/751bacdd-d5b8-46c4-850b-2dd8db2c1eee)


### 3.8- Iha Kiralama işlemlerinin yapılması için Rentals klasörü altındaki create request’ine tıklanır ve kullanıcı id, user id, başlangıç tarihi ve bitiş tarihi gönderilir. Kiralama işlemi başarılı olursa kullanıcıya response olarak mesaj döndülür.

![38](https://github.com/rozdemir96/baykar_odev/assets/92824318/1b9db975-0350-468a-982a-a7550bd4219b)


### 3.9- Kiralama isteği sonrası rentals tablosunun güncel hali;

![39](https://github.com/rozdemir96/baykar_odev/assets/92824318/fca7355f-c88c-48b1-88e2-4b9192e37648)


### 3.10- Farklı bir kullanıcı aynı ihayı kiralandığı saatler aralığında kiralamaya çalışırsa kullanıcıya hata mesajı döndürülür.

![310](https://github.com/rozdemir96/baykar_odev/assets/92824318/2c2d5477-95cb-418d-82ab-78cb298f29db)


### 3.11- Sistemdeki bütün kiralanan iha’ları görmek için Rentals klasörü altındaki get request’ine tıklanır ve Send isteği atılır. İstek sonucunda veritabanında bulunan bütün kiralanmış iha’lar response olarak dönülür.

![311](https://github.com/rozdemir96/baykar_odev/assets/92824318/0f3129d9-f0e9-4922-94b1-d7160fb77347)


### 3.12- İha kiralamada güncelleme yapılması için Rentals klasörü altındaki update request’ine istek atılır ve url’de güncellemesi istenen kaydın id’si eklenerek body’de kiralama bilgileri güncellenir ve kullanıcıya request olarak güncellenmiş hali dönülür.

![312](https://github.com/rozdemir96/baykar_odev/assets/92824318/2694ba37-30b7-4242-9318-0e261a040857)


### 3.13- Güncelleme yapıldıktan sonraki veritabanı tablosu;

![313](https://github.com/rozdemir96/baykar_odev/assets/92824318/bb9d4038-8a6b-4965-85b1-77fba3280aca)


### 3.14- Kiralama kaydı silinmek istendiğinde Rentals klasörü altındaki delete request’ine tıklanır ve url’e ilgili kaydın id’si girilerek Send isteği atılır.

![314](https://github.com/rozdemir96/baykar_odev/assets/92824318/d460dda2-ab5c-4b38-a003-22cd9813e267)


### 3.15- Silme yapıldıktan sonraki veritabanı tablosu;

![315](https://github.com/rozdemir96/baykar_odev/assets/92824318/0e7b7b86-b573-4c30-b9c9-455bd9ae85aa)

