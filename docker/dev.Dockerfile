FROM brazildatacube/base:0.1

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# CMD [ "python3", "manage.py", "run" ]
