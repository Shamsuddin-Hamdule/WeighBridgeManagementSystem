from tkinter import *
from tkinter import ttk
import tkinter as tk
import webbrowser
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import datetime
#from pynput.keyboard import Key,Listener

now=datetime.datetime.now()
n1=datetime.datetime.now()
fx1=n1.strftime("%x")
fx2=n1.strftime("%X")

root = tk.Tk()
window_width = 700
window_height = 600

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

main_frame = tk.Frame(root,highlightbackground="black"
                      ,highlightthickness=2)
image_path = "th.jfif"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(main_frame, image=photo,width=490).pack()


image_path1 = "wb1.jpeg"
image1 = Image.open(image_path1)
photo1 = ImageTk.PhotoImage(image1)
image_label1 = tk.Label(main_frame, image=photo1,height=280,width=470).pack()

main_frame.pack()
#main_frame.pack_propagate(False)
main_frame.configure(height=300,width=400)

# Dummy user credentials
valid_credentials = {
    "Admin":"admin",
    "Guest": "yes",
}

Username = StringVar()
Password = StringVar()

def validate_login():
    username = Username.get()
    password = Password.get()

    if username in valid_credentials and valid_credentials[username] == password:
        messagebox.showinfo("Login Successful", "Welcome on Board, {}".format(username))
        open_link()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_link():
    subprocess.run(["python", "main"])

Login_Frame = tk.Frame(root)
Login_Frame.pack()
#Login_Frame.pack_propagate(False)
Login_Frame.configure(width=100,height=300)

def create_login_page():

    date=tk.Label(Login_Frame,text="Date :",font=('Bold',15)).grid(row=1,column=2)
    datee=tk.Label(Login_Frame,text=fx1,font=('Bold',15)).grid(row=1,column=3)

    label_username = tk.Label(Login_Frame, text="Username:",font=('Bold',15))
    label_username.grid(row=2,column=2)
    entry_username = tk.Entry(Login_Frame,textvariable=Username,font=('Bold',15))
    entry_username.grid(row=2,column=3)

    label_password = tk.Label(Login_Frame, text="Password:",font=('Bold',15))
    label_password.grid(row=3,column=2)
    entry_password = tk.Entry(Login_Frame, show="*",textvariable=Password,font=('Bold',15))
    entry_password.grid(row=3,column=3)

    login_button = tk.Button(Login_Frame, text="Login", command=validate_login,font=('Bold',15))
    login_button.grid(row=5,column=2,columnspan=4,pady=10)

    root.mainloop()

#with Listener(on_press = lo) as listener:
 #   listener.join()

if __name__ == "__main__":
    create_login_page()

