FROM python:3.9.5-buster

RUN mkdir /website_tutorial
WORKDIR /website_tutorial

COPY . .

RUN pip install -e .

CMD exec gunicorn --bind 0.0.0.0:8090 'dash_website.index:get_server()'

# docker build -t gcr.io/age-prediction-306519/website_tutorial:answer .
# TO CHECK IF IT WORKS LOCALLY: docker run -p 8090:8090 gcr.io/age-prediction-306519/website_tutorial:answer
# docker push gcr.io/age-prediction-306519/website_tutorial:answer