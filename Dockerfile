FROM python:3.8.15-buster
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 vlc -y

COPY project/requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY project/*.py /app/
COPY project/labels.csv /app/

WORKDIR /app

CMD python /app/detect.py
