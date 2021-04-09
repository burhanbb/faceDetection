import cv2
import os
import numpy
from PIL import Image

import threading
import time
from tkinter import *
import face_data
import face_recognition
import face_training

class FuncThread(threading.Thread):
    def __init__(self,target):
        self.target=target
        super(FuncThread,self).__init__()
        self._stop_event=threading.Event()
        
    def stop(self):
        self._stop_event.set()
        
    def stopped(self):
        return self._stop_event.is_set()
    
    def run(self):
        self.target(self)
        
t1=FuncThread(face_data.face_data)
t2=FuncThread(face_training.face_training)
t3=FuncThread(face_recognition.face_recognition)

def main_screen():
    screen=Tk()
    screen.title("Burhan's Face Recognition")
    screen.geometry("600x550")
    Label(text="Welcome To Face Recognition").pack()
    Label(text="",height='2',width='30')
    Button(text="Register Your Face",height='2',width='30',bg="blue",command=t1.start).pack()
    Label(text="",height='2',width='30').pack()
    Button(text="Load Registered Data",height='2',width='30',bg="green",command=t2.start).pack()
    Label(text="",height='2',width='30').pack()
    Button(text="Start Recognition",height='2',width='30',bg="red",command=t3.start).pack()
    screen.mainloop()



main_screen()

