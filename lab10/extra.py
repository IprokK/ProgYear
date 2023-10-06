import json
import os
import pyttsx3
import pyaudio
import vosk
import requests
from PIL import Image
from io import BytesIO
from dog_breeds import dogbr

current_phrase = None


tts = pyttsx3.init('sapi5')

voices = tts.getProperty('voices')
tts.setProperty('voices', 'en')

for voice in voices:
    print(voice.name)
    if voice.name == 'Microsoft David Desktop - English (United States)':
        tts.setProperty('voice', voice.id)

pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=16000,
                 input=True,
                 frames_per_buffer=8000)
stream.start_stream()

model = vosk.Model('model_small_en')
recognizer = vosk.KaldiRecognizer(model, 16000)


def speak(say):
    tts.say(say)
    tts.runAndWait()

def recognize_audio():
    data = stream.read(4000, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data) and len(data) > 0:
        result = json.loads(recognizer.Result())
        if 'text' in result:
            return result['text'].lower()
    return None


def execute_command(command):
    global current_phrase


    word_to_find = command.split(" ")[-1]
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word_to_find}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        if "meaning" in command:
            meanings = data[0]['meanings']
            if meanings:
                first_meaning = meanings[0]['definitions'][0]['definition']
                speak(f"The meaning of {word_to_find} is: {first_meaning}")
                print(f"The meaning of {word_to_find} is: {first_meaning}")
            else:
                speak(f"No meanings found for {word_to_find}")
                print(f"No meanings found for {word_to_find}")


        elif "example" in command:
            examples = data[0]['meanings'][0]['definitions'][0].get('examples', [])
            ii = 0
            for m in range(len(data[0]['meanings'])):
                if ii < 1:
                    for i in range(len(data[0]['meanings'][m]['definitions'])):
                        if 'example' in data[0]['meanings'][m]['definitions'][i]:
                            examples = data[0]['meanings'][m]['definitions'][i]['example']
                            if examples and ii < 1:
                                ii+=1
                                first_example = examples
                                speak(f"An example of {word_to_find} is: {first_example}")
                                print(f"An example of {word_to_find} is: {first_example}")
                else:
                    continue
            if ii ==0:
                speak(f"No examples found for {word_to_find}")
                print(f"No examples found for {word_to_find}")

        elif "link" in command:
            speak(f"Opening browser for {word_to_find}")
            print(f"Opening browser for {word_to_find}")
            os.system(f"start https://www.dictionary.com/browse/{word_to_find}")

        elif "save" in command:
            speak(f"Sorry, saving functionality is not available for dictionary entries.")
            print(f"Sorry, saving functionality is not available for dictionary entries.")

        else:
            speak(f"Unknown command for {word_to_find}")
            print(f"Unknown command for {word_to_find}")

    else:
        speak(f"Error fetching information for {word_to_find}")
        print(f"Error fetching information for {word_to_find}")

try:
    while True:
        command = recognize_audio()
        if command:
            print(f"You said: {command}")
            execute_command(command)
except KeyboardInterrupt:
    print("Программа завершена.")
finally:
    stream.stop_stream()
    stream.close()
    pa.terminate()
