import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Welcome to bot. You just said:")
    audio_data = r.record(source, duration=5)
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(type(text))
    # listen until you heat "hi bot", than listen for X seconds, and print the command given. Wait for ? seconds if a
    # you identify a break in the speech flow.
    if text == "hi bot":
        print(text)
