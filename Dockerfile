FROM python:3.6
MAINTAINER Nick Goldstein <nick@nickgoldstein.com>
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /opt/nick
CMD python /opt/nick/manage.py runserver 0.0.0.0:80
