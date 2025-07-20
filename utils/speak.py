import pyttsx3
import threading

engine = pyttsx3.init()
is_speaking = False

def _speak(text):
    global is_speaking
    is_speaking = True
    engine.say(text)
    engine.runAndWait()
    is_speaking = False

def speak(text):
    threading.Thread(target=_speak, args=(text,), daemon=True).start()

def stop_speaking():
    global is_speaking
    if is_speaking:
        engine.stop()
        is_speaking = False
