FROM python:3.8

# Installing Python dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt

# The project
RUN mkdir /app
COPY main.py /app

# Install nltk dependencies
RUN [ "python", "-c", "import nltk; nltk.download('stopwords'); nltk.download('punkt')" ]

# Set the workdir
WORKDIR /app

# Expose the flask port
EXPOSE 5000

ENTRYPOINT ["python", "main.py"]
