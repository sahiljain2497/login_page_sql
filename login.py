from tkinter import *
import backend
import os

def Signup():
    global pwordE
    global nameE
    global roots
    
    roots = Tk()
    roots.title('signup')
    instruction = Label(roots,text='please enter your credentials\n')
    instruction.grid(row=0,column=0,sticky=E)
    
    nameL =Label(roots,text='New Username: ')
    pwordL = Label(roots,text='New Password: ')
    nameL.grid(row=1,column=0,sticky=W)
    pwordL.grid(row=2,column=0,sticky=W)
    
    nameE=Entry(roots)
    pwordE=Entry(roots,show='*')
    nameE.grid(row=1,column=1)
    pwordE.grid(row=2,column=1)
    signupButton=Button(roots,text='Signup',command=register_command)
    signupButton.grid(columnspan=2,sticky=W)
    roots.mainloop()
    
def register_command():
    backend.register(nameE.get(),pwordE.get())
    roots.destroy()
    
def Login():
    backend.connect()
    global nameEL
    global pwordEL
    global rootA
    
    rootA =Tk()
    rootA.title('Login')
    
    instruction = Label(rootA,text='Please login: ')
    instruction.grid(row=0,sticky=E)
    
    nameL =Label(rootA,text='Username: ')
    pwordL =Label(rootA,text='Passwrod: ')
    nameL.grid(row=1,column=0,sticky=W)
    pwordL.grid(row=2,column=0,sticky=W)
    
    nameEL=Entry(rootA)
    pwordEL=Entry(rootA,show='*')
    nameEL.grid(row=1,column=1)
    pwordEL.grid(row=2,column=1)
    
    loginB=Button(rootA,text='Login',command=Checklogin)
    loginB.grid(row=3,column=0,sticky=W)

    SignupB=Button(rootA,text='Signup',command=Signup)
    SignupB.grid(row=3,column=2,sticky=W)

    rootA.mainloop()
    
def Checklogin():
    validity=backend.search(str(nameEL.get()),str(pwordEL.get()))
    if validity== True:
        print('logged in')
    else:
        print('wrong uname or pass')
        
Login()
