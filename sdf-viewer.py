""" SDF-Viewer
"""

import sys
from tkinter import*
from wpanel import*
from menu_bar import*


class AppWindow(Tk):
    def __init__(self, **kwargs):
        ### GUI ###
        Tk.__init__(self, **kwargs)
        self.wm_title('SDF-Viewer')
        self.WorkingFrame = WorkingPanel(root=self)
        self.AppMenu = GMenu(root=self)
        self.config(menu=self.AppMenu)

        self.WorkingFrame.grid(row=0, column=0, sticky='nwes')

        ### DATA ###
        self.open_file_name = None
        self.MoleculesListDB = []

    def open_file(self, file_name):
        self.open_file_name = file_name
        file = open(file_name, 'tr')
        OpenMoleculeslist = extract_molecules_list_from_sdf(file, 'Source')
        file.close()

        self.MoleculesListDB.append(OpenMoleculeslist)
        self.WorkingFrame.change_molecules_list(OpenMoleculeslist)


def main(argv=None):
    if argv is None:
        pass
    try:
        MainWindow = AppWindow()
        MainWindow.mainloop()
    except:
        pass


if __name__ == "__main__":
    sys.exit(main())