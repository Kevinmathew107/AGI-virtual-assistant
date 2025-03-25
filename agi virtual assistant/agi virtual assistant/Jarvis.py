from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Started The Jarvis : Wait For Few Seconds More")
from Main import MainTaskExecution


def MainExecution():    
    Speak("Hello Sir")
    Speak("I'm Jarvis, I'm Ready To Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")        
        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True: 
            pass

        elif len(Data)<3:
            pass

        elif "google search" in Data :
            pass
        
        elif "youtube search" in Data :
            pass

        elif "whatsapp message" in Data:
            pass

        elif "whatsapp voice" in Data :
            pass

        elif "whatsapp video" in Data:
            pass

        elif "show whatsapp" in Data:
            pass

        elif "set alarm" in Data:
            pass

        elif "youtube download " in Data:
            pass

        elif "google chrome" in Data:
            pass

        elif "turn on the tv" in Data :
            Speak("Ok..Turning On The Android Tv")

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
          
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!! >>")
        print("")
        MainExecution()
    else:
        pass

ClapDetect()




