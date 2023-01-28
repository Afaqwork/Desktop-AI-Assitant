import os
import sys
from click import BaseCommand
from gtts import gTTS  # pip install gTTS
import requests
import speech_recognition as sr  # pip install speechRecognition
import datetime
import cv2  # pip install opencv-python
import random
from requests import get
import wikipedia  # pip install wikipedia
import webbrowser  # pip install web browser
import smtplib  # pip install smtplib
import pyjokes  # pip install pyjokes
import pyautogui  # pip install pyautogui
import psutil  # pip install psutil
import PyPDF2  # pip install PyPDF2
from pywikihow import search_wikihow  # pip install pywikihow

import audioplayer  # pip install audioplayer
import wolframalpha  # pip install wolframalpha
# from neuralintents import GenericAssistant
from quote import quote
import ctypes 

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
# from DesktopAI import speak
from Jarvius import Ui_DesktopAI
# from state import state
from pywikihow import search_wikihow
import speedtest
from pytube import YouTube
import qrcode

def speak(audio):
    """Google text-to-speech function"""
    tts = gTTS(audio)
    tts.save("friday.mp3")
    audioplayer.AudioPlayer("friday.mp3").play(block=True)


def wish():
    """Wish with respective datetime"""
    hour = int(datetime.datetime.now().hour)

    if 8 <= hour < 12:
        speak("good morning")
    elif 13 <= hour < 16:
        speak("good afternoon")
    else:
        speak("good evening")
    # speak("i am Desktop AI sir. please tell me how can i help you")
    

class MainThread(QThread):  # main
    """Main class"""

    def __init__(self, parent=None):
        """self.query field"""
        super().__init__(parent)
        self.query = None
        

    def run(self):
        """Running thread"""
        self.main()

    @staticmethod
    def voicecom():  # speech-to-text
        """Recognize"""
        r = sr.Recognizer()  
        with sr.Microphone() as source:  
            print("Please wait. Calibrating microphone...")  
            # listen for 2 seconds and create the ambient noise energy level  
            r.adjust_for_ambient_noise(source, duration=2)  
            print("Say something!")  
            audio = r.listen(source)  
        
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            # speak({query})
            cmd=r.recognize_google(audio)

        except Exception as e:
            print(e)    
            print("Say that again please...")  
            return "None"
        return query
  
    def main(self):  # main task execution
        """The original task"""
        wish()
        while True:
        # self.query = self.voicecom().lower() 
            self.query = self.voicecom().lower()

            #Logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in self.query:
                   speak('Opening youtube')
                   webbrowser.open("https://www.youtube.com/")
            elif ' play music' in self.query:
                try:
                    music_dir = 'E:\\music' #change the song path directory if you have songs in other directory
                    songs = os.listdir(music_dir)
                    for song in songs:
                        if song.endswith('.mp3'):
                            os.startfile(os.path.join(music_dir, song))
                except:
                    speak("Boss an unexpected error occured")
            elif "volume mute" in self.query:
                speak(' muteing volume')
                pyautogui.press("volumemute")
            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                speak(f"your IP address is {ip}")
            elif 'sleep' in self.query:  # for turning pc into sleep
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif 'lock window' in self.query: #for locking pc
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()
                    
            elif 'Close chrome' :
                def close_app(app_name):
                    running_apps=psutil.process_iter(['pid','name']) #returns names of running processes
                    found=False
                    for app in running_apps:
                            sys_app=app.info.get('name').split('.')[0].lower()

                            if sys_app in app_name.split() or app_name in sys_app:
                                pid=app.info.get('pid') #returns PID of the given app if found running
                                
                                try: #deleting the app if asked app is running.(It raises error for some windows apps)
                                    app_pid = psutil.Process(pid)
                                    app_pid.terminate()
                                    found=True
                                except: pass
                                
                            else: pass
                    if not found:
                            print(app_name+" not found running")
                    else:
                            print(app_name+'('+sys_app+')'+' closed')

                close_app('chrome')

            # assistant.request(self.query)


startExecution = MainThread()


class Main(QMainWindow):
    
    """Program gui thread"""

    
    def __init__(self):
        super().__init__()
        self.ui = Ui_DesktopAI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)
    
    #NOTE make sure to place a correct path where you are keeping this gifs
    def startTask(self):
       
        timer = QTimer(self)
        # timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()   


# the UI
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

