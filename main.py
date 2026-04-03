import asyncio
import os
import json
import webbrowser
import winshell
import time
import screen_brightness_control as sbc
from datetime import datetime

# Import your custom modules
from jami_speech_rec import Listener
import TTS_DF as JarvisVoice

# 1. DYNAMIC MEMORY SYSTEM
MEMORY_FILE = "memory.json"

def load_memory():
    default_data = {"user_name": "Sir", "bot_name": "Jarvis"}
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        except:
            return default_data
    return default_data

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

memory = load_memory()

# 2. HARDWARE & SYSTEM FUNCTIONS
def set_brightness(level):
    try:
        sbc.set_brightness(level)
        return f"Brightness adjusted to {level} percent."
    except:
        return "I could not access the display settings."

def empty_recycle_bin():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        return "Recycle bin has been emptied, sir."
    except:
        return "The recycle bin is already empty."

# 3. THE COMMAND BRAIN
async def process_command(text):
    query = text.lower()
    
    # Identity & Memory
    if "my name is" in query:
        name = query.split("is")[-1].strip()
        memory["user_name"] = name
        save_memory(memory)
        await JarvisVoice.speak(f"Updated. I will remember you as {name}.")

    elif "who am i" in query:
        await JarvisVoice.speak(f"You are {memory['user_name']}, the developer of this system.")

    # Hardware
    elif "brightness" in query:
        level = "".join(filter(str.isdigit, query)) or "70"
        await JarvisVoice.speak(set_brightness(level))

    # System Utilities
    elif "open recycle bin" in query:
        os.startfile("shell:RecycleBinFolder")
        await JarvisVoice.speak("Opening the folder now.")

    elif "empty recycle bin" in query:
        await JarvisVoice.speak(empty_recycle_bin())

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        await JarvisVoice.speak("Opening YouTube.")

    elif "open github" in query:
        webbrowser.open("https://www.github.com")
        await JarvisVoice.speak("Opening Github.")


    elif "time" in query:
        current_time = datetime.now().strftime('%I:%M %p')
        await JarvisVoice.speak(f"The current time is {current_time}.")

    # Exit
    elif "stop" in query or "exit" in query:
        await JarvisVoice.speak("Powering down. Goodbye, sir.")
        return False
    
    return True

async def main_loop():
    user = memory.get("user_name", "Sir")
    await JarvisVoice.speak(f"Core systems initialized. Welcome back, {user}.")
    
    try:
        # Listening loop from your jami-speech package
        for text in Listener.listen():
            if text:
                print(f"User: {text}")
                if not await process_command(text):
                    break
    except Exception as e:
        print(f"System Error: {e}")

if __name__ == "__main__":
    asyncio.run(main_loop())