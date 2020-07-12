#imports

from gtts import gTTS

#the text you want to convert and the language

text = "huso1"
language = "en"

#the settings for the speaker


speech = gTTS(text = text, lang = language, slow = False)

#the file is saved in your project folder

speech.save("text.mp3")