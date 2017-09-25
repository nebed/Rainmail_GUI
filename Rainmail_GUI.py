#-*-coding:utf8;-*-
from tkinter import *
	
def express_gui():
	express = Toplevel(rainmail)
	express.title('Express Mode')
	express.geometry('500x400')
    

def prompt_gui():
	rainmail = Tk()
	rainmail.title('Rainmail GUI')
	rainmail.geometry('500x400')
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label='Exit', command=rainmail.quit)
	menubar.add_cascade(label='File', menu=filemenu)
    
	options = Menu(menubar, tearoff=0)
	options.add_command(label='Express Mode', command=express_gui)
	options.add_seperator()
	options.add_command(label='Normal Mode', command=user_gui)
	menubar.add_cascade(label='Select Mode', menu=options)
    
    
    
    
    
