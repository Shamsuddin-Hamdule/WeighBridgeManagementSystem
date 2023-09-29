import tkinter as tk
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime

now=datetime.datetime.now()
n1=datetime.datetime.now()
fx1=n1.strftime("%x")
fx2=n1.strftime("%X")

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

Id1=Id.get()
name1=name.get()
con= sqlite3.connect('WBMS.txt')
cur= con.cursor()
cur.execute('''create table if not exists material(ID text,Name text,Date date,Time time)''')
def show_data():
    con= sqlite3.connect('WBMS.txt')
    cur= con.cursor()
    cur.execute('''select * from material''')
    for record in cur:
        print('ID :',str(record[0])+'\n')
        print('Name:',str(record[1])+'\n')
        print('Date:',str(record[2])+'\n')
        print('Time:',str(record[3]+'\n'))

def adde():           #ADDING DATA 
    Id1=Id.get()
    name1=name.get()
    cur.execute('''Insert into material(ID,Name,Date,Time)values(?,?,?,?)''',(Id1,name1,fx1,fx2))
    con.commit()
    show_data()

    tkinter.messagebox.showinfo('Congratulations !!','material successfully Added')

def upe():         #UPDATING DATA 
    Id1=Id.get()
    name1=name.get()
    cur.execute('''Update material SET Name=? WHERE ID=?''',(name1,Id1))
    con.commit()
    show_data()
    tkinter.messagebox.showinfo('Congratulations !!','material successfully updated')

def dele():
    Id1=Id.get()
    cur.execute('''Delete from material where ID=?''',(Id1,))
    con.commit()
    tkinter.messagebox.showinfo('Congratulations !!','material successfully Deleted')
    show_data()

def prnt():
    print(root)

def close():
    root.destroy()
    
Cus_frame=tk.Frame(main_frame)
lb = tk.Label(Cus_frame,text="Product Name Details",padx=10,pady=30,
              font=('Bold',40)).grid(row=0,column=0,columnspan=6)
Cus_ID=tk.Label(Cus_frame,text="Material ID",padx=5,pady=30,font=('Bold',15)).grid(row=1,column=0)
Cus_id=tk.Entry(Cus_frame,textvariable=Id,font=('Bold',15)).grid(row=1,column=1,columnspan=2)
    
Cus_Name=tk.Label(Cus_frame,text="Material Name",padx=5,pady=30,font=('Bold',15)).grid(row=1,column=2)
Cus_name=tk.Entry(Cus_frame,textvariable=name,font=('Bold',15)).grid(row=1,column=3,columnspan=2)

save=tk.Button(Cus_frame,text="Save",font=('Bold',15)
                  ,command=adde).grid(row=6,column=0)
Modify=tk.Button(Cus_frame,text="Modify",font=('Bold',15)
                  ,command=upe).grid(row=6,column=1)
dele=tk.Button(Cus_frame,text="Delete",font=('Bold',15)
                  ,command=dele).grid(row=6,column=2)
#new=tk.Button(Cus_frame,text="new",font=('Bold',15)
 #                 ,command=new).grid(row=6,column=3)
prnt=tk.Button(Cus_frame,text="Print",font=('Bold',15)
                  ,command=prnt).grid(row=6,column=3)
cl=tk.Button(Cus_frame,text="Close",font=('Bold',15)
                  ,command=close).grid(row=6,column=4)
Cus_frame.pack()
