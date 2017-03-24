from tkinter import *
from tkinter import ttk, messagebox

import fileTransfer_main
import fileTransfer_functions

def window(self):

    ttk.Label(self.master, text='Please select source and destination folders:').grid(row=0,column=0,columnspan=3,padx=15,pady=15,sticky='w')
    ttk.Label(self.master, text='Source folder:').grid(row=1,column=0,padx=15,sticky='w')

    ttk.Label(self.master, text='Destination folder:').grid(row=3,column=0,columnspan=2,padx=15,sticky='w')

    ttk.Label(self.master, text='Transfer files created or modified within the last 24 hours:').grid(row=7,column=0,columnspan=4,padx=15,pady=15,sticky='sw')

    self.srcDir = StringVar()
    self.field_src = ttk.Entry(self.master,width=59,text='',textvariable=self.srcDir)
    self.field_src.grid(row=2,column=0,columnspan=4,padx=15,sticky='e')
    self.destDir = StringVar()
    self.field_dest = ttk.Entry(self.master,width=59,text='',textvariable=self.destDir)
    self.field_dest.grid(row=4,column=0,columnspan=4,padx=15,sticky='e')

    ttk.Button(self.master,text='Browse',command=lambda:fileTransfer_functions.browseSrc(self)).grid(row=2,column=4,columnspan=1,padx=2,sticky='w')
    ttk.Button(self.master,text='Browse',command=lambda:fileTransfer_functions.browseDest(self)).grid(row=4,column=4,columnspan=1,padx=2,sticky='w')

    ttk.Button(self.master, text='List Files',command=lambda:fileTransfer_functions.listFiles(self)).grid(row=5,column=0,padx=15,pady='15',sticky='w')

    ttk.Button(self.master,text='Transfer',command=lambda:fileTransfer_functions.transfer(self)).grid(row=8,column=1,sticky='nw')
    ttk.Button(self.master,text='Clear All',command=lambda:fileTransfer_functions.clear(self)).grid(row=8,column=3,sticky='nw')

    self.scrollbar = Scrollbar(self.master,orient=VERTICAL)
    self.listbox = Listbox(self.master,width=72,height=8,yscrollcommand=self.scrollbar.set)
    self.listbox.grid(row=6,column=0,columnspan=5,padx=15,sticky='w')
    self.scrollbar.config(command=self.listbox.yview)
    self.scrollbar.grid(row=6,column=4,padx=5,sticky='nse')
    
    
if __name__ == "__main__":
    pass
