from gtts import gTTS

text = "Bu bir test konuşması."

tts = gTTS(text, lang="en")
tts.play()