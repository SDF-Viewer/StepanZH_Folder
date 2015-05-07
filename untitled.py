from tkinter import Tk, Frame, Menu


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Simple menu")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        # fileMenu = Menu(menubar)
        menubar.add_command(label="Exit", command=self.onExit)
        # menubar.add_cascade(label="File", menu=fileMenu)

    def onExit(self):
        import tkinter.filedialog
        # добавить, чтоб только SDF видел
        open_file_name = tkinter.filedialog.askopenfilename()


  
root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()