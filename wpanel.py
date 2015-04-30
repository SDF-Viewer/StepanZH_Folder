from tkinter import *
from molecules_list import *
import module_ref


class WorkingPanel(Frame):
    """ Рабочая панель, объединяющая 3 фрейма для работы со списком молекул
    """

    def __init__(self, root, MoleculesList=None, **kwargs):
        """ Наследует свойства родителя, также закрепляет за собой MoleculeList,
            инициализирует 3 фрейма: рисунок молекулы, панель навигации и таблицу полей
        """
        Frame.__init__(self, root, **kwargs)
        self.CanvasFrame = CanvasFrame(root=self, bg='lightblue')
        self.NavigationFrame = NavigationFrame(root=self, ParentWorkingPanel=self, bg='red')
        self.FieldsFrame = FieldsFrame(root=self, bg='lightgreen')
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
        self.CanvasFrame.grid(row=0, column=0, sticky='we')
        self.NavigationFrame.grid(row=1, column=0, sticky='we')
        self.FieldsFrame.grid(row=2, column=0, sticky='wes')

        self.CanvasFrame.rowconfigure(0, weight=38)
        self.NavigationFrame.rowconfigure(2, weight=18)
        self.FieldsFrame.rowconfigure(1, weight=10)

    def turn_page(self, page_code):
        """ Смена отображаемого элемента списка молекул

            page_code: -1 -- next page, -2 -- previous page, 0, <-2 -- ignore, >0 -- goto page
        """
        if self.MoleculesList is not None:
            # определяем страницу, на которую нужно переключиться, исключая невозможные варианты
            if 0 < page_code <= self.pages_sum:
                self.active_page = page_code
                self.change_status(Molecule=self.MoleculesList.mol_list[self.active_page - 1])
            elif (page_code == -2) and (self.active_page > 1):
                self.active_page -= 1
                self.change_status(Molecule=self.MoleculesList.mol_list[self.active_page - 1])
            elif (page_code == -1) and (self.active_page < self.pages_sum):
                self.active_page += 1
                self.change_status(Molecule=self.MoleculesList.mol_list[self.active_page - 1])
            else:
                return

    def change_status(self, Molecule, set_empty_status=False):
        """ Наполняет составляющие содержимым, подгружает новую молекулу
        """
        if set_empty_status is False:
            self.NavigationFrame.change_status()
            self.FieldsFrame.fill(Molecule=Molecule)
            self.CanvasFrame.fill(Molecule=Molecule)
        else:
            self.active_page = 0
            self.pages_sum = 0
            self.MoleculesList = None
            self.NavigationFrame.change_status()

    def change_molecules_list(self, MoleculesList):
        import copy
        # self.MoleculesList = MoleculesList
        self.MoleculesList = copy.deepcopy(MoleculesList)
        self.MoleculesList.mol_list = copy.deepcopy(MoleculesList.mol_list)
        self.active_page = 1
        self.pages_sum = len(MoleculesList.mol_list)
        self.NavigationFrame.fill_molecules_box()
        self.change_status(Molecule=self.MoleculesList.mol_list[self.active_page - 1])


class CanvasFrame(Frame):
    """ Фрейм, содержащий рисунок молекулы и ползунки для навигации по рисунку
    """

    def __init__(self, root, **kwargs):
        Frame.__init__(self, root, **kwargs)

        self.Canvas = Canvas(self, bg="lightyellow", cursor="pencil")

        self.YScrollBar = Scrollbar(self, orient=VERTICAL)
        self.YScrollBar.config(command=self.Canvas.yview)
        self.Canvas.config(yscrollcommand=self.YScrollBar.set)

        self.XScrollBar = Scrollbar(self, orient=HORIZONTAL)
        self.XScrollBar.config(command=self.Canvas.xview)
        self.Canvas.config(xscrollcommand=self.XScrollBar.set)

        self.YScrollBar.grid(row=0, column=0, sticky='ns')
        self.XScrollBar.grid(row=1, column=1, sticky='we')
        self.Canvas.grid(row=0, column=1, sticky='we')
        self.Canvas.bind("<ButtonPress-1>", lambda event: self.Canvas.scan_mark(event.x, event.y))
        self.Canvas.bind("<B1-Motion>", lambda event: self.Canvas.scan_dragto(event.x, event.y, gain=1))

    def fill(self, Molecule):
        """ Подгрузка Canvas другой молекулой
        """
        import copy
        MoleculeCopy = copy.deepcopy(Molecule)
        MoleculeCopy.bond_block = copy.deepcopy(Molecule.bond_block)
        MoleculeCopy.atom_block = copy.deepcopy(Molecule.atom_block)
        "отцентровать холст! при перелистовании"
        self.Canvas.delete("all")
        module_ref.draw_mol(mol=MoleculeCopy, canv=self.Canvas)


class NavigationFrame(Frame):
    def __init__(self, root, ParentWorkingPanel, **kwargs):
        Frame.__init__(self, root, **kwargs)

        self.ParentWorkingPanel = ParentWorkingPanel
        self.PreviousPageButton = Button(self, text='<')
        self.PreviousPageButton.grid(row=0, column=0, sticky='e')

        self.NextPageButton = Button(self, text='>')
        self.NextPageButton.grid(row=0, column=1, sticky='w')

        self.PositionLabel = Label(self, text='0/0')
        self.PositionLabel.grid(row=0, column=2)

        self.GoToPageButton = Button(self, text='Перейти')
        self.GoToPageButton.grid(row=0, column=3)

        self.GoToPageEntry = Entry(self, width=5)
        self.GoToPageEntry.grid(row=0, column=4)

        # self.CallListButton = Button(self, text='Список молекул')
        # self.CallListButton.grid(row=0, column=5)
        import tkinter.ttk
        self.MoleculesBox = tkinter.ttk.Combobox(self, height=10, state='readonly')
        self.MoleculesBox.grid(row=0, column=5)

        self.columnconfigure(0, weight=8)
        self.columnconfigure(1, weight=8)
        self.columnconfigure(2, weight=8)
        self.columnconfigure(3, weight=8)
        self.columnconfigure(4, weight=4)
        self.columnconfigure(5, weight=20)

        self.set_binding()

    def change_status(self):
        """ Обработчик события 'смена страницы' для Navigation Panel

            Обновляет информацию Navigation Panel для пользователя
        """
        position_label = str(self.ParentWorkingPanel.active_page) + '/' + \
                         str(self.ParentWorkingPanel.pages_sum)
        self.PositionLabel.config(text=position_label)
        self.MoleculesBox.current(self.ParentWorkingPanel.active_page-1)

    def fill_molecules_box(self):
        curr_mol_list = self.ParentWorkingPanel.MoleculesList.mol_list
        molecules_names = [mol.header_list[0] for mol in curr_mol_list]
        self.MoleculesBox.config(values=molecules_names)

    def set_binding(self):
        self.NextPageButton.bind("<Button-1>", self.next_page_click)
        self.PreviousPageButton.bind("<Button-1>", self.previous_page_click)
        self.GoToPageButton.bind("<Button-1>", self.go_to_page_click)
        self.GoToPageEntry.bind("<Return>", self.go_to_page_click)
        self.MoleculesBox.bind("<<ComboboxSelected>>", self.select_from_box)

    def next_page_click(self, event):
        self.ParentWorkingPanel.turn_page(page_code=-1)

    def previous_page_click(self, event):
        self.ParentWorkingPanel.turn_page(page_code=-2)

    def go_to_page_click(self, event):
        try:
            page = int(self.GoToPageEntry.get())
            if 0 < page <= self.ParentWorkingPanel.pages_sum:
                self.ParentWorkingPanel.turn_page(page_code=page)
        except:
            pass
        self.GoToPageEntry.delete(first=0, last='end')

    def select_from_box(self, event):
        new_page = event.widget.current() + 1
        self.ParentWorkingPanel.turn_page(new_page)
        event.widget.selection_clear()


class FieldsFrame(Frame):
    def __init__(self, root, **kwargs):
        Frame.__init__(self, root, **kwargs)
        import tkinter.ttk

        self.Table = tkinter.ttk.Treeview(self)
        self.Table['columns'] = ('FieldValue')
        self.Table.heading('#0', text='Название поля')
        self.Table.heading('FieldValue', text='Значение поля')
        # self.Table.column('#0', width=150)
        # self.Table.column('FieldValue', minwidth=150)

        self.YScrollBar = Scrollbar(self)
        self.YScrollBar.config(command=self.Table.yview)
        self.Table.configure(yscrollcommand=self.YScrollBar.set)

        self.Table.grid(row=0, column=0, sticky=(N, S, E, W))
        self.YScrollBar.grid(row=0, column=1, sticky=(N, S))

    def fill(self, Molecule, common_order_list=None):
        self.Table.delete(*self.Table.get_children())
        if common_order_list is None:
            order_list = Molecule.fill_default_field_order_list()
        else:
            order_list = common_order_list
        for field_name in order_list:
            # не прописывает Name полностью!!
            self.Table.insert('', 'end', text=field_name,
                              values=(Molecule.fields_dict[field_name],))


######################################################################################
file = open('sdf_list.sdf', 'tr')
lm = extract_molecules_list_from_sdf(file, 'Source')
file.close()

root = Tk()

WPanelFrameLeft = WorkingPanel(root=root, MoleculesList=lm, bg='red')
# print(WPanelFrameLeft.MoleculesList == lm)

WPanelFrameLeft.grid(row=0, column=0, sticky=(N, E, W, S))
root.mainloop()