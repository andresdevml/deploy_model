FROM  python:3.11

RUN mkdir -p /home/app

COPY . /home/app

WORKDIR /home/app

RUN pip install -r requirements.txt

EXPOSE 2205:2205

CMD ["python3","server.py"]

