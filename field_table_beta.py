from tkinter import*
from tkinter import ttk

root = Tk()

class Table():

    Frame1 = Frame(root, height=100, width=400, bg = 'blue')

    Table = ttk.Treeview(Frame1)

'''
for i in range(30):
    text = str(i)
    Label1 = Label(Frame1, text=text)
    Label1.grid(row=i, column=0)
    
Scrollbar1 = Scrollbar(Frame1)
Scrollbar1.grid(row=0, rowspan=15, column=1, sticky='ns')
Scrollbar1['command'] = Frame1.yview
Frame1['yscrollcommand'] = Scrollbar1.set
'''
    Frame1.pack()

root.mainloop()
