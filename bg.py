#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.24.1
#  in conjunction with Tcl version 8.6
#    Aug 27, 2019 12:41:11 AM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import bg_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    root.overrideredirect(True)
    bg_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    bg_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def close_window (): 
    root.destroy()

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family Calibri -size 14 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("600x310+705+443")
        top.title("New Toplevel")
        top.configure(background="#323539")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.0, rely=0.0, height=46, width=602)
        self.Label1.configure(background="#2A2D30")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(width=602)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.892, rely=0.0, height=29, width=55)
        self.Button1.configure(activebackground="#33CFDB")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#33CFDB")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../icon/Close-02-02.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img0)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')
        self.Button1.configure(width=60)
        self.Button1.configure(command = close_window)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.792, rely=0.0, height=29, width=55)
        self.Button2.configure(activebackground="#33CFDB")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#33CFDB")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../icon/Minimize-02.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Button2.configure(image=_img1)
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Button''')

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.067, rely=0.71, height=53, width=176)
        self.Button3.configure(activebackground="#ffffff")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#ffffff")
        self.Button3.configure(borderwidth="0")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font10)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Exit''')
        self.Button3.configure(width=176)

        self.Button3_3 = tk.Button(top)
        self.Button3_3.place(relx=0.617, rely=0.71, height=53, width=176)
        self.Button3_3.configure(activebackground="#33CFDB")
        self.Button3_3.configure(activeforeground="#000000")
        self.Button3_3.configure(background="#33CFDB")
        self.Button3_3.configure(borderwidth="0")
        self.Button3_3.configure(disabledforeground="#a3a3a3")
        self.Button3_3.configure(font=font10)
        self.Button3_3.configure(foreground="#000000")
        self.Button3_3.configure(highlightbackground="#33CFDB")
        self.Button3_3.configure(highlightcolor="black")
        self.Button3_3.configure(pady="0")
        self.Button3_3.configure(text='''Background''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.167, rely=0.226, height=26, width=402)
        self.Label2.configure(background="#323539")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Do you want to run the application in''')
        self.Label2.configure(width=402)

        self.Label2_4 = tk.Label(top)
        self.Label2_4.place(relx=0.167, rely=0.323, height=26, width=402)
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(activeforeground="black")
        self.Label2_4.configure(background="#323539")
        self.Label2_4.configure(disabledforeground="#a3a3a3")
        self.Label2_4.configure(font=font10)
        self.Label2_4.configure(foreground="#ffffff")
        self.Label2_4.configure(highlightbackground="#d9d9d9")
        self.Label2_4.configure(highlightcolor="black")
        self.Label2_4.configure(text='''background or exit the application''')

if __name__ == '__main__':
    vp_start_gui()





