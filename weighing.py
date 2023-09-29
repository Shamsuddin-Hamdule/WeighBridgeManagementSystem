import tkinter as tk
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import serial
import serial.tools.list_ports
from tkinter import scrolledtext
import time
import re

now=datetime.datetime.now()

root = tk.Tk()
window_width = 800
window_height = 650

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
#root.resizable(False,False)
#textbox = scrolledtext.ScrolledText(root, height=1, width=30).pack(padx=5,pady=5)
main_frame = tk.Frame(root)
main_frame.pack()
main_frame.pack_propagate(False)
#main_frame.configure(height=700,width=1200)

global d1,t1,gr1

CN = StringVar()
Addr = StringVar()
mate = StringVar()
Id = StringVar()
name = StringVar()
Sorc = StringVar()
Desti = StringVar()
rema = StringVar()

CN1 = CN.get()
Addr1 = Addr.get()
mate1 = mate.get()
Id1=Id.get()
name1=name.get()
Sorc1 = Sorc.get()
Desti1 = Desti.get()
rem1 = rema.get()

con= sqlite3.connect('WBMS.txt')
cur= con.cursor()
cur.execute('''create table if not exists WD(Company_Name text,Address text,Serial_no text,Customer_Name text,Material text,
            source text,Destination text,Remarks text,st_wt_dt date,st_wt_t time,wt text,nd_wt_dt date,nd_wt_t time,ndwt text)''')
def show_data():
    con= sqlite3.connect('WBMS.txt')
    cur= con.cursor()
    cur.execute('''select * from WD''')
    for record in cur:
        print('Company Name :',str(record[0])+'\n')
        print('Address:',str(record[1])+'\n')
        print('Serial no:',str(record[2])+'\n')
        print('Customer Name:',str(record[3])+'\n')
        print('Material:',str(record[4])+'\n')
        print('Source:',str(record[5])+'\n')
        print('Destination:',str(record[6])+'\n')
        print('Remarks:',str(record[7])+'\n')
        print('1st weight date:',str(record[8])+'\n')
        print('1st weight time:',str(record[9])+'\n')
        print('1st weight:',str(record[10])+'\n')
        print('2nd weight date:',str(record[11])+'\n')
        print('2nd weight time:',str(record[12])+'\n')
        print('2nd weight:',str(record[13])+'\n')

def adde():           #ADDING DATA 
    CN1 = CN.get()
    Addr1 = Addr.get()
    mate1 = mate.get()
    Id1=Id.get()
    name1=name.get()
    Sorc1 = Sorc.get()
    Desti1 = Desti.get()
    rem1 = rema.get()
    cur.execute('''Insert into WD(Company_Name,Address,Serial_no,Customer_Name,Material,source,Destination,Remarks,st_wt_dt,st_wt_t,wt,nd_wt_dt,nd_wt_dt,ndwt)
        values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,)''',(CN1,Addr1,mate1,Id1,name1,Sorc1,Desti1,rem1,fx1,fx2,fn,sx1,sx2,sn,))
    con.commit()
    show_data()

    tkinter.messagebox.showinfo('Congratulations !!','Weighing Details successfully Added')

def upe():         #UPDATING DATA 
    CN1 = CN.get()
    Addr1 = Addr.get()
    mate1 = mate.get()
    Id1=Id.get()
    name1=name.get()
    Sorc1 = Sorc.get()
    Desti1 = Desti.get()
    rem1 = rema.get()
    cur.execute('''Update WD SET Name=? WHERE ID=?''',(name1,Id1))
    con.commit()
    show_data()
    tkinter.messagebox.showinfo('Congratulations !!','Weighing Details successfully updated')

def dele():
    Id1=Id.get()
    cur.execute('''Delete from WD where ID=?''',(Id1,))
    con.commit()
    tkinter.messagebox.showinfo('Congratulations !!','Weighing Details successfully Deleted')
    show_data()

def prnt():
    print(root)

def close():
    root.destroy()

def connect():
    connect_serial()

global fx1,fx2,fn
##n1=datetime.datetime.now()
##fx1=n1.strftime("%x")
##fx2=n1.strftime("%X")
##fn="{received_data}"print(fn)
def gro():
    #time.sleep(10)
    n1=datetime.datetime.now()
    fx1=n1.strftime("%x")
    fx2=n1.strftime("%X")
    print(fx1,fx2)
    Da1=tk.Label(Cus_frame,text=fx1,font=('Bold',15)).grid(row=10,column=1)
    Ta1=tk.Label(Cus_frame,text=fx2,font=('Bold',15)).grid(row=10,column=2)
    try:
        global fn
        fn=f"{received_data}"
        fn=''.join(char for char in fn if not char.isalpha())
        print(fn)
        w1 = tk.Label(Cus_frame,text=fn,font=('Bold',15)).grid(row=10,column=3)
    except:
        tk.messagebox.showinfo("Alert","Connect First")
    #disconnect_serial()


global sx1,sx2,sn
##n2=datetime.datetime.now()
##sx1=n2.strftime("%x")
##sx2=n2.strftime("%X")
##sn="{received_data}"
def gro2():
    n2=datetime.datetime.now()
    sx1=n2.strftime("%x")
    sx2=n2.strftime("%X")
    print(sx1,sx2)
    Da1=tk.Label(Cus_frame,text=sx1,font=('Bold',15)).grid(row=11,column=1)
    Ta1=tk.Label(Cus_frame,text=sx2,font=('Bold',15)).grid(row=11,column=2)
    try:
        global sn
        sn=f"{received_data}"
        sn=''.join(char for char in sn if not char.isalpha())
        w2 = tk.Label(Cus_frame,text=sn,font=('Bold',15)).grid(row=11,column=3)
    except:
        tk.messagebox.showinfo("Alert","Connect First")
    #disconnect_serial()

##w1 = StringVar()
##w2 = StringVar()
##w11 = w1.get()
##w22 = w2.get()
##long(w11)
##long(w22)

def net():
    int(fn)
    int(sn)
    if (fn > sn):
        nw = fn - sn
    else:
        nw = sn - fn
        ntwt=tk.Label(Cus_frame,text=nw,font=('Bold',15)).grid(row=12,column=3)
        
Cus_frame=tk.Frame(main_frame)
lb = tk.Label(Cus_frame,text="Weighing Details",padx=5,pady=10,
              font=('Bold',30)).grid(row=0,column=0,columnspan=4)
Compname=tk.Label(Cus_frame,text="Company Name",font=('Bold',15)).grid(row=1,column=1)
CompName=tk.Entry(Cus_frame,textvariable=CN,font=('Bold',15)).grid(row=1,column=2,columnspan=2)
addre=tk.Label(Cus_frame,text="Address",font=('Bold',15)).grid(row=2,column=1)
Addre=tk.Entry(Cus_frame,textvariable=Addr,font=('Bold',15)).grid(row=2,column=2,columnspan=2)
Cus_ID=tk.Label(Cus_frame,text="Serial no",font=('Bold',15)).grid(row=3,column=1)
Cus_id=tk.Entry(Cus_frame,textvariable=Id,font=('Bold',15)).grid(row=3,column=2,columnspan=2)
Cus_Name=tk.Label(Cus_frame,text="Customer Name",font=('Bold',15)).grid(row=4,column=1)
Cus_name=tk.Entry(Cus_frame,textvariable=name,font=('Bold',15)).grid(row=4,column=2,columnspan=2)
mat=tk.Label(Cus_frame,text="Material",font=('Bold',15)).grid(row=5,column=1)
Mat=tk.Entry(Cus_frame,textvariable=mate,font=('Bold',15)).grid(row=5,column=2,columnspan=2)
so=tk.Label(Cus_frame,text="Source",font=('Bold',15)).grid(row=6,column=1)
So=tk.Entry(Cus_frame,font=('Bold',15),textvariable=Sorc).grid(row=6,column=2,columnspan=2)
des=tk.Label(Cus_frame,font=('Bold',15),text="Destination").grid(row=7,column=1)
Des=tk.Entry(Cus_frame,font=('Bold',15),textvariable=Desti).grid(row=7,column=2,columnspan=2)
Re=tk.Label(Cus_frame,text="Remarks",font=('Bold',15)).grid(row=8,column=1)
re=tk.Entry(Cus_frame,font=('Bold',15),textvariable=rema).grid(row=8,column=2,columnspan=2)


D1=tk.Label(Cus_frame,text="Date",font=('Bold',15)).grid(row=9,column=1)
T1=tk.Label(Cus_frame,text="Time",font=('Bold',15)).grid(row=9,column=2)
W1=tk.Label(Cus_frame,text="Weight(KGS)",font=('Bold',15)).grid(row=9,column=3)
G1=tk.Button(Cus_frame,text="1st weight",padx=3.49,font=('Bold',15),command=gro).grid(row=10,column=0)
Da1=tk.Entry(Cus_frame,font=('Bold',10)).grid(row=10,column=1)
Ta1=tk.Entry(Cus_frame,font=('Bold',10)).grid(row=10,column=2)
w1 = tk.Entry(Cus_frame,font=('Bold',10)).grid(row=10,column=3)

tare1=tk.Button(Cus_frame,text="2nd weight",font=('Bold',15),command=gro2).grid(row=11,column=0)
Da1=tk.Entry(Cus_frame,font=('Bold',10)).grid(row=11,column=1)
Ta1=tk.Entry(Cus_frame,font=('Bold',10)).grid(row=11,column=2)
w2 = tk.Entry(Cus_frame,font=('Bold',10)).grid(row=11,column=3)
        

NTWT=tk.Button(Cus_frame,text="NET WT",padx=11,font=('Bold',15),command=net).grid(row=12,column=0)
ntwt=tk.Entry(Cus_frame,font=('Bold',10)).grid(row=12,column=3)

save=tk.Button(Cus_frame,text="Save",font=('Bold',15)
                  ,command=adde).grid(row=13,column=0)
Modify=tk.Button(Cus_frame,text="Modify",font=('Bold',15)
                  ,command=upe).grid(row=13,column=1)
dele=tk.Button(Cus_frame,text="Delete",font=('Bold',15)
                  ,command=dele).grid(row=13,column=2)
prnt=tk.Button(Cus_frame,text="Print",font=('Bold',15)
                  ,command=prnt).grid(row=13,column=3)
cl=tk.Button(Cus_frame,text="Close",font=('Bold',15)
                  ,command=close).grid(row=13,column=4)
Cus_frame.grid()

ser = None
baud_rate = None
after_id = None

def connect_serial():
    textbox.delete("1.0", tk.END)
    global ser
    global after_id
    port = port_var.get()
    baud_rate = baud_rate_var.get()
    try:
        ser = serial.Serial(port, baud_rate)
        #textbox.insert(tk.END, f"Connected to {port} at {baud_rate} baud\n")
        after_id = textbox.after(100, read_serial)  # Start reading data after 100ms
    except serial.SerialException as e:
        textbox.insert(tk.END, f"Failed to connect to {port}: {str(e)}\n")

def disconnect_serial():
    global ser
    global after_id
    if ser is not None and ser.is_open:
        ser.close()
        textbox.after_cancel(after_id)  # Cancel the recurring calls
        after_id = None
       # textbox.insert(tk.END, "Serial port disconnected\n")
        ser = None
        baud_rate = None
global n
def read_serial():
    global ser
    global after_id
    try:
        if ser is not None and ser.is_open and ser.in_waiting > 0:
            global received_data
            received_data= ser.readline().decode().strip()
            textbox.insert(tk.END, f"{received_data}\n")
            n=f"{received_data}"
            n=''.join(char for char in n if not char.isalpha())
            #print(n)
            textbox.see(tk.END)  # Scroll to the end of the text
    except serial.SerialException as e:
        textbox.insert(tk.END, f"Error reading from serial port: {str(e)}\n")
    after_id = textbox.after(100, read_serial)  # Schedule the next read after 100ms

# Create the main Tkinter window
window = tk.Frame(root)
#window.title("Serial Monitor V0.3")

# COM ports Selection
top_frame = tk.Frame(window)
top_frame.pack(padx=5, pady=5)

port_label = tk.Label(top_frame, text="Port:")
port_label.pack(side=tk.LEFT)

available_ports = [port.device for port in serial.tools.list_ports.comports()]
port_var = tk.StringVar(window)
port_var.set(available_ports[0] if available_ports else "")
port_dropdown = tk.OptionMenu(top_frame, port_var, *available_ports)
port_dropdown.pack(side=tk.LEFT)

# Baud rate selection
top_frame.pack(padx=5, pady=5)
baud_rate_label = tk.Label(top_frame, text="Baud Rate:")
baud_rate_label.pack(side=tk.LEFT)

baud_rate_var = tk.StringVar(window)
baud_rate_var.set("9600")
baud_rate_dropdown = tk.OptionMenu(top_frame, baud_rate_var, "300", "600", "1200", "2400", "4800", "9600", "19200", "38400", "115200", "230400", "500000", "1000000")
baud_rate_dropdown.pack(side=tk.LEFT)


# Buttons top_frame, Connect button
connect_button = tk.Button(top_frame, text="Connect ", command=connect_serial)
connect_button.pack(side=tk.LEFT, padx=5, pady=5)
# Disconnect button
disconnect_button = tk.Button(top_frame, text="Disconnect ", command=disconnect_serial)
disconnect_button.pack(side=tk.LEFT, padx=5, pady=5)

# Textbox
textbox = scrolledtext.ScrolledText(window, height=5, width=15,font=('Bold',35))
textbox.pack(padx=10, pady=5)

connect_serial()

window.pack()



root.mainloop()



