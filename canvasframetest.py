from module_ref import *
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



class CanvasFrame(UnitedFrameWidget):
    """ Фрейм, содержащий рисунок молекулы и ползунки для навигации по рисунку
    """
    def __init__(self, root, width=500, height=500):
        UnitedFrameWidget.__init__(self, root=root, width=width, height=height)

        self.Canvas = Canvas(self.FrameMe, width=int(width*0.9), scrollregion=(-600, -600, 600, 600), bg="lightyellow",
                             cursor="pencil")

        self.YScrollBar = Scrollbar(self.FrameMe, orient=VERTICAL)
        self.YScrollBar.config(command=self.Canvas.yview)
        self.Canvas.config(yscrollcommand=self.YScrollBar.set)

        self.XScrollBar = Scrollbar(self.FrameMe, orient=HORIZONTAL)
        self.XScrollBar.config(command=self.Canvas.xview)
        self.Canvas.config(xscrollcommand=self.XScrollBar.set)

        self.YScrollBar.grid(row=0, column=0, sticky='ns')
        self.XScrollBar.grid(row=1, column=1, sticky='we')
        self.Canvas.grid(row=0, column=1)

    def fill(self, Molecule):
        """ Подгрузка Canvas другой молекулой
        """
        draw_mol(Molecule, self.Canvas)

root = Tk()

file = open('sdf_list.sdf', 'tr')
lm = extract_molecules_list_from_sdf(file)
file.close()
mol = lm.mol_list[30]

F = Frame(root)
CFrame = CanvasFrame(F)

F.pack()
CFrame.grid(row=0, column=0)

CFrame.fill(mol)

root.mainloop()