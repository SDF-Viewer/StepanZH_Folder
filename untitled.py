from tkinter.ttk import *
from tkinter import *

root = Tk()
root.config(width=800, height=800)

tree = Treeview(root, columns=('1', '2'))

tree.column('1', anchor='w',  width=100)
tree.column('2', anchor='e', width=100)

tree.heading('#0', text='1616')
tree.heading('1', text='Field')
tree.heading('2', text='Value')
for i in range(50):
    tree.insert('', 'end', text=str(i), values=('2'))

S = Scrollbar(root, orient=VERTICAL)
S.grid(row=0, column=1, sticky='ns')
S.config(command=tree.yview)
tree.config(yscrollcommand=S.set)

tree.grid(row=0, column=0, sticky='nwes')
root.mainloop()