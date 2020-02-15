from tkinter import *
from tkinter import Tk, Label,Frame, Button, Menu
from main import EyeDet
from math import hypot
from pynput.keyboard import Controller
#import time


#from test import test

class display(EyeDet):
    global count
    global entry
    count=0
    
    
    def print_me():
        print(entry.get())
        
    def __init__(self, master):
        global count
        global entry
        elem = EyeDet()
        master.title("IDetector")
        master.geometry("600x400+200+0")
        menu = Menu(master)
        master.config(menu=menu, bg="#49504F")
        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Exit", command=self.finish)
        self.container1 = Frame(master, width=100, height=100)
        self.container1.pack()
        self.title = Label(self.container1, text="Welcome To IDetector", fg="#C9E9E5", bg="#49504F", font="Helvetica 40", pady=40, bd=2)
        self.title.grid(row=0, columnspan=5)
        self.container2 = Frame(master, width=100, height=20)
        self.container2.pack()
        self.button1 = Button(self.container2, text="Click here to start eye detection and do wonderful things", bg="#eee", font="Times 15", height=10, width = 60)
        self.button1.grid(row=0)
        self.button1.bind("<Button-1>", elem.starter)     
#        self.container3 = Frame(master)
#        self.container3.config(bg="#49504F")
#        entry= Entry(self.container2)
#        entry.grid(row=1, padx=10, pady=10)
#        self.button2 = Button(self.container3, text="Start Exam", command = self.print_me)
#        self.button2.pack()
#        self.enter = Text(self.container2)
#        self.enter.grid(row=1, pady = 10, padx=10)
#        result = self.enter.get(1.0,END)
#        self.status = Label(master, text="Test Exam", bd=1, relief=SUNKEN)
#        self.status.pack(side=BOTTOM, fill=X)


    def finish(self):
        root.destroy()

                 
if __name__ =="__main__":
    root = Tk()
    start = display(root)
    root.mainloop()

