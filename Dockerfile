FROM python:3.6.8-alpine

WORKDIR /apps/

COPY app/ /apps/

WORKDIR /apps/

RUN pip install -U pip setuptools && pip install -r /apps/requirements.txt

EXPOSE 5060

ENTRYPOINT ["python"]

CMD ["app.py"]
