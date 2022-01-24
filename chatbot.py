import pyttsx3 # text to speech
from decouple import config # for config
from utils import things_text # self defined
import wikipedia as wk # to make wikipedia searches
import requests as rq #to make web get requests
import pywhatkit as pwk #for google search

USERNAME = config("USERNAME")
BOTNAME = config("BOTNAME")

engine = pyttsx3.init()

engine.setProperty("rate", 190)

voice = engine.getProperty("voices")
engine.setProperty("voice", voice[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

def greet():
    speak("hi i am {}".format(BOTNAME)+"choose a number from the list of options")
    for i in things_text:
        print(i) 

def user_in():
    user_input = input()
    return int(user_input)-1

#using the Advice slip api
def advice():
    r = rq.get("https://api.adviceslip.com/advice").json()
    return r["slip"]["advice"]


# using icanhazdadjoke api
def jokes():
    headers = {
        'Accept': 'application/json'
    }
    data = rq.get("https://icanhazdadjoke.com/", headers = headers).json()
    return data["joke"]

#google search using pywhatkit module
def goog():
    speak("Type in what you want to search")
    search = input("Enter: ")
    pwk.search(search)

# searchs a video on youtube
def yout():
    speak("Type in what you want to watch")
    vid = input("Enter: ")
    pwk.playonyt(vid)

# search on wikipedia
def wiki():
    speak("Type in what you want to know")
    ob = input("Enter: ")
    return wk.summary(ob, sentences = 1)

#main function
def jarvis(inp):
    if inp == 0:
        speak(advice())
    if inp == 1:
        speak(jokes())
    if inp == 2:
        goog()
    if inp == 3:
        yout()
    if inp == 4:
        speak(wiki())
    
if __name__ == "__main__":
    greet()
    jarvis(user_in())