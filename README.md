# polly
Polly for Wins

This is the code to get Amazon AWS Polly working on the Raspberry PI.  The idea is to have an interface to allow someone to type a sentence and then have a Raspberry PI voice out the sentence using the AWS Polly API service.
I'm using a Raspberry PI 3 Model B for the record.  Really fast for 2018 and the credit card sized computer - let's all laugh at this in 2038 :)  !

I followed these instructions (also attached in case the web site 404s)
Commands	Description	
sudo apt-get install python3-pip		
sudo apt-get install python-pip	Install pip (if you don't already have it)	
sudo pip install -v awscli -i https://pypi.python.org/simple/	Install the AWS Cli tools required to communicate with AWS	
sudo aws configure
sudo pip install -v boto3 -i https://pypi.python.org/simple/	a Python package to interact with AWS	
sudo apt-get install python-dev	To get pyaudio in the next step to install	
sudo apt-get update && sudo apt-get upgrade		
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg libav-tools		
sudo pip install -v pyaudio -i https://pypi.python.org/simple/	In order to play sound from Python	
