from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
import time
import speech_recognition as sr
import pyaudio
from tkinter.scrolledtext import ScrolledText
#*************************gui code *******************************
#scrolledtext is compund text with scroll


recognizedText = ""
temp = ""

def reocognizeSpeech() :
     print("gwa l function")
     r = sr.Recognizer()
     with sr.Microphone() as source:

        audio = r.listen(source)
        
        try :
            recognizedText = r.recognize_google(audio)
            return recognizedText
        except Exception as e:
            print(e)

    
     return recognizedText





def startSpeech(scrolltext,speechtotextlabel):
    scrolltext.delete('1.0', END)
    temp=reocognizeSpeech()
    speechtotextlabel.configure(text="Check you text now")
    scrolltext.insert(INSERT,temp + "\n")




root=Tk()
root.geometry("700x350+300+300")
root.title('speech to text')
root.resizable(0,0)
root.iconbitmap(r'icons8-voice-recognition-30.ico')


scrolltext=ScrolledText(root, width=60, height=15)
scrolltext.place(x=35,y=65)

speechtotextlabel=Label(root,text='click the mic button to start speech')
speechtotextlabel.place(x=45,y=20)

startButtonimage=PhotoImage(file="icons8-microphone-35.png")
stopbuttonimage=PhotoImage(file="icons8-stop-squared-35.png")
clearbuttonimage=PhotoImage(file="icons8-clear-symbol-35.png")

startspeechbutton=Button(root,text="Start",fg='black',image=startButtonimage,command=lambda :startSpeech(scrolltext,speechtotextlabel))
startspeechbutton.place(x=580,y=110)

root.mainloop()
