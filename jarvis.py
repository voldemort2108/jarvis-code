import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import pywhatkit
import datetime
import smtplib #for emails
import pyjokes
from datetime import date
import random 
import PyPDF2
from datetime import date
import calendar
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import requests
from requests import get
import subprocess
from playsound import playsound
from googlesearch import search
from selenium import webdriver
import wolframalpha
from tkinter import *
from tkinter.ttk import *
from time import strftime
import datetime
import winsound
import sys
import cv2
import pywhatkit as kit
import pyautogui
from subprocess import call
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from frontui import Ui_obj
import cv2
from ecapture import ecapture as ec






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 175) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour <= 12:
        print("Good morning Sir")
        speak("Good morning Sir")
    elif hour >=12 and hour <=18:
        print("Good Afternoon Sir")
        speak("Good Afternoon Sir")
    else :
        print("Good Evening Sir")
        speak("Good Evening Sir")
    print("I am your assistant Jarvis , How may I help you?")
    speak("I am your assistant Jarvis , How may I help you?")





def note(audio):
    date = datetime.datetime.now()
    file_name = str(date).replace(':' , '-') + '-note.txt'
    with open (file_name , 'w') as f:
        f.write(audio)
    subprocess.Popen(["notepad.exe" , file_name])




def alarm(text):
    dTimeA= datefinder.find_dates(text)
    print(dTimeA)





class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()



    def sendEmail(to,content):

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('sender email','semder email password')
        server.sendmail('receiver email',person,content)
        server.close()



    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)
        try :
            print("Recognizing...")
            self.query = r.recognize_google(audio,language='en-in')  #,language='en-in'
            print(f"Your command:{self.query}\n")
        except Exception as e :
            print ("Say that again please...")
            return ""
        return self.query




    def TaskExecution(self):
    
        print("Initializing Jarvis...")
        wishMe()
        while True :
            self.query = self.takeCommand().lower()
        

            if 'wikipedia' in self.query  :
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia","")
                self.query = self.query.replace("according to wikipedia","")
                results = wikipedia.summary(self.query,sentences=2)
                print(results)
                speak("According to wikipedia")
                speak(results)


            elif "mute" in self.query :
                pyautogui.press("volumemute")
                

            elif "unmute" in self.query :
                pyautogui.press("volumemute")
            

            elif "pause" in self.query:
                pyautogui.press("playpause")


            elif "start" in self.query:
                pyautogui.press("playpause")  


            elif 'old are you' in self.query :
                current_day = datetime.datetime.now()
                build_day = datetime.datetime(2021, 2, 8)
                diff = current_day - build_day
                speak('I am' + str(diff.days)+'days old')



            elif 'open youtube' in self.query :
                webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("youtube.com")


            elif 'open chrome' in self.query :
                webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("google.com")


            elif 'open google' in self.query :
                webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("google.com")


            elif 'open wikipedia' in self.query :
                webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("wikipedia.com")


            elif 'play ' in self.query:
                song = self.query.replace('play','')
                speak ('ok playing')
                pywhatkit.playonyt(song)


            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                speak (f"Sir , the time is {strTime}")


            elif 'code' in self.query :
                codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)


        


            elif 'send an email' in self.query :
                
                dict1 = {ids in which you have to send emails}
                try :
                    speak("whom do you want to send")
                    self.query = self.takeCommand().lower()
                    for j in dict1.keys():
                        if self.query == j :
                            person = dict1[j]
                    speak("What should I say?")
                    content = self.takeCommand()
                    sendEmail(person,content)
                    speak("Email has been sent!")
                except Exception as e :
                    print (e)
                    speak("Sorry sir but the e-mail was not sent ")
                
                
            elif 'joke' in self.query :
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)



            elif 'are you' in self.query:
                reply1 = 'I am very good and hope same for you' 
                print(reply1) 
                speak(reply1) 



            elif 'were you made' in self.query :
                reply2 = "I was created by Mr. Abhinav on 8th of feb midnight"
                print(reply2) 
                speak(reply2)



            elif "go die" in self.query :
                reply3 = "I'm sorry i can't do that ......I can't leave you like this"
                print(reply3) 
                speak(reply3)



            elif "mar jao" in self.query :
                reply3 = "I'm sorry i can't do that ......I can't leave you like this"
                print(reply3) 
                speak(reply3)



            elif "score" in self.query :
                reply4 = "Sure see this"
                speak(reply4)
                webbrowser.open("https://www.cricbuzz.com/cricket-match/live-scores")



            elif 'about yourself' in self.query:
                reply5 = "I am your personal assistant . and i can do anything for you like play music or send email or whatsapp anyone"
                print(reply5) 
                speak(reply5)




            elif "creator" in self.query :
                reply6 = "Abhinav is my creator , he is soon going to be an aerospace engineer , he lives in lucknow. Abhinav loves coding."
                print(reply6) 
                speak(reply6)



            elif 'who is' in self.query :
                person = self.query.replace('who is ','')
                info = wikipedia.summary(person,2)
                print(info)
                speak(info)



            elif 'what is' in self.query :
                person = self.query.replace('what is ','')
                info = wikipedia.summary(person,2)
                print(info)
                speak(info)



            elif 'tell me about' in self.query :
                person2 = self.query.replace('tell me about', '')
                info = wikipedia.summary(person2,10)
                print(info)
                speak(info)
            
            
            elif 'game' in self.query :
                speak('OK starting the guess game')
                speak('Guess a number between 1 to 10')
                a = None
                b = random.randint(1,10)
                guess = 0
                while (a!=b):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Listening...")
                        r.pause_threshold = 1
                        audio = r.listen(source)
                    try :
                        print("Recognizing...")
                        a = r.recognize_google(audio)
                        print(f"user said: {a}\n")
                        a = int(a)
                    except Exception as e :
                        # print (e) 
                        print ("Say that again please...")                    
                        if (a < b) :
                            speak('lesser, try again')
                            guess = guess + 1
                        elif (a > b) :
                            speak('greater, try again')
                            guess = guess + 1
                        elif (a == b) :
                            speak('Gotcha !! you got it in')
                            speak(str(guess))
                            speak('times')

            elif 'bye bye' in self.query:
                speak("Initiating shutting command.....Good-bye sir")
                exit()

            elif "camera" in self.query or "take a photo" in self.query:
                ec.capture(0, "jarvis camera","img.jpg")     


            elif 'date' in self.query: 
                today = date.today()
                print(today)
                speak(today)



            elif 'day' in self.query :
                today = date.today()
                d1 = today.strftime("%d/%m/%Y")
                day, month, year = (int(x) for x in d1.split('/'))    
                ans = datetime.date(year, month, day)
                print (ans.strftime("%A"))
                speak(ans.strftime("%A"))



            elif 'news' in self.query:
                url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=3103661539ec4deca15cd122cd5381ad')
                response = requests.get(url)
                text = response.text
                my_json = json.loads(text)
                for i in range(0, 5):
                    print((i+1),'.',my_json['articles'][i]['title'])
                    speak(my_json['articles'][i]['title'])





            elif 'instagram' in self.query :
                webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("instagram.com")





            elif 'pagal' in self.query :
                speak ('who speaks is the one who is')





            elif 'temperature' in self.query :
                speak("Which city sir")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source) 
                    try:
                        print("Recognizing...")
                        place = r.recognize_google(audio , language= 'en-in')
                        print(f"user said: {place}\n")   
                    except Exception as e:
                        print('Say that again please')
                        place = none 
                    search = f"Weather in {place}"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    soup = BeautifulSoup(r.text , "html.parser")
                    update = soup.find("div" , class_="BNeawe").text
                    print(f"{search} now is {update}")
                    speak(f"{search} now is {update}")




            elif 'mails' in self.query :
                webbrowser.open('https://mail.google.com/')     



            



            elif 'note' in self.query:
                speak("What would you like me to write down?")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                    try:
                        print("Recognizing...")
                        self.query = r.recognize_google(audio , language= 'en-in')
                        print(f"user said: {self.query}\n")
                    except Exception as e:
                        print('Say that again please')
                        self.query = none
                    note(self.query)
                    print("I've made a note of that")





            elif 'remember' in self.query:
                speak("What would you like me to remember?")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                    try:
                        print("Recognizing...")
                        self.query = r.recognize_google(audio , language= 'en-in')
                        print(f"user said: {self.query}\n")
                    except Exception as e:
                        print('Say that again please')
                        self.query = none
                        note(self.query)
                        print("I've stored your messege")



            elif 'blackboard' in self.query:
                reply5 = "Opening blackboard"
                speak(reply5)
                webbrowser.open("https://learn.upes.ac.in//webapps//portal//execute//tabs//tabAction?tab_tab_group_id=_141_1") 




            elif 'sing a song' in self.query:
                speak("although i am having a sour throat stil i can try ")
                playsound('C:\\Users\\user\\OneDrive\\Documents\\jarvis song.mp3')





            elif 'thank you' in self.query :
                speak("Pleasure sir , it's my duty to make you happy")


            elif 'open whatsapp' in self.query :
                speak("opening")
                codePath = "C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(codePath)




            elif 'send message' in self.query :
                d = dict(name1=phone number,name2=phone number2)
                try :
                    speak("whom do you want to send")
                    receiver_name = self.takeCommand().lower()
                    receiver_name= receiver_name.lower()
                    for j in d.keys():
                        if receiver_name == j :
                            receiver_number = str(d.get(receiver_name))
                            receiver_number = "+91" + receiver_number 
                            print(receiver_number)
                    speak("What should I say?")
                    content = self.takeCommand()
                    speak("What time you want to send the messege")
                    msg_time = str(self.takeCommand().lower())
                    msg_time = msg_time.replace(' ','')
                    hour = int(msg_time[:2])
                    minute = int(msg_time[2:])
                    content[0].upper()
                    kit.sendwhatmsg(receiver_number,content,hour,minute)
                    speak("Message has been sent")
                except Exception as e :
                    print (e)
                    speak("Sorry sir but the messege was not sent ")


                


                
            
            elif 'jarvis' in self.query:
                client = wolframalpha.Client('6RLLXQ-UK69UXVU2T')
                try:
                    print("Yes sir what can i do for you")
                    speak("Yes sir what can i do for you")
                    question = self.takeCommand()
                    query = str(question)
                    
                    res = client.query(query)
                    print(next(res.results).text)
                    speak(f"The answer is {next(res.results).text}")
                except:
                    print("I dont know that but i am improving")
                    speak("Sorry , i dont know that but i am improving")
                


            elif 'alarm' in self.query  :
                nn == int(datetime.datetime.now().hour)
                if nn == 1:
                    music_dir = "C:\\Users\\user\\Documents\\my_assitant.py\\alarm_beeps.mp3"
                    songs = os.listendr(music_dir)
                    os.startfile(os.path.join(music_dir,songs[0]))



            elif "shutdown the system" in self.query :
                pyautogui.confirm('Shall I proceed?')
                speak('ok shutting down')
                os.system("shutdown /s /t 5")

            elif "new tab" in self.query:
                pyautogui.hotkey("ctrl","t")
                


            elif "restart the system" in self.query :
                os.system("shutdown /r /t 5")


            elif "go to sleep" in self.query :
                os.system("rundll123.exe powrprof.dll,SetSuspendState 0,1,0")


            elif 'switch the window' in self.query :
                speak("Switching...")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.press("alt")


            elif 'start menu' in self.query :
                pyautogui.click(0,1079)


            elif 'blinking mouse' in self.query :
                j=0
                while j < 100 :
                    pyautogui.click(500,540)
                    pyautogui.click(1500,540)
                    j = j + 1



            
        

            elif "screenshot" in self.query :
                pyautogui.keyDown("start")
                pyautogui.keyDown("prtsc")


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_obj()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)


    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Pictures/sFaoXq3.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Pictures/images.png")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Pictures/images.png")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Pictures/9c046e14e6ca7754d21dcd5c0deceea6.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Pictures/gauge_001.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()

        
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        


    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())











           
       
    
    
            
                    
           

        
        

        
        
        

       
        


            



        




        


