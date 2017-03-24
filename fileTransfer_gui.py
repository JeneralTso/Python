from tkinter import *
from tkinter import ttk

import fileTransfer_main
import fileTransfer_functions

def window(self):

    ttk.Label(self.master, text='Please select source and destination folders.').grid(row=0,column=0,columnspan=3,padx=15,pady=15,sticky='w')

    ttk.Label(self.master, text='Source folder:').grid(row=1,column=0,padx=15,sticky='w')
    ttk.Label(self.master, text='Destination folder:').grid(row=3,column=0,columnspan=2,padx=15,sticky='w')

    self.srcDir = StringVar()
    self.field_src = ttk.Entry(self.master,width=59,text='',textvariable=self.srcDir)
    self.field_src.grid(row=2,column=0,columnspan=3,padx=15,sticky='w')
    self.destDir = StringVar()
    self.field_dest = ttk.Entry(self.master,width=59,text='',textvariable=self.destDir)
    self.field_dest.grid(row=4,column=0,columnspan=3,padx=15,sticky='w')

    ttk.Button(self.master,text='Browse',command=lambda:fileTransfer_functions.browseSrc(self)).grid(row=2,column=2,columnspan=2,padx=2,sticky='e')
    ttk.Button(self.master,text='Browse',command=lambda:fileTransfer_functions.browseDest(self)).grid(row=4,column=2,columnspan=2,padx=2,sticky='e')

    '''
    self.browseBtn1 = ttk.Button(self.master,text='Browse')
    self.browseBtn1.grid(row=2,column=2,columnspan=2,padx=2,sticky='e')
    self.browseBtn2 = ttk.Button(self.master,text='Browse')
    self.browseBtn2.grid(row=4,column=2,columnspan=2,padx=2,sticky='e')
    '''

    ttk.Button(self.master, text='List Files',command=lambda:fileTransfer_functions.listFiles(self)).grid(row=6,column=0,padx=15,pady='15',sticky='w')

    self.scrollbar = Scrollbar(self.master,orient=VERTICAL)
    self.listbox = Listbox(self.master,width=72,yscrollcommand=self.scrollbar.set)
    #self.listbox.bind()
    self.listbox.grid(row=8,column=0,rowspan=3,padx=15,columnspan=4)
    self.scrollbar.config(command=self.listbox.yview)
    self.scrollbar.grid(row=8,column=4,rowspan=3,columnspan=1)
    

    ttk.Button(self.master,text='Yes, Transfer Files',command=lambda:fileTransfer_functions.transfer(self)).grid(row=12,column=1,pady=15,sticky='w')
    ttk.Button(self.master,text='No, Clear All',command=lambda:fileTransfer_functions.clear(self)).grid(row=12,column=2,pady=15,sticky='w')

        


if __name__ == "__main__":
    pass
