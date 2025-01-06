from tkinter import *
window = Tk()

coordinateList=[]

def submit():
    x = entry.get()

entry = Entry(window, font=("Arial",25))
entry.grid(row=0, column=0)

submit = Button(window, text="Submit", font=("Arial",25),command=submit)
submit.grid(row=0, column=1)


window.mainloop()