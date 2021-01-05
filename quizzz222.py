'''
The objective of this project is to develop a program in python where players test the knowledge about certain concepts from computer science.
This will be in the form of a quiz, a mind sport, in which the players attempt to answer questions correctly.
The program is an interactive, GUI based quiz that uses the modules tkinter, sql-connector and matplotlib.
At the end of the game, players can see where they stand compared to others who have also taken the same quiz by looking at the graphical comparison
made between the player's score and the average score. For deeper analysis players can also view other individual scores.

Author: Aditya Manthri
Date:   January 4, 2020
'''

import mysql.connector as sql

from tkinter import *

import matplotlib.pyplot as plt

#mydb=sql.connect(host="localhost",user="root",passwd="root123",database="quizaditya")

#This class represents questions, options, and the correct answer
#Includes operations such as displaying the question and options, validating the answer and moving to the next question

class Question:

#Initializes the object with question, options and the correct answer

        def __init__(self, question, answers, correctLetter):
            self.question = question
            self.answers = answers
            self.correctLetter = correctLetter

#Validates the option selected by the player and awards/deducts points accordingly

        def check(self, letter, view):
            global right,pointswin
            if(letter == self.correctLetter):
                label = Label(view, text="Right!")
                right += 1
                pointswin+=10
            else:
                label = Label(view, text="Wrong!")
                pointswin-=2
            label.pack()
            view.after(1000, lambda *args: self.unpackView(view))

#Displays question in textbox and options in the form of buttons

        def getView(self, window):
            view = Frame(window)
            Label(view, text=self.question).pack()
            Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
            Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
            Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
            Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
            return view

#Moves to the next question once an option is selected

        def unpackView(self, view):
            view.pack_forget()
            askQuestion()

#The following function is used to start the quiz by clicking the start button.
#After the quiz is over, final score and points are displayed.

def askQuestion():
        global questions, window, index, button, right, number_of_questions,pointswin
        button2 = Button(window, text='Click Here to Start', command=askQuestion,state= DISABLED).place(x=360,y=310)
        if(len(questions) == index + 1):
            Label(window, text="Thank you for answering the questions, "+Name+". You answered "+ str(right) + " of " + str(number_of_questions) + " questions right",bg = "cyan",font="Times 15 italic").place(x=100,y=260)
            Label(window, text="Total Points: " + str(pointswin),bg = "cyan",font="Times 25 italic").place(x=250,y=310)
            L.append(Name)
            L.append(pointswin)
            print(L)
            return
        #button.pack_forget()
        index += 1
        questions[index].getView(window).pack()

butt1 = 0
button2=0

#Allows the player to input name and then start the quiz

def details():
       global Name
       butt1 = Button(window, text='Submit', command=details, state = DISABLED).place(x=360,y=100)
       Name= e1.get()
       Label(window, text="Hello"+" " + Name+" !",bg = "orange",fg="blue",font="algerian 25 italic").pack()
       Label(window, text='''There are 5 questions to be answered.
       For each right answer, you get 10 points.
       For each wrong answer you lose 2 points.
        Lets play!''', bg="orange",font="times 20 italic").pack()
       button2=Button(window, text='Click Here to Start', command=askQuestion).place(x=360,y=310)

#Using File handling to extract the questions and answers from textfile named "questions.txt".

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
        questionString = line
        answers = []
        for i in range (4):
            answers.append(file.readline())

        correctLetter = file.readline()
        correctLetter = correctLetter[:-1]
        questions.append(Question(questionString, answers, correctLetter))
        line = file.readline()
file.close()

#Fixing initial values for index, right and pointwin

index = -1
right = 0
pointswin=0
Name=""
number_of_questions = len(questions)

window = Tk()
L=[]
v = IntVar()
e1=StringVar()

#The following lines of code are for displaying initial welcome text, entering name

Label(window,text="Welcome!",bg = "yellow",fg="blue",font="Times 25 bold").pack()

Label(window, text='Enter your Name: ',bg = "pink",font="Times 15 italic").pack()

Entry(window,width=20, textvariable=e1).pack()

# Button starting the quiz after the button submit is clicked.

butt1 = Button(window, text='Submit',command=details).place(x=360,y=100)

scrollbar = Scrollbar(window)


window.geometry("800x800")
window.mainloop()
print(L)


#The following lines of code are used to create table.
#These codes must be disabled after running the program once to avoid error (table should'nt be created again).

#cur=mydb.cursor()
#cur.execute('''create table statsquiz(
                #name varchar(25)
                #charge int)''')

#Now, inserting values into the table.


#cur = mydb.cursor()
st1 = '''Insert into statsquiz
           (name,score)
           values(%s,%s)
           '''
t = (L[0], L[1])
#cur.execute(st1, t)
#mydb.commit()
#cur.execute('Select * from statsquiz')
#d = cur.fetchall()
#for x in d:
#    print(x)
#cur.execute('select avg(score) from statsquiz')
avg=0
#for x in cur:
    #print("Average score is",x)
    #avg=x

#Now, using matplotlib module to plot average score, user's score and maximum score as a bar graph.

labs=["Your score","Average score","Max score"]
plt.bar(labs[0],L[1],width=0.8,color='aqua')
plt.ylabel("scores")
plt.bar(labs[1],avg,width=0.8,color='red')
plt.bar(labs[2],50,width=0.8,color='orange')
plt.show()

'''
Which of the following are true of Python lists?
A given object may NOT appear in a list more than once
All elements in a list must be of the same type
listS may contain any type of object except another list
There is no conceptual limit to the size of a list
D
One kilobyte is equal to:
1000 bytes
100 bytes
1024 bytes
1023 bytes
C
Which one of the following has the same precedence level?
Addition and Subtraction
Multiplication, Division and Addition
Multiplication, Division, Addition and Subtraction
Addition and Multiplication
A
Which supercomputer is developed by the Indian Scientists?
Param
Super 301
Compaq Presario
CRAY YMP
A
Find out the odd one from these options:
Internet
Linux
Unix
Windows
AX'''
