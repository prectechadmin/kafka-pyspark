FROM ubuntu:latest
USER root

WORKDIR /starlizard_comsumer

# Install OpenJDK 8
RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/*

# Install Python
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa

RUN  apt install -y python3.7 && \
     apt install -y python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install PySpark
COPY requirements.txt requirements.txt
COPY pyspark_start.py app_start.py
RUN \
    pip3 install -r requirements.txt


# Define default command
#CMD ["./wait-for-it.sh", "kafka_cluster:9092", "-s", "--timeout=20", "--", "python3", "app_start.py"]
CMD ["python3", "app_start.py"]