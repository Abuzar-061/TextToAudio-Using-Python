from gtts import gTTS
from pathlib import Path
import playsound

text=''
with open('text.txt') as f:
    for s in f:
        text+=str(s)
    text = text.replace('\n','')
    print(text)

    audio = gTTS(text,slow=False,lang='en')
    audio.save('audio.mp3')

playsound.playsound('audio.mp3') 