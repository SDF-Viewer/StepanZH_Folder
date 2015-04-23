from tkinter import *
from molecules_list import *
from module_ref import *


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



class WorkingPanel(UnitedFrameWidget):
    """ Рабочая панель, объединяющая 3 фрейма для работы со списком молекул
    """
    def __init__(self, root, width, height, MoleculesList=None):
        """ Наследует свойства родителя, также закрепляет за собой MoleculeList,
            инициализирует 3 фрейма: рисунок молекулы, панель навигации и таблицу полей
        """
        UnitedFrameWidget.__init__(self, root, width, height)
        self.CanvasFrame = CanvasFrame(root, width=width, height=int(height * 0.5))
        self.NavigationFrame = NavigationFrame(root, width=width, height=int(height * 0.1))
        self.FieldsFrame = FieldsFrame(root, width=width, height=int(height * 0.4))
        # исключение
        if MoleculesList != None:
            import copy
            self.MoleculesList = copy.deepcopy(MoleculesList)
            self.MoleculesList.mol_list = copy.deepcopy(MoleculesList.mol_list)
        else:
            self.MoleculesList = None
        self.create_scaffold()

    def create_scaffold(self):
        """ Размещает составляющие на WorkingPanel друг под другом
        """
        self.CanvasFrame.grid(row=0, column=0)
        self.NavigationFrame.grid(row=1, column=0)
        self.FieldsFrame.grid(row=2, column=0)

    def fill(self, Molecule):
        """ Наполняет составляющие содержимым, также подгружает новую молекулу
        """
        self.CanvasFrame.fill(Molecule)


class CanvasFrame(UnitedFrameWidget):
    """ Фрейм, содержащий рисунок молекулы и ползунки для навигации по рисунку
    """
    def __init__(self, root, width=500, height=500):
        UnitedFrameWidget.__init__(self, root, width, height)

        self.Canvas = Canvas(self.FrameMe, width=int(width*0.9), scrollregion=(-200, -200, 600, 600), bg="lightyellow",
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


class NavigationFrame(UnitedFrameWidget):
    pass


class FieldsFrame(UnitedFrameWidget):
    pass


'''
file = open('sdf_list.sdf', 'tr')

lm = extract_molecules_list_from_sdf(file, 'Source')
file.close()

CurrLeftMolecule = lm[0]
field_order_list = lm[0].field_order_list

root = Tk()

WPanelFrameLeft = Frame(root)
wpanel_fill(WPanelFrameLeft, CurrLeftMolecule)

WPanelFrameLeft.pack()

root.mainloop()'''