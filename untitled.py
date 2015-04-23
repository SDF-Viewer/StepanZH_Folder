from tkinter import *

root = Tk()

F = Frame(root)
C = Canvas(F, scrollregion=(0, 0, 500, 500))
XB = Scrollbar(F, width=100, orient=HORIZONTAL)

C.create_line(50, 50, 100, 100, width=2, arrow=LAST)
XB.config(command=C.xview)
C.config(xscrollcommand=XB.set)

XB.grid(row=1, column=0, sticky='ew')
C.grid(row=0, column=0)

C.create_line(50, 50, 100, 75, width=2, arrow=LAST)
C.delete('all')

F.pack()
root.mainloop()