import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#create a dictionary for each topic, each dict is a key-value pair with a list
Variables_dict={
    'How can you convert a variable from one data type to another in python?': ['switch(variable_name)','change(variable_name)','type(variable_name)','convert(variable_name)'],
    'What is a variable?':['A constant value' , 'A reserved keyword in Python','A placeholder for storing data' ,' A mathematical operation']
}
Iterations_dict={
    'What is the difference between for and while loop?': ['for loops are used for indefinite iteration and while loops for definite iteration', 
                'There is no difference between them', 
                'while loops are used for indefinite iteration and for loops are for definite iteration',
                'while" loops can only iterate over numbers, for loops can iterate over any data type'],
    'How do you exit a loop prematurely in python?':['exit statement', 'stop statement','break statement','range statement']
}
#create functions that display the questions after topic is chosen

def variable_topic_chosen():
    for questions in Variables_dict.keys():
        q_label=tk.Label(window, text=questions)
        q_label.pack

def iterations_topic_chosen():
    for questions in Iterations_dict.keys():
        q_label=tk.Label(window, text=questions)
        q_label.pack


#create the basic layout of the GUI
window=tk.Tk()

#let us create the first window that allows user to choose a topic to study
window.geometry('800x500')
window.title('Studdy Buddy Quiz App')

label=tk.Label(window, text='Test your knowledge of Python with StudyBuddy!!!', font=('Times New Roman',24), fg='blue')
label.pack(padx=10,pady=10)

label=tk.Label(window,text='Please choose a topic you want to study', font=('Times New Roamn',18))
label.pack()

topic1=tk.Button(window,text='VARIABLES', font=('Gothic',14),fg='green',command=variable_topic_chosen)
topic1.pack()

topic2=tk.Button(window,text='ITERATIONS', font=('Gothic',14),fg='green')
topic2.pack()

window.mainloop()

#now to add functionality to the buttons