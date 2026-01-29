FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip \
    && pip install ipython pandas requests jupyter matplotlib numpy

CMD ["ipython"]
