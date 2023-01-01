FROM selenium/standalone-chrome

USER root
RUN apt-get update && apt-get upgrade -y && apt install -y python3-pip

USER 1200
RUN pip3 install selenium
