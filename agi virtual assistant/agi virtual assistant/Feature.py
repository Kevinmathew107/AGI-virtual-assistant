import pywhatkit
from Body.Speak import Speak
import wikipedia
from pywikihow import WikiHow , search_wikihow
import os
import webbrowser as web
from Body.Listen import MicExecution

def GoogleSearch(term):
    
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")
    writeab = str(query)

    oooooo = open ('C:\\AI Jarvis\\Database\\Data.txt','a')
    oooooo.write(writeab)
    oooooo.close()

    Queryy = str(term)
    pywhatkit.search(Queryy)

    if 'how to' in Queryy:
        max_result = 1 
        how_to_func = search_wikihow(query=Queryy , max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Speak(how_to_func[0].summary)

    else:
        search = wikipedia.summary(Queryy,2)
        Speak(f" : According to Your Search : {search}")

# def GoogleSearch(term):
#     Speak('What should i search for?')
#     search = MicExecution()
#     web.open('https://www.google.com/search?q='+search)


def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")

def Alarm(query):

    TimeHere = open('C:\\AI Jarvis\\Database\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\AI Jarvis\\Automations\\Alarm.py")

def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip 
    from time import sleep

    sleep(2)
    click(x=1208, y=66)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download('C:\\AI Jarvis\\Database\\YouTube Download\\')


    Download(Link)


    Speak("Done Sir , I Have Downloaded The Video .")

    Speak("You Can Go And Check It Out.")


    os.startfile('C:\\AI Jarvis\\Database\\YouTube Download\\')

    
