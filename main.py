#https://www.youtube.com/watch?v=AWvsXxDtEkU <--this code is from this video
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices') #get all type of voices
engine.setProperty('voice', voices[1].id) #female alexa voice in in number 2(index 1)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening . . .")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '') #removing alexa from command
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("current time is " + time)
    elif 'definition' in command:
        question = command.replace("what is the definition of ", '')
        info = wikipedia.summary(question, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        the_joke = pyjokes.get_joke()
        talk(the_joke)
        print(the_joke)
    else:
        talk("please repet your command")

while True:
    run_alexa()

