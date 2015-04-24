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

    def __init__(self, root, width=700, height=600, MoleculesList=None):
        """ Наследует свойства родителя, также закрепляет за собой MoleculeList,
            инициализирует 3 фрейма: рисунок молекулы, панель навигации и таблицу полей
        """
        UnitedFrameWidget.__init__(self, root, width, height)
        self.CanvasFrame = CanvasFrame(root=self.FrameMe, width=width, height=int(height * 0.5))
        self.NavigationFrame = NavigationFrame(root=self.FrameMe, ParentWorkingPanel=self,
                                               width=width, height=int(height * 0.1))
        self.FieldsFrame = FieldsFrame(root=self.FrameMe, width=width, height=int(height * 0.4))
        self.create_scaffold()
        self.active_page = 0
        self.pages_sum = 0
        # исключение
        if MoleculesList is not None:
            self.change_molecules_list(MoleculesList)
        else:
            self.MoleculesList = None

    def create_scaffold(self):
        """ Размещает составляющие на WorkingPanel друг под другом
        """
        self.CanvasFrame.grid(row=0, column=0)
        self.NavigationFrame.grid(row=1, column=0)
        self.FieldsFrame.grid(row=2, column=0)

    def turn_page(self, page_code):
        """ Смена отображаемого элемента списка молекул

            page_code: -1 -- next page, -2 -- previous page, 0, <-2 -- ignore, >0 -- goto page
        """
        if self.MoleculesList is not None:
            # определяем страницу, на которую нужно переключиться, исключая невозможные варианты
            if 0 < page_code <= self.pages_sum:
                self.active_page = page_code
                self.change_status(MoleculesList.mol_list[self.active_page - 1])
            elif (page_code == -2) and (self.active_page > 1):
                self.active_page -= 1
                self.change_status(MoleculesList.mol_list[self.active_page - 1])
            elif (page_code == -1) and (self.active_page < self.pages_sum):
                self.active_page += 1
                self.change_status(MoleculesList.mol_list[self.active_page - 1])
            else:
                return


    def change_status(self, Molecule):
        """ Наполняет составляющие содержимым, также подгружает новую молекулу
        """
        self.NavigationFrame.change_status()
        self.CanvasFrame.fill(Molecule)
        # подгрузить таблицу

    def change_molecules_list(self, MoleculesList):
        import copy

        self.MoleculesList = copy.deepcopy(MoleculesList)
        self.MoleculesList.mol_list = copy.deepcopy(MoleculesList.mol_list)
        self.active_page = 1
        self.pages_sum = len(MoleculesList.mol_list)
        self.change_status(self.MoleculesList.mol_list[self.active_page - 1])


class CanvasFrame(UnitedFrameWidget):
    """ Фрейм, содержащий рисунок молекулы и ползунки для навигации по рисунку
    """

    def __init__(self, root, width=500, height=500):
        UnitedFrameWidget.__init__(self, root, width, height)

        self.Canvas = Canvas(self.FrameMe, width=int(width * 0.9), scrollregion=(-200, -200, 600, 600),
                             bg="lightyellow", cursor="pencil")

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
        self.Canvas.delete("all")
        draw_mol(Molecule, self.Canvas)


class NavigationFrame(UnitedFrameWidget):
    def __init__(self, root, ParentWorkingPanel, width=500, height=100):
        UnitedFrameWidget.__init__(self, root=root, width=width, height=height)

        self.ParentWorkingPanel = ParentWorkingPanel
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

        self.set_binding()

    def change_status(self):
        """ Обработчик события 'смена страницы' для Navigation Panel

            Обновляет информацию Navigation Panel для пользователя
        """
        position_label = str(self.ParentWorkingPanel.active_page) + '/' + \
                         str(self.ParentWorkingPanel.pages_sum)
        self.PositionLabel.config(text=position_label)
        # self.GoToPageEntry.delete(first=0, last=15)

    def set_binding(self):
        self.NextPageButton.bind("<Button-1>", self.next_page_click)
        self.PreviousPageButton.bind("<Button-1>", self.previous_page_click)

    def next_page_click(self, event):
        self.ParentWorkingPanel.turn_page(page_code=-1)

    def previous_page_click(self, event):
        self.ParentWorkingPanel.turn_page(page_code=-2)


class FieldsFrame(UnitedFrameWidget):
    pass


######################################################################################
file = open('sdf_list.sdf', 'tr')
lm = extract_molecules_list_from_sdf(file, 'Source')
file.close()

root = Tk()

WPanelFrameLeft = WorkingPanel(root, MoleculesList=lm)

WPanelFrameLeft.grid(row=0, column=0)
root.mainloop()