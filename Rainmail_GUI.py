#-*-coding:utf8;-*-
from tkinter import *

def choose_keyword():
	
	
def express_gui():
	express = Toplevel(rainmail)
	express.title('Express Mode')
	express.geometry('500x400')
	values_to_set = Menubutton(express, text='Values to Set', relief=RAISED)
	values_to_set.grid()
	values_to_set_menu = Menu(values_to_set, tearoff=0)
	values_to_set_menu.add_command = (label='Choose What to Search', command=choose_keyword())
	
	
    

def prompt_gui():
	rainmail = Tk()
	rainmail.title('Rainmail GUI')
	rainmail.geometry('500x400')
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label='Exit', command=rainmail.quit)
	menubar.add_cascade(label='File', menu=filemenu)
    
	options = Menu(menubar, tearoff=0)
	options.add_command(label='Express Mode', command=express_gui())
	options.add_seperator()
	options.add_command(label='Normal Mode', command=user_gui())
	menubar.add_cascade(label='Select Mode', menu=options)
    
    
    
    
    
