FROM python:3.9

WORKDIR /app

#install requirements

COPY requirements.txt requirements.txt
RUN apt-get install pkg-config && apt-get install sentencepiece && pip install sentencepiece && pip install --upgrade pip && pip3 install -r requirements.txt

# Copy the rest of the application code to the working directory 
COPY . /app/
EXPOSE 9001

# Set the entrypoint for the container
CMD ["hypercorn", "--bind", "0.0.0.0:9001", "api:app"]
