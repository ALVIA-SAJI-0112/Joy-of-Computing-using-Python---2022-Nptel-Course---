import speech_recognition as sr
AUDIO_FILE=("speechtotext.wav")
#use audio file as source

r=sr.Recognizer() #initialise the recogniser

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
#reads the audio file

#when google unable to recognise audio file(except 1st one)
#when google unable to get audio file(except 2nd one)
try:
    print("audio file contains " + r.recognize_google(audio))
except sr.UnknownValueError :  
    print("Google Speech Recognition could not understand audio")
except sr.RequestError:
    print("Couldn't get the results from Google Speech Recognition")