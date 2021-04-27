import speech_recognition as sr 
listener = sr.Recognizer()

try:
    with sr.Microphone() as soure:
        print("escuchando...")
        voice = listener.listen(soure)
        rec = listener.recognize_google(voice, language='es-ES')
        print(rec)
        #comprobando las situacion del repocitorio
        #modificando las modificaciones

except:
    pass