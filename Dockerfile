# base image
FROM python:3.11.7-alpine3.18


# environment variable
ENV APP /PYTHON-WEB-1-HOMEWORK


# working directory
WORKDIR $APP


# copy our project
COPY . .


ENTRYPOINT ["python", "__main__.py"]