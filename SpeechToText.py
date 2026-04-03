# pip install SpeechRecognition==3.8.1
import speech_recognition as sr

import os
import threading

#pip install mtranslate
from mtranslate import translate

#pip install colorama
from colorama import Fore, Style, init

init(autoreset=True)

def print_loop():
    while True:
        print (Fore.BLUE + "Listening...", end ="", flush=True)
        print(Style.RESET_ALL, end="", flush=True)

def Translate_Urdu_to_English(text):
    English_text = translate(text, "en-us")
    return English_text

def Speech_to_Text_Python():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 2.0
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 1.0
    recognizer.non_speaking_duration = 0.5

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:   
            print (Fore.BLUE + "Listening...", end = "", flush=True)
            try:
                audio = recognizer.listen(source, timeout = None)
                print("/r" + Fore.CYAN + "Processing...", end="", flush=True)
                recognize_text = recognizer.recognize_google(audio).lower()
                if recognize_text:
                    Trans_text = Translate_Urdu_to_English(recognize_text)
                    print("/r" + Fore.CYAN + "You said:" + Trans_text)
                    return Trans_text
                else:
                    return ""
            except sr.UnknownValueError:
                recognize_text = ""
            finally:
                print("/r", end = "", flush=True)

            os.system("cls" if os.name == "nt" else "clear")

        Stt_thread = threading.Thread(target=Speech_to_Text_Python)
        print_thread = threading.Thread(target=print_loop)
        Stt_thread.start()
        print_loop.start()
        Stt_thread.join()
        Stt_loop.join()

Speech_to_Text_Python()
        