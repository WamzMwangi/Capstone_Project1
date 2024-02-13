import tkinter as tk
from tkinter import ttk
window=tk.Tk()

#let us create the first window that allows user to choose a topic to study
window.geometry('800x500')
window.title('Studdy Buddy Quiz App')


label=tk.Label(window, text='Test your knowledge of Python with StudyBuddy!!!', font=('Times New Roman',24), fg='blue')
label.pack(padx=10,pady=10)

label=tk.Label(window,text='Please choose a topic you want to study', font=('Times New Roamn',18))
label.pack()

button=tk.Button(window,text='VARIABLES', font=('Gothic',14),fg='green')
button.pack()

button=tk.Button(window,text='ITERATIONS', font=('Gothic',14),fg='green')
button.pack()

window.mainloop()

#now to add functionality to the buttons