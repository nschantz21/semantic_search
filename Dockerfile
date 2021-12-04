# use lite weight python image
FROM python:3.7-slim-buster

# set the active directory in the container - GCP will expect this
ENV APP_HOME /app
WORKDIR $APP_HOME
# copy everything from source directory to the image filesystem
COPY . ./

# install the package requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# initialize the HTTP server using gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
