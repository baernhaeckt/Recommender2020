FROM python:3.8

# Installing Python dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt

# The project
RUN mkdir /app
COPY simple_recommender.py /app

# The starting script
WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python", "simple_recommender.py"]
