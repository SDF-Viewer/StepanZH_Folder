from handlers import*
from molecule import*
from molecules_list import*
from module_ref import*
from tkinter import*


def create_canvas():
    root = Tk()
    canv = Canvas(root, width=600, height=500, bg="lightyellow",
                  cursor="pencil")
    canv.pack()
    canv.config(width=100, height=700)
    # scrollregion=(left, top, right, bottom)
    file = open('sdf_list.sdf', 'tr')
    lm = extract_molecules_list_from_sdf(file, 'Source')
    file.close()
    mol=lm.mol_list[29]
    draw_mol(mol, canv, 5)
    root.mainloop()
create_canvas()
