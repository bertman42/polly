from polly import Polly
from subprocess import call
import time

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
#    tts.say('Klocwork ')
    tts.saveToFile(message, 'polly.wav')
    call(["amixer", "cset numid=3 1"])
    call(["mplayer", "polly.wav"])
    time.sleep(1)

    return render_template('greeting.html', say=request.form['say'])
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
