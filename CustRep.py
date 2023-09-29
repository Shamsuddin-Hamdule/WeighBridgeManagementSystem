import tkinter as tk
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime

now=datetime.datetime.now()

root = tk.Tk()
window_width = 800
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
root.title('WBMS')
root.resizable(False,False)
main_frame = tk.Frame(root,highlightbackground="black"
                      ,highlightthickness=2)
main_frame.pack()
main_frame.pack_propagate(False)
main_frame.configure(height=700,width=1200)

Id = StringVar()
name = StringVar()
Comp = StringVar()
br = StringVar()

Id1=Id.get()
name1=name.get()
Comp1=Comp.get()
br1=br.get()
con= sqlite3.connect('WBMS.txt')
cur= con.cursor()
def show_data():
    name1 = name
    con= sqlite3.connect('WBMS.txt')
    cur= con.cursor()
    cur.execute('''select * from Customer''')
    for record in cur:
        print('ID :',str(record[0])+'\n')
        print('Name:',str(record[1])+'\n')
        print('Date:',str(record[2])+'\n')
        print('Time:',str(record[3]+'\n'))

def gbId():
    Id1=Id.get()
    name1=name.get()
    Comp1=Comp.get()
    br1=br.get()
    cur.execute('''select * from Customer where Id=?''',(Id1,))
    for record in cur:
        print('ID :',str(record[0])+'\n')
        print('Name:',str(record[1])+'\n')
        print('Date:',str(record[2])+'\n')
        print('Time:',str(record[3]+'\n'))

def Cus():
    Id1=Id.get()
    name1=name.get()
    Comp1=Comp.get()
    br1=br.get()
    cur.execute('''select * from Customer where name=?''',(name1,))
    for record in cur:
        print('ID :',str(record[0])+'\n')
        print('Name:',str(record[1])+'\n')
        print('Date:',str(record[2])+'\n')
        print('Time:',str(record[3]+'\n'))


def prnt():
    print(root)

def close():
    root.destroy()
    
Cus_frame=tk.Frame(main_frame)
lb = tk.Label(Cus_frame,text="Customer Wise Report",padx=10,pady=30,
              font=('Bold',40)).grid(row=0,column=0,columnspan=6)

Comp_l=tk.Label(Cus_frame,text="Company name",padx=5,pady=30,font=('Bold',15)).grid(row=1,column=0)
Comp_E=tk.Entry(Cus_frame,textvariable=Comp,font=('Bold',15)).grid(row=1,column=1)
    
BR=tk.Label(Cus_frame,text="Branch Name",padx=5,pady=30,font=('Bold',15)).grid(row=1,column=2)
BR_E=tk.Entry(Cus_frame,textvariable=br,font=('Bold',15)).grid(row=1,column=3,columnspan=2)

Cus_ID=tk.Label(Cus_frame,text="Customer ID",padx=5,pady=30,font=('Bold',15)).grid(row=2,column=0)
Cus_id=tk.Entry(Cus_frame,textvariable=Id,font=('Bold',15)).grid(row=2,column=1)
    
Cus_Name=tk.Label(Cus_frame,text="Customer Name",padx=5,pady=30,font=('Bold',15)).grid(row=2,column=2)
Cus_name=tk.Entry(Cus_frame,textvariable=name,font=('Bold',15)).grid(row=2,column=3,columnspan=2)

getBYid=tk.Button(Cus_frame,text="get Report By Customer Id",command=gbId).grid(row=6,column=0)
getBYid=tk.Button(Cus_frame,text="get Report By Customer Name",command=Cus).grid(row=6,column=1)

prnt=tk.Button(Cus_frame,text="Print",font=('Bold',15)
                  ,command=prnt).grid(row=6,column=3)
cl=tk.Button(Cus_frame,text="Close",font=('Bold',15)
                  ,command=close).grid(row=6,column=4)
Cus_frame.pack()
