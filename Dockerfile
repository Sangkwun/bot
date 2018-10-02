FROM tiangolo/uwsgi-nginx-flask:python3.5

WORKDIR '/app'


COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .
#COPY requirements.txt .
#RUN pip install -r requirements.txt
