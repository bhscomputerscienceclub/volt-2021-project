FROM alpine:3.13
WORKDIR /code
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk update
RUN apk add --no-cache py3-enchant py3-pip hunspell-en aspell-en
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
CMD ["flask","run"]
