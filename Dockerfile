FROM python:3.6-alpine3.7

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN apk add xvfb


# install selenium
RUN pip install selenium==3.8.0

ADD ./src /code
WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "main.py"]
VOLUME [ "/code/static/storage" ]