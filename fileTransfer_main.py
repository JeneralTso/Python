'''
Python 3.6.0

Jenny Tso
GUI Drill

'''

from tkinter import *
import tkinter as ttk

import fileTransfer_gui
import fileTransfer_functions

class ParentFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.minsize(480, 420)
        self.master.maxsize(480, 420)
        #self.master.resizeable(False, False)
        #fileTransfer_functions.center_window(self, 480, 480)
        self.master.title("Transfer New or Modified Files")
        self.master.configure(bg="#F0F0F0")
        #self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        fileTransfer_gui.window(self)

if __name__ == "__main__":
    root = ttk.Tk()
    Application = ParentFrame(root)
    root.mainloop()
    
