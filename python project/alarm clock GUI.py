from tkinter import *
from tkinter import messagebox
import time, sys
from pygame import mixer
from PIL import Image, ImageTk

mixer.init()

def alarm():
    alarm_time=user_input.get()
    if alarm_time=="":
        messagebox.askretrycancel("Error Message","Please Enter Value")
    else:
         while True:
            time.sleep(1)
         if (alarm_time==time.strftime("%H:%M")):
            playmusic()
def playmusic():
    mixer.init()
    mixer.music.load('Alarm 2.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
      time.sleep(30)
      mixer.music.stop()
      sys.exit()

root=Tk()
root.title("Alarm Clock")
root.geometry("600x338")
canvas=Canvas(root,width=600,height=338)
image=ImageTk.PhotoImage(Image.open("python alarm clock new.jpg"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
header=Frame(root)

box1=Frame(root)
box1.place(x=250,y=180)
box2=Frame(root)
box2.place(x=250,y=260)
#Time taken by the user as input
user_input=Entry(box1,font=('Arial Narrow',20),width=8)
user_input.grid(row=0,column=2)
#Set Alarm Button
start_button=Button(box2,text="Set Alarm",font=('Arial Narrow',16,'bold'),command=alarm)
start_button.grid(row=2,column=2)

root.mainloop()