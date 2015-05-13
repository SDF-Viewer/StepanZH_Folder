from tkinter import *


class Manual(Toplevel):
    def __init__(self, root, **kwargs):
        Toplevel.__init__(self, master=root, **kwargs)
        self.title("Справка")
        self.resizable(0, 0)
        self.TextBox = Text(self)
        self.YScrollBar = Scrollbar(orient=VERTICAL)
        