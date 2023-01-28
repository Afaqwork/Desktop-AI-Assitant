from ast import main
import cmd
import os
import sys
import time 
from socket import timeout
import webbrowser
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr # for speech Recognition 
import ctypes     # ctypes module to load windows library
#from ecapture import ecapture as ec # for camera 
#import cv2 # for camera 
import numpy as np
import psutil # for ending any app 
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
