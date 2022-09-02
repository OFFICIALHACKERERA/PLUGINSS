FROM LEGEND-AI/LEGENDBOT:slim-buster

#clonning repo 

RUN git clone https://github.com/LEGEND-AI/LEGENDUSERBOT.git /root/userbot

#working directory 
WORKDIR /root/Deepak

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/Deepak/bin:$PATH"

CMD ["python3","-m","Deepak"]



RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_17.x | bash -
RUN apt-get install -y nodejs
COPY . /app
WORKDIR /app
RUN pip3 install -U -r requirements.txt
CMD python3 Deepak
