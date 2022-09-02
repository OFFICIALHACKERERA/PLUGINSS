FROM LEGEND-AI/LEGENDBOT:slim-buster

#clonning repo 

RUN git clone https://github.com/LEGEND-AI/LEGENDUSERBOT.git /root/userbot

#working directory 
WORKDIR /root/Deepak

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/Deepak/bin:$PATH"

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs 15.0.0+

CMD ["python3","-m","Deepak"]



