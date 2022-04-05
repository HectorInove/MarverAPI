FROM python:3.9.5
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /opt/back_end
COPY . /opt/back_end
CMD python marvel_api/manage.py runserver 0.0.0.0:8000