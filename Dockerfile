FROM apache/airflow:2.5.2
COPY lib.txt /lib.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /lib.txt
COPY requirements.txt /requirements.txt
RUN pip insatll -r requirements.txt


