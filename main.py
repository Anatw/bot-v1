# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Welcome to bot. You just said:")
    audio_data = r.record(source, duration=5)
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(type(text))
    if text == "hi bot":
        print(text)

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

