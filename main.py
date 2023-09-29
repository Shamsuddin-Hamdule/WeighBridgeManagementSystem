import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import webbrowser
import subprocess
from PIL import Image, ImageTk

root = tk.Tk()
window_width = 1200
window_height = 500

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#root.geometry('1200x750')
root.title('Weigh Bridge Management Sysytem')
root.resizable(False,False)

def open_link():
    url = "https://www.google.com"  # Replace this with your desired link
    webbrowser.open(url)

def del_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def init(page):
    del_pages()
    page()

options_frame = tk.Frame(root, bg='#c3c3c3')

Master_btn = tk.Button(options_frame,text='Master Entries',font=('Bold',15),border=4,
                     fg='#1500ff',bd=3,command=lambda: init(ME)).grid(row=0,column=0)#place(x=10,y=10)
tr_btn = tk.Button(options_frame,text='Transactions',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(Tr)).grid(row=0,column=1)#place(x=90,y=10)
rep_btn = tk.Button(options_frame,text='Reports',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(Re)).grid(row=0,column=2)#place(x=210,y=10)
tools_btn = tk.Button(options_frame,text='Administrative tools',font=('Bold',15),
                    fg='#1500ff',bd=3,command=lambda: init(AT)).grid(row=0,column=4)#place(x=410,y=10)
util_btn = tk.Button(options_frame,text='Utilities',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(Ut)).grid(row=0,column=3)#place(x=320,y=10)
Exit_btn = tk.Button(options_frame,text='Exit',font=('Bold',15),
                     fg='#1500ff',bd=3,command=lambda: init(EX)).grid(row=0,column=7)#place(x=810,y=10)
options_frame.pack()#.grid(row=0,column=0)
##options_frame.pack_propagate(False)
options_frame.configure(width=1200,height=60)

main_frame = tk.Frame(root,highlightbackground="black"
                      ,highlightthickness=2)
image_path = "wlc.png"  # Replace this with your image file path
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(main_frame, image=photo)
image_label.pack(pady=50)

main_frame.pack()#.grid(row=1,column=0)
#main_frame.pack_propagate(False)
main_frame.configure(height=900,width=1200)



def ME():
    me_frame=tk.Frame(main_frame)
    def mat():
        subprocess.run(["python","material.py"])
    Mater = tk.Button(me_frame,text="Material",command=mat).grid(row=0,column=0)
    def cus():
        subprocess.run(["python","Customer.py"])
    Cust = tk.Button(me_frame,text="Customer",command=cus).grid(row=1,column=0)
    def tru():
        subprocess.run(["python","Truck.py"])
    Truck = tk.Button(me_frame,text="Truck",command=tru).grid(row=2,column=0)
    def desti():
        subprocess.run(["python","Destination.py"])
    des = tk.Button(me_frame,text="Destination",command=desti).grid(row=3,column=0)
    def surc():
        subprocess.run(["python","Source.py"])
    sour = tk.Button(me_frame,text="Source",command=surc).grid(row=4,column=0)
    me_frame.place(x=300,y=10)
def Tr():
    tr_frame=tk.Frame(main_frame)
    def WR():
        subprocess.run(["python","weighing.py"])
    WR_btn=tk.Button(tr_frame,text="Weighing Details",command=WR).grid(row=0,column=0)
    tr_frame.place(x=400,y=10)
def Re():
    re_frame=tk.Frame(main_frame)
    def CVR():
        subprocess.run(["python","CustRep.py"])
    CustV_btn=tk.Button(re_frame,text="Customer Vise Report",command=CVR).grid(row=0,column=0)
    def MVR():
        subprocess.run(["python","MatRep.py"])
    MatV_btn=tk.Button(re_frame,text="Material Vise Report",command=MVR).grid(row=1,column=0)
    def DVR():
        subprocess.run(["python","DesRep.py"])
    DesV_btn=tk.Button(re_frame,text="Destination Vise Report",command=DVR).grid(row=2,column=0)
    def SVR():
        subprocess.run(["python","SoRep.py"])
    SoV_btn=tk.Button(re_frame,text="Source Vise Report",command=SVR).grid(row=3,column=0)
    def TVR():
        subprocess.run(["python","TrRep.py"])
    trV_btn=tk.Button(re_frame,text="Truck Vise Report",command=TVR).grid(row=4,column=0)
    re_frame.place(x=500,y=10)
def AT():
    at_frame=tk.Frame(main_frame)
    def SM():
        subprocess.run(["python","serial_monitor_v03.py"])
    WCV_btn=tk.Button(at_frame,text="Weighing Configuration",command=SM).grid(row=0,column=0)
    at_frame.place(x=700,y=10)

def ms():
    subprocess.run(["python", "wbms.py"])
    #import wbms.py
def Ut():
    ut_frame=tk.Frame(main_frame)
    LOV_btn=tk.Button(ut_frame,text="log Off",command=Exit).grid(row=0,column=0)
    ut_frame.place(x=600,y=10)

def Exit():
    root.destroy()
def EX():
    ex_frame=tk.Frame(main_frame)
    lb = tk.Button(ex_frame,text="Exit",command=Exit,
                  font=('Bold',10)).pack()
    ex_frame.place(x=850,y=10)

