FROM ubuntu:16.04
RUN apt-get update

# Install python, pip git
RUN apt-get install -y python3-setuptools python3-pip git
RUN pip3 install absl-py
RUN git clone https://github.com/eastsideod/conways_game_of_life.git

CMD ["python3 -m conways_game_of_life"]

# docker build -t cglol:0.0 .
# docker run -it --name cgol cgol:0.0
