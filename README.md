# Topfood API

API for auto generation and printing checks with swagger documentation.

 ### Features

 - Admin panel with filters /admin/
 - Documentation is located at /api/schema/swagger/
 - Auto generation PDF checks 
 - Printing PDF checks 

 ## Installing
    Docker should be installed
 ```shell
 git clone https://github.com/KatrinLazarenko/topfood.git
 git checkout main
 python -m venv venv
 source venv/bin/activate (macOS) or venv\Scripts\activate (Windows)
 pip install -r requirements.txt
 docker-compose up
 python manage.py migrate
 python manage.py runserver
 celery -A topfood worker -l INFO
