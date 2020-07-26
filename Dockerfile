FROM ubuntu

RUN apt-get update
RUN apt-get install -y python

COPY . /opt/source-code

CMD [ "python", "./opt/source-code/ParallelDemo.py" ]