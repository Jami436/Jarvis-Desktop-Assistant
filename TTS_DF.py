import asyncio
import edge_tts
import pygame
import os

# Initialize mixer once at the start
pygame.mixer.init()

async def speak(text):
    output_file = "speech.mp3"
    voice = "en-IE-EmilyNeural"  # You can change this to any available voice
    
    try:
        # 1. Generate the TTS file
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)

        # 2. Play the audio
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()

        # 3. Wait for playback to finish
        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.01) # Sleep briefly to avoid busy-waiting
        
        # 4. Unload and delete
        pygame.mixer.music.unload() 
        os.remove(output_file)

    except Exception as e:
        print(f"Jarvis TTS Error: {e}")

# Example Usage
if __name__ == "__main__":
    msg1 = "Hello sir, Jarvis is online."
    msg2 = "How can I help you today?"
    msg3 = "Should I make you a cup of coffee?"
    asyncio.run(speak(msg1))
    asyncio.run(speak(msg2))
    asyncio.run(speak(msg3))