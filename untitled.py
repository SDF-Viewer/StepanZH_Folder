from tkinter import *

def myprint(event):
    print(event.widget)
    event.widget.config(bg='blue')

root = Tk()

F = Frame(root, width=100, height=100, bg='yellow')
B = Button(F, text='<', width=10, height=10)
B.bind("<Button-1>", myprint)
B.grid(row=0, column=0)
print(super())
F.pack()
root.mainloop()