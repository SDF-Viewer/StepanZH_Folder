from tkinter import *
from tkinter.filedialog import *
import fileinput

class W(Tk):
    def __init__(self, **kwargs):
        Tk.__init__(self, **kwargs)
        print('aa')

root = W()

root.mainloop()