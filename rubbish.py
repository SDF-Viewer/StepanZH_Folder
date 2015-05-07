from tkinter import *


def ch_red(event):
    if event.delta == 120:
        root.config(bg='red')
    elif event.delta == -120:
        root.config(bg='blue')
    print(event.x, event.y)

root = Tk()

root.config()

root.bind('<MouseWheel>', ch_red)

root.mainloop()