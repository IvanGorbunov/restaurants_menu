FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /restaurants_menu

# install dependences
COPY ./requirements.txt /restaurants_menu/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r /restaurants_menu/requirements.txt

# set open port
EXPOSE 8027











