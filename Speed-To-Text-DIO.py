import speech_recognition as sr

def initialize_recognizer():
    """ Inicializa o reconhecedor de fala com parâmetros ajustados para melhor desempenho. """
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300  # Ajustar sensibilidade ao ruído ambiente
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1.0  # Tempo máximo de pausa antes de terminar a fala
    return recognizer

def listen():
    """ Captura e converte fala em texto com tratamento de erros e feedback. """
    recognizer = initialize_recognizer()
    with sr.Microphone() as source:
        print("Ajustando ruído de fundo, por favor aguarde...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Fale agora...")

        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="pt-BR")
            print("Você disse: " + text)
            return text.lower()
        except sr.UnknownValueError:
            print("Não entendi o que foi dito. Tente novamente.")
            return ""
        except sr.RequestError:
            print("Erro ao conectar com o serviço de reconhecimento. Verifique sua conexão.")
            return ""
        except sr.WaitTimeoutError:
            print("Nenhuma fala detectada no tempo limite. Tente novamente.")
            return ""

if __name__ == "__main__":
    resultado = listen()
    if resultado:
        print(f"Texto reconhecido: {resultado}")
