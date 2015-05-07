from tkinter import*


class GMenu(Menu):
    def __init__(self, root, **kwargs):
        Menu.__init__(self, root, **kwargs)
        # self.FileMenu = Menu(self)
        # self.add_cascade(label='Файл', menu=self.FileMenu)
        self.ParentWindow = root
        self.set_commands()


    def set_commands(self):
        self.add_command(label='Открыть файл', command=self.open_file)

    def open_file(self):
        import tkinter.filedialog
        # добавить, чтоб только SDF видел
        open_file_name = tkinter.filedialog.askopenfilename()
        self.ParentWindow.open_file(open_file_name)

    def create(self):
        pass
