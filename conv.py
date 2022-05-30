from gtts import gTTS

# If you don't have gtts run the next command in your terminal "pip install gtts"
import os

# Reading the files
f = open("test.txt", "r")
x = f.read()

# Specifying language:
language = 'en'  # You can specify any language. Reffer to the gtts documentation
# simply write this down for better sound
audio = gTTS(text=x, lang=language, slow=False)

# Now save the audio file
# You can save by any name you wish
audio.save("3.wav")
os.system("3.wav")
