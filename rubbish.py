from tkinter import *


def ch_red(event):
    if event.delta == 120:
        root.config(bg='red')
    elif event.delta == -120:
        root.config(bg='blue')
    print(event.x, event.y)

root = Tk()

text = Text(root)
ch_list = []

for i in range(9):
    ch_list.append(1)
    chb = Checkbutton(text='5', variable=ch_list[i], onvalue=1, offvalue=0)
    chb.select()
    text.window_create("end", window=chb)
    text.insert("end", '\n')

b = Button(root)
b.pack()

#b.bind("<Button-1>", lambda event: ch_list[5] = 1)

text.pack()
root.mainloop()