from huggingsound import SpeechRecognitionModel

modelo = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-spanish") # Cargar el modelo de speech to text
audio = "Audios/edad.wav"
texto = modelo.transcribe([audio])
m=texto[0]
print(m['transcription'])

