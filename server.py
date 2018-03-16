from polly import Polly
from subprocess import call

import socket
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():

    return render_template('form.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    message=request.form['say']
    tts = Polly('Matthew')
    tts.saveToFile(message, 'polly.mp3')
    call(["omxplayer", "polly.mp3"])

    return render_template('greeting.html', say=request.form['say'], to=request.form['sale'])
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
