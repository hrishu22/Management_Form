from tkinter import *
import os
from tkinter import messagebox
screen=Tk()
screen.title("Management Area")
screen.geometry('749x468')
img=PhotoImage(file='witch.png')
bg=Canvas(screen, width=749, height=468)
bg.pack()
bgpic=Label(screen,image=img)
bgpic.place(x=0, y=0)
def button1():
    global filename1
    nam=name.get()
    pa=str(passvar.get())
    use=str(uservar.get())
    gen=str(gendervar.get())
    random=str(c.get())
    filename1 = "username.txt"
    filename2="extra.txt"
    with open(filename1, 'a') as f:
        f.write("\n"+use+","+pa)

        f.close()
    with open(filename2,'a') as f:
        f.write(gen)
        f.write(random)
        f.close()
        print(use,pa)
    messagebox.showinfo("Registration Successful","Thanks for Registering with us")
def button2():
    us=(user4.get())
    passq=(pass4.get())
    file=open("username.txt",'r').readlines()
    for i in file:
        a,b=i.split(",")

    if us==a:
        print("username matched")
    else:
        messagebox.showinfo("Error","user not found")
    if passq==b:
        print("password matched")
    else:
        messagebox.showinfo("Error","Password Mismatched")
    if us==a and passq==b:
        messagebox.showinfo("Success","Login Successfull!!!")
def login():
    global user4
    global pass4
    global login
    login=Toplevel(screen)
    login.geometry('300x250')
    login.title("Login-Window")
    user4=StringVar()
    pass4=StringVar()
    username=Label(login,font=font,text='UserName').place(x=20,y=50)
    uservar=Entry(login,textvariable=user4).place(x=160,y=60)
    passwrd=Label(login,font=font,text='Password').place(x=20,y=90)
    passvar = Entry(login,textvariable=pass4,show='*').place(x=160, y=90)
    button=Button(login,text='Login',command=button2).place(x=200,y=120)
def register():
    global name
    global uservar
    global passvar
    global gendervar
    global c
    global signup
    signup=Toplevel(screen)
    signup.geometry('300x320')
    signup.title("Registration-Window")
    name=StringVar()
    uservar=StringVar()
    passvar=StringVar()
    gendervar=IntVar()
    c=StringVar()
    na=Label(signup,font=font,text='Name').place(x=20,y=50)
    name1=Entry(signup,textvariable=name).place(x=160,y=60)
    user1=Label(signup,font=font,text='Username').place(x=20,y=100)
    user1entry= Entry(signup,textvariable=uservar).place(x=160, y=100)
    passw= Label(signup, font=font, text='Password').place(x=20, y=140)
    passq1 = Entry(signup,textvariable=passvar,show='*').place(x=160, y=140)
    gender=Radiobutton(signup,text='Male',variable=gendervar,value=1).place(x=150,y=160)
    gender1=Radiobutton(signup,text='Female',variable=gendervar,value=2).place(x=210,y=160)
    country=Label(signup,text='Country',font=font).place(x=20,y=200)
    list=['India','US','UK','Germany']
    droplist=OptionMenu(signup,c,*list)
    droplist.config(width=20)
    c.set('Select Your Country')
    droplist.place(x=150,y=200)
    button2 = Button(signup, text='Register',command=button1).place(x=150, y=250)
font=('verdana',18)
text=Label(screen,font=font, text="Register/Login").place(x=200,y=50)
login=Button(screen,font=font, text="Login", command=login, bg="#cfdac8",fg="#6a492b").place(x=250,y=190)
signup=Button(screen,font=font, text="Register",command=register, bg="#74c7b8",fg="#6a492b").place(x=230,y=260)
screen.mainloop()