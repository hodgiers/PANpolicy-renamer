FROM ubuntu:latest

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Update Software Repo
RUN apt update -y

# Install openssh client
RUN apt install -y openssh-client

RUN apt update -y
RUN apt install git -y
RUN apt install python3 -y
RUN apt install curl -y
RUN apt install python3-pip -y
RUN pip3 install python-dotenv
RUN pip3 install requests

# Set the working directory to scripts; we'll bind the local dev env to this dir in a volume at runtime
RUN mkdir /scripts
WORKDIR /scripts