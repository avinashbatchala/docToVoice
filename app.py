from gtts import gTTS

import os
tts = gTTS(text='If you use Microsoft Windows 10, it has a speech engine included. Install the module win32com, then you can use this code:', lang='en')
tts.save("mp3Files/sample.mp3")
os.system("mpg321 good.mp3")
