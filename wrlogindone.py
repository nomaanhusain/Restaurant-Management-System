from tkinter import *
import os
def delete3():
    screen4.destroy()
     

    

def not_matched():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("Sucess")
    screen4.geometry("300x250")
    Label(screen4,text="Login Failed Check username or password").pack()
    Button(screen4,text="Ok",command=delete3).pack()



def reg_user():
    username_info=username.get()
    password_info=password.get()
    lsoffile = os.listdir()
    if username_info in lsoffile:
        Label(screen1, text = "User already exist").pack()
        raise Exception("Error")
    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info+"\n")
    file.close()

    username_entry.delete(0,END)#to clear entry fields
    password_entry.delete(0,END)
    Label(screen1,text="Registration Succesfull",fg="green").pack()

def log_user():
    username1=username_verify.get()
    password1=password_verify.get()
     
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
       file1=open(username1,"r")
       verify=file1.read().splitlines()
       print(type(verify))
       if password1 in verify:
           import wrms
    else:
        not_matched()

def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    
    username=StringVar()
    password=StringVar()
    Label(screen1, text = "Enter Details",bg='grey', width="300", height = "2").pack()
    Label(screen1, text = "").pack()
    Label(screen1,text = "Username").pack()
    username_entry = Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text = "Password").pack()
    password_entry = Entry(screen1,textvariable=password)
    password_entry.pack()
    Button(screen1, text ="Register", width = 10, height =1, command=reg_user).pack()
    
def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Enter login details").pack()
    Label(screen2, text ="").pack()

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()
    
    Label(screen2,text = "Username").pack()
    username_entry1=Entry(screen2,textvariable = username_verify)
    username_entry1.pack()
    Label(screen2,text = "Password").pack()
    password_entry1=Entry(screen2,textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text ="").pack()
    Button(screen2, text="Login",width=10,height=1,command=log_user).pack()
    

def main_screen():
    global screen
    screen= Tk()
    screen.geometry("300x250")
    screen.title('Restuarant Login')
    Label(text="Resturant Login",bg='grey', width="300", height = "2").pack()
    Label(text = "").pack()
    Button(text = "Login",height="2", width="30", command = login).pack()
    Label(text = "").pack()
    Button(text= "Register",height="2", width="30", command = register).pack()
    screen.mainloop()

main_screen()
