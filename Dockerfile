FROM fedora:23
MAINTAINER rubin.diego@gmail.com

# System dependences 
# install cyclone system dependences
RUN dnf install -y libffi-devel
RUN dnf install -y gcc
RUN dnf install -y rpm-build

# install python2
RUN dnf install -y python-pip
RUN dnf install -y python-devel
RUN dnf install -y openssl-devel 

# Python dependences
RUN pip install flask
RUN pip install Flask-OAuth
RUN pip install pymongo==2.8

# Copy application
RUN mkdir /app
ADD bin /app/bin
ADD notes /app/notes
RUN ln -s /app/bin/spellchecker-server /usr/bin/spellchecker-server

WORKDIR /app/notes

EXPOSE 8084

