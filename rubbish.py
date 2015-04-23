from tkinter import *
from molecules_list import *

class UnitedFrameWidget:
    def __init__(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height
        self.FrameMe = Frame(root, width=width, height=height)

    def grid(self, row, column, sticky):
        self.FrameMe.grid(row=row, column=column, sticky=sticky)


class CanvasFrame(UnitedFrameWidget):
    def __init__(self, root, width, height):
        UnitedFrameWidget.__init__(self, root, width, height)

        self.Canvas = Canvas(self.FrameMe, scrollregion=(-400, -400, 400, 400), bg="lightyellow",
                             cursor="pencil")

        self.YScrollBar = Scrollbar(self.FrameMe, orient=VERTICAL)
        self.YScrollBar.config(command=self.Canvas.yview())
        self.Canvas.config(yscrollcommand=self.YScrollBar.set)

        self.XScrollBar = Scrollbar(self.FrameMe, orient=HORIZONTAL)
        self.XScrollBar.config(command=self.Canvas.xview())
        self.Canvas.config(xscrollcommand=self.XScrollBar.set)

        self.YScrollBar.grid(row=0, column=0, sticky='ns')
        self.XScrollBar.grid(row=2, column=2, sticky='we')
        self.Canvas.grid(row=0, column=1)