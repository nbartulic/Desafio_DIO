import pyttsx3

def initialize_tts():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Configurar voz feminina (ajuste conforme necessário)
    for voice in voices:
        if "brazil" in voice.name.lower() or "portuguese" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.setProperty('rate', 180)  
    engine.setProperty('volume', 1.0)  
    return engine

def speak(text):
    if not text.strip():
        print("Texto vazio, nada a ser falado.")
        return

    engine = initialize_tts()
    print(f"Assistente: {text}")  
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Olá, eu sou seu assistente virtual. Como posso ajudar?")
