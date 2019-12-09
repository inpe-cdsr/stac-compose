FROM brazildatacube/base:0.1

RUN apt-get update && apt-get install -y build-essential

ADD . /bdc-stac-compose

WORKDIR /bdc-stac-compose

RUN pip3 install -r requirements.txt

VOLUME /data

CMD [ "python3", "manage.py", "run" ]