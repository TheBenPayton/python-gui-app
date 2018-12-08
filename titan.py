"""Created by: Payton Long
    STILL IN BEGINNING STAGES
    GITHUB: THEBENPAYTON"""

from tkinter import *
from tkinter import messagebox
from datetime import datetime
import random
import time
import os
import math
import urllib


#********HERE STARTS THE ENTER PASSWORD/KEY WINDOW******************************************************************
class Launch(Frame):

    def __init__(self, first):
        Frame.__init__(self, first)
        self.grid()
        self.widgits()

    def widgits(self):
        self.ask = Label(self, text = "Hello, and welcome to Project Titan! I am absolutely pleased")
        self.ask.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.ask2 = Label(self, text = " that you have decided to help progress Titan in its developmental ")
        self.ask2.grid(row = 2, column = 0, columnspan = 2, sticky = W)

        self.ask3 = Label(self, text = "stages! Here are some instructions..")
        self.ask3.grid(row = 3, column = 0, columnspan = 2, sticky = W)

        self.key_in = Entry(self)
        self.key_in.grid(row=5, column=0, sticky=W)

        self.submit = Button(self, text="Submit Key!", command=self.function)
        self.submit.grid(row=6, column=0, sticky=W)

        self.reply = Text(self, width=35, height=5, wrap=WORD)
        self.reply.grid(row=8, column=0, columnspan=2, sticky=W)

        #self.close_button = Button(self, text="Click To Close!", command=root.destroy)
        #self.close_button.grid(row=7, column=0, columnspan=1, sticky=W)


    def function(self):
        key = self.key_in.get()

        if  key == "FLARE":
            #reply = "WELCOME TO TITAN!"
            messagebox.showinfo("Access Granted:", "Welcome to Titan Beta!")
            time.sleep(1)
            root.destroy()
        else:
            reply = "Sorry. You have entered an invalid key."

        self.reply.delete(0.0, END)
        self.reply.insert(0.0, reply)

root = Tk()
root.title("Titan 1.2 Welcome!")
root.geometry("450x400")
app = Launch(root)
root.configure(background='red')
root.mainloop()

#****************HERE STARTS THE ACTUAL FRAME AFTER KEY IS ENTERED CORRECTLY**********************************
class Application(Frame):

    def __init__(titan, master):
        Frame.__init__(titan, master)
        titan.grid()
        titan.create_widgits()

    def create_widgits(titan):
        titan.welcome = Label(titan, text = "Hello! I am Titan. How may I help?")
        titan.welcome.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        titan.instruction = Label(titan, text = "Enter your question here:")
        titan.instruction.grid(row = 1, column = 0, sticky = W)

        titan.question = Entry(titan)
        titan.question.grid(row = 1, column = 1, sticky = W)

        titan.submit_button = Button(titan, text = "Ask Titan!", command = titan.reveal)
        titan.submit_button.grid(row = 2, column = 0, sticky = W)

        titan.text = Text(titan, width = 35, height = 5, wrap = WORD)
        titan.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)

        titan.exitButton = Button(titan, text="Click To Exit!", command = root.destroy)
        titan.exitButton.grid(row = 8, column = 1, columnspan = 1, sticky = W)

#BELOW HERE BEGINS TITANS MATH MODULE CODE FOR THE GUI******************************************************************

        titan.math_instruction = Label(titan, text="Enter your math here:")
        titan.math_instruction.grid(row=4, column=0, sticky=W)

        titan.math_q = Entry(titan)
        titan.math_q.grid(row=4, column=1, sticky=W)

        titan.math_submit = Button(titan, text="Ask Titan math!", command= titan.math)
        titan.math_submit.grid(row=5, column=0, sticky=W)

        titan.answer = Text(titan, width=35, height=5, wrap=WORD)
        titan.answer.grid(row=6, column=0, columnspan=2, sticky=W)

        titan.python_get = Button(titan, text="My GitHub", command=titan.get)
        titan.python_get.grid(row=8, column=0, sticky=W)
#THIS IS THE DEF FUNCTION FOR THE BASIC QUESTIONS AND COMMANDS FOR TITAN************************************************
    def reveal(titan):
        content = titan.question.get()

#BELOW HERE BEGINS THE "KNOWLEDGE BASE". UPDATE THE KNOWLEDGE AND ANSWERES HERE IN THE ELIF STATEMENTS.
#***************************************************************************************************************
        now = datetime.now()
        birthday = 1
        random_number = random.randint(0, 2350)
        pass_chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%*&"
        pass_len = 8
        password = "".join(random.sample(pass_chars, pass_len))

        if content == "What is the date?":
            message = "Today is: " + '%02d/%02d/%04d' % (now.month, now.day, now.year)

        elif content == "Generate a random password.":
            message = "Here is your password: --> " + password

        elif content == "What is the current time?":
            message = "The current time on Earth where you are located is: " + '%03d:%03d' % (now.hour, now.minute)

        elif content == "What is the time?":
            message = "The current time on Earth where you are located is: " + '%03d:%03d' % (now.hour, now.minute)

        elif content == "What time is it?":
            message = "The current time on Earth where you are located is: " + '%03d:%03d' % (now.hour, now.minute)

        elif content == "How far away is the sun?":
            message = "The sun is approximately 92.96 million miles from your home planet Earth."

        elif content == "What is your name?":
            message = "My name is Titan!"

        elif content == "Who created you?":
            message = "Payton Long is the human that developed me."

        elif content == "How old are you?":
            message = "I am " + str(birthday) + " year(s) old."

        elif content == "Guess a random number.":
            message = "Okay. Here is the number I'm thinking: " + str(random_number)

        elif content == "Hello.":
            message = "Hello there human! :)"

        elif content == "How far away is the moon?":
            message = "The moon is 238,900 miles from your home planet Earth."

        elif content == "How long is my name?":
            message = len("Payton")


#Don't add anymore knowledge code for Titan below this line it will mess the code up.
#*********************************************************************************************************************
        else:
            message = "Did you enter a question that Titan can process?"
        titan.text.delete(0.0, END)
        titan.text.insert(0.0, message)

#BELOW HERE IS TITANS DEF FUNCTION FOR THE MATH KNOWLEDGE MODULE******************************************************
    def math(titan):
        mquestion = titan.math_q.get()

        a = mquestion
        b = mquestion

        if mquestion == "Test":
            answer = "Hello world"


        else:
            answer = "Did you ask Titan a valid mathematical question?"



        titan.answer.delete(0.0, END)
        titan.answer.insert(0.0, answer)

#********THIS SECTION BEGINS THE OPEN BROWSER/URL BUTTON ACTIONS*************************************************************
    def get(titan):

        url = 'https://github.com/TheBenPayton'
        webbrowser.open_new(url)


#BELOW HERE BEGINS THE GUI LAYOUT SIZE AND COLOR DESIGN*****************************************************************
root = Tk()
root.title("Titan 1.2")
root.geometry("450x400")
app = Application(root)
root.configure(background='lightblue')
root.mainloop()

