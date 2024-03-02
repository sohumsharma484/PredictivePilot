FROM ubuntu:22.04

LABEL maintainer="Daniel Philipov <dp33@illinois.edu>"

SHELL ["/bin/bash", "-c"]

######################################################
#               Install System Dependencies          #
######################################################

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git curl make
RUN apt-get install -y tar zip

######################################################
#               Install Rust and Cargo               #
######################################################

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

#######################################################
#         Install Python and Dependencies            #
######################################################

RUN apt-get install -y python3.10 python3-pip 
RUN cp /usr/bin/python3 /usr/bin/python
RUN pip3 install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

#######################################################

RUN source ~/.bashrc