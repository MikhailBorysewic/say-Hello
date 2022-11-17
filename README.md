# Run project
```commandline
cd greeting
python manage.py migrate
python manage.py runserver
```

or if you have docker installed:
```commandline
cd greeting
docker build .
docker run -p 8000:8000 --network host BUILDED_CONTAINER_ID
```
Open url in your browser:

http://127.0.0.1:8000/hello/?name=Rekruto&message=%D0%94%D0%B0%D0%B2%D0%B0%D0%B9%20%D0%B4%D1%80%D1%83%D0%B6%D0%B8%D1%82%D1%8C