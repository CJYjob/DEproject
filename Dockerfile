FROM apache/airflow:2.5.2
ENV PYTHONUNBUFFERED 1
COPY lib.txt /lib.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /lib.txt

FROM python:3.8
ENV PYTHONUNBUFFERED 1
COPY lib.txt /lib.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /lib.txt

