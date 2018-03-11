from polly import Polly

tts = Polly('Matthew')
#tts.say('Hello you sexy thing.  Thanks for the massage!')
tts.saveToFile('Hello you sexy thing.  Thanks for the massage,, ', 'polly.mp3')

