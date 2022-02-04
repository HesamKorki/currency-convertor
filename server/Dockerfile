# pull official python image
FROM python:3.8-slim

# set working directory
ENV DockerHome=/home/services/convertor-api

# create the working directory
RUN mkdir -p ${DockerHome}


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy the working directory
COPY requirements.txt ${DockerHome}

# set the working directory
RUN mkdir -p ${DockerHome}/src
WORKDIR ${DockerHome}

# install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy the working directory
COPY ./src ${DockerHome}/src

CMD python src/server/main.py