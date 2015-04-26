from tkinter.ttk import *
from tkinter import *

root = Tk()
root.config(width=800, height=800)

l = ['a', 'b']

F = Frame(root, bg='blue')

CB = Combobox(root, values=l)
CB.current(1)
print(CB.current())
CB.grid(sticky=(N))

root.mainloop()