import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

name = 'teresa'

listener = sr.Recognizer()

engine  = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#for voice in voices:
 #   print(voice)

def talk(text):
    engine.say(text)
    engine.runAndWait()


engine.say("buenos dias")
engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as soure:
            print("escuchando...")
            voice = listener.listen(soure)
            rec = listener.recognize_google(voice, language='es-ES')
            rec =rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)

    except:
        pass
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo' + music)
        pywhatkit.playonyt(music)

    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("son las" + hora)

    elif 'busca' in rec:
        order = rec.replace('busca', '')
        info = wikipedia.summary(order, 1)
        talk(info)
        
    elif 'mayor' in rec:
        repuesta = rec.replace('mayor', '')
        talk(repuesta)
        
        for i  in range(1):
            n1 = int(input("digite el primere numero"))
            n2= int(input ("digite el segundo numero"))
            if n1 > n2 :
                mayor=(n1,"es mayor que",n2)
                talk(mayor)
            elif n2 > n1:
                mayor=(n2, "es mayor que", n1)
                talk(mayor)
            else:
                mayor=(n1, "es igual a", n2)
                talk(mayor)
                
    elif 'chiste' in rec:
        My_joke = pyjokes.get_joke(language="es", category="all")

        talk(My_joke)
        
    else:
        talk("vuelve a intentarlo")
while True:
    run() 