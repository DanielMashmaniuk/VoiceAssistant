import pyttsx3  #
import speech_recognition as sr
import datetime
import webbrowser

# Ініціалізація голоса
engine = pyttsx3.init()


# Функція для голосового виводу тексту
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Функція для розпізнавання мови
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слухаю...")
        audio = recognizer.listen(source)
        command = ""
        try:
            command = recognizer.recognize_google(audio, language="uk-UA")
            print("Ви сказали: " + command)
        except sr.UnknownValueError:
            print("Не розпізнано")
        return command


# Основний цикл програми
if __name__ == "__main__":
    while True:
        command = listen().lower()

        if "привіт" in command:
            speak("Привіт! Як я можу вам допомогти?")
        elif "як справи" in command:
            speak("Справи добре, дякую! Як у вас?")
        elif "як тебе звати" in command:
            speak("Мене звуть Джарвіс.")
        elif "що ти вмієш" in command:
            speak("Я можу відкривати веб-сторінки, розповідати про погоду, і виконувати інші завдання.")
        elif "відкрий Google" in command:
            webbrowser.open("https://www.google.com")
        elif "відкрий YouTube" in command:
            webbrowser.open("https://www.youtube.com")
        elif "до побачення" in command:
            speak("До побачення! Маєте гарного дня!")
            break
