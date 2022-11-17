FROM python:3.9-slim

WORKDIR /usr/src/app

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations
CMD ["python", "manage.py", "runserver"]