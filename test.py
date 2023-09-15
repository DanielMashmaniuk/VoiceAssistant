import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Ініціалізація розпізнавача
recognizer = sr.Recognizer()

# Ініціалізація синтезатора мовлення
engine = pyttsx3.init()

# Функція для розпізнавання голосу та виконання команд
def recognize_command():
    with sr.Microphone() as source:
        print("Скажіть команду:")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("Ви сказали: " + command)
        return command
    except sr.UnknownValueError:
        print("Розпізнавання не вдалося")
        return ""
    except sr.RequestError as e:
        print("Помилка при зверненні до служби розпізнавання: {0}".format(e))
        return ""

# Функція для відтворення тексту голосом
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Функція для виконання арифметичних операцій
def calculate(command):
    try:
        # Розділити команду на операнди та операцію
        parts = command.split()
        operand1 = float(parts[0])
        operator = parts[1]
        operand2 = float(parts[2])

        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2
        elif operator == "/":
            result = operand1 / operand2
        else:
            return "Невідома операція"

        return f"Результат: {result}"
    except Exception as e:
        return "Помилка обчислення: " + str(e)

# Функція для перекладу тексту
def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Основний цикл для слухання команд
while True:
    command = recognize_command()

    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "what is your name" in command:
        speak("I am your virtual assistant.")
    elif "calculate" in command:
        result = calculate(command.replace("calculate", "").strip())
        speak(result)
    elif "translate" in command:
        speak("What would you like to translate?")
        text_to_translate = recognize_command()
        speak("To which language would you like to translate it?")
        target_language = recognize_command()
        translated_text = translate_text(text_to_translate, target_language)
        speak(f"Translation: {translated_text}")
    elif "exit" in command:
        speak("Goodbye!")
        break
    else:
        speak("I'm sorry, I didn't understand that command.")
