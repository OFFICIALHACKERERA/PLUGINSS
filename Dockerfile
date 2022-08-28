FROM LEGEND-AI/LEGENDBOT:slim-buster

#clonning repo 

RUN git clone https://github.com/LEGEND-AI/LEGENDUSERBOT.git /root/userbot

#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/Deepak/bin:$PATH"

CMD ["python3","-m","Deepak"]

FROM python:3.9.7-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN python3 -m pip install --upgrade pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt
CMD bash start

