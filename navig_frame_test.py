from tkinter import *
from molecules_list import *


class UnitedFrameWidget:
    """ Класс-родитель для фрейма Working Panel и фреймов, его составляющих:
        Canvas, Navigation, Fields ... Frames
    """

    def __init__(self, root, width=500, height=500):
        """ Инициализация свойств объединяющих фреймы
        """
        # каждый экземпляр (сложный фрейм) помнит, частью какого объекта является
        self.root = root
        self.width = width
        self.height = height
        # UnitedFrameWidget прежде всего рамка
        self.FrameMe = Frame(root, width=width, height=height, bg='lightblue')

    def grid(self, row, column, sticky=''):
        """ Размещает UnitedFrame
        """
        self.FrameMe.grid(row=row, column=column, sticky=sticky)


class NavigationFrame(UnitedFrameWidget):
    def __init__(self, root, width=500, height=100):
        UnitedFrameWidget.__init__(self, root=root, width=width, height=height)

        self.PreviousPageButton = Button(self.FrameMe, text='<')
        self.PreviousPageButton.grid(row=0, column=0)

        self.NextPageButton = Button(self.FrameMe, text='>')
        self.NextPageButton.grid(row=0, column=1)

        self.PositionLabel = Label(self.FrameMe, text='0/0')
        self.PositionLabel.grid(row=0, column=2)

        self.GoToPageButton = Button(self.FrameMe, text='Перейти')
        self.GoToPageButton.grid(row=0, column=3)

        self.GoToPageEntry = Entry(self.FrameMe)
        self.GoToPageEntry.grid(row=0, column=4)

        self.CallListButton = Button(self.FrameMe, text='Список молекул')
        self.CallListButton.grid(row=0, column=5)

root = Tk()

F = Frame(root)

Panel = NavigationFrame(F)

Panel.grid(row=0, column=0)
F.pack()
root.mainloop()