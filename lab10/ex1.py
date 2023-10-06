import json
import os
import pyttsx3
import pyaudio
import vosk
import requests
from PIL import Image
from io import BytesIO
from dog_breeds import dogbr

current_image = None
url = None

tts = pyttsx3.init('sapi5')

voices = tts.getProperty('voices')
tts.setProperty('voices', 'en')

for voice in voices:
    print(voice.name)
    if voice.name == 'Microsoft Irina Desktop - Russian':
        tts.setProperty('voice', voice.id)

pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=16000,
                 input=True,
                 frames_per_buffer=8000)
stream.start_stream()

model = vosk.Model('model_small')
recognizer = vosk.KaldiRecognizer(model, 16000)


def speak(say):
    tts.say(say)
    tts.runAndWait()


def get_breed(url):
    print(url)
    parts = url.split("/")
    if len(parts) >= 2:
        return parts[-2]
    else:
        return None


def recognize_audio():
    data = stream.read(4000, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data) and len(data) > 0:
        result = json.loads(recognizer.Result())
        if 'text' in result:
            return result['text'].lower()
    return None


def execute_command(command):
    global current_image
    global url

    if "показать" in command:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        image_url = response.json()['message']
        speak("Показываю изображение")
        print(f"Показываю изображение: {image_url}")

        image_data = requests.get(image_url).content
        url = image_url
        current_image = Image.open(BytesIO(image_data))
        current_image.show()

    elif "сохранить" in command:
        if current_image is not None:
            if len(url.split("/")) > 0:
                fname = url.split("/")[-1]
            else:
                fname = "dog_image.jpg"
            current_image.save("dogs/" + fname)
            speak("Изображение сохранено в папку dogs как " + fname)
            print("Изображение сохранено в папку dogs как " + fname)
        else:
            speak("Откройте изображение с помощью команды 'показать' перед сохранением.")
            print("Откройте изображение с помощью команды 'показать' перед сохранением.")

    elif "следующее" in command or "следующая" in command or "далее" in command:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        image_url = response.json()['message']
        speak("Показываю следующее изображение")
        print(f"Обновляю изображение: {image_url}")

        image_data = requests.get(image_url).content
        url = image_url
        current_image = Image.open(BytesIO(image_data))
        current_image.show()

    elif "назвать породу" in command or "назвать пород" in command or "порода" in command \
            or "назвать породы" in command or "породы" in command:
        response = requests.get("https://dog.ceo/api/breeds/list/allhttps://dog.ceo/api/breeds/list/all")
        if current_image:
            breed = get_breed(url)
            if breed in dogbr:
                breed = dogbr[breed]
                speak("Порода собаки" + breed)
                print(f"Порода собаки:" + breed)
            elif breed.split("-")[0] in dogbr:
                breed = dogbr[breed.split("-")[0]]
                speak("Порода собаки" + breed)
                print(f"Порода собаки:" + breed)
            else:
                speak("Порода собаки не была переведена с английского")
                print(f"Порода собаки:" + breed)
        else:
            print("Откройте изображение с помощью команды 'показать' перед определением породы.")
            speak("Откройте изображение с помощью команды 'показать' перед определением породы.")

    elif "разрешение" in command or "разрешения" in command:
        if current_image is not None:
            width, height = current_image.size
            speak(f"Разрешение текущего изображения: {width} на {height}")
            print(f"Разрешение текущего изображения: {width} на {height}")
        else:
            print("Откройте изображение с помощью команды 'показать' перед определением разрешения.")
            speak("Откройте изображение с помощью команды 'показать' перед определением разрешения.")

    else:
        print("Не распознана команда.")


try:
    while True:
        command = recognize_audio()
        if command:
            print(f"Вы сказали: {command}")
            execute_command(command)
except KeyboardInterrupt:
    print("Программа завершена.")
finally:
    stream.stop_stream()
    stream.close()
    pa.terminate()
