import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#create a dictionary for each topic, each dict is a key-value pair with a list

Questions_dict={
    'What is the difference between for and while loop?': ['for loops are used for indefinite iteration and while loops for definite iteration', 
                'There is no difference between them', 
                'while loops are used for indefinite iteration and for loops are for definite iteration',
                'while" loops can only iterate over numbers, for loops can iterate over any data type'],
    'How do you exit a loop prematurely in python?':['exit statement', 'stop statement','break statement','range statement']
}
#counter for questions
current_q_index=0
#counter for score
score_count=0

#now a function that checks for the results
def check_answer():
    global current_q_index, score_count
    selected_answer=user_answer.get()
    correct_answer=Questions_dict[list(Questions_dict.keys())[current_q_index-1]][2]
    if correct_answer==selected_answer:
        labelA=tk.Label(window,text='CORRECT!', font=('Helvetica',20),fg='blue')
        labelA.pack()
        score_count=score_count+1
    else:
        LabelW=tk.Label(window,text=f'Sorry!!!\n the correct answer is\n {correct_answer}', font=('Helvetica,20'),fg='blue')
        LabelW.pack()

#Now to display each question at a time
def display_quiz():
    for widget in window.winfo_children():
        widget.destroy()
    global current_q_index,user_answer
    if current_q_index<len(Questions_dict):
        questions, choices=list(Questions_dict.items())[current_q_index]
        q_label=tk.Label(window, text=questions)
        q_label.pack()\
    
        user_answer.set('')
        
        for x in choices:
            choices_button=ttk.Radiobutton(window, text=x, variable=user_answer,value=x)
            choices_button.pack()
        current_q_index=current_q_index+1
        Next_button=tk.Button(window, text ='Next', command=display_quiz)
        Next_button.pack()
        check_button=tk.Button(window,text='Check Answer',command=check_answer)
        check_button.pack()

    else:
         messagebox.showinfo('Well Done!!',f'Your score is {score_count}')
  

#create the basic layout of the GUI
window=tk.Tk()

#let us create the first window that allows user to choose a topic to study
window.geometry('800x500')
window.title('Studdy Buddy Quiz App')

user_answer=tk.StringVar()
label=tk.Label(window, text='Test your knowledge of Python with StudyBuddy!!!', font=('Times New Roman',24), fg='blue')
label.pack(padx=10,pady=10)

topic2=tk.Button(window,text='START QUIZ', font=('Gothic',20),fg='green',command=display_quiz)
topic2.pack()

window.mainloop()

