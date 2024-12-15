from tkinter import *
import re
import tkinter.constants as tk

from email_message import send_email
from whatsapp_message import send_message

win = Tk()



def users_window():
    users_win = Toplevel()
    users_win.geometry("400x600")
    Label(users_win,text="User information",font=("Arial",15)).pack()

    with open("files.txt") as file:
        for i in file.readlines():
            name = i.replace("\n","")
            Button(users_win, text=f"{name}'s information", command=lambda: info_window(name)).pack(pady=10)


win.title("Information Software")

win.geometry("600x500")


lb_name = Label(win, text="Name:")
lb_lastname = Label(win, text="Lastname:")
lb_birth = Label(win, text="Birthday (MM/DD/YYYY):")
lb_country = Label(win, text="Country:")
lb_email = Label(win, text="Email:")
lb_number = Label(win, text="Phone number (+584125030478):")

text_name = Entry(win)
text_lastname = Entry(win)
text_birth = Entry(win)
text_country = Entry(win)
text_email = Entry(win)
text_number = Entry(win)

succes = Frame()
T_succes = Label(succes,text="Information saved succesfully", fg="green")
T_succes.pack_forget()

T_email = Frame(win)

E_email = Label(T_email, text= "Error entering email", fg="red")
E_email.pack_forget()

T_number = Frame(win)

E_number = Label(T_number, text= "Error entering number", fg="red")
E_number.pack_forget()

T_birth = Frame(win)

E_birth = Label(T_birth, text= "Error entering date", fg="red")
E_birth.pack_forget()

Label(text="Register information",font=("Arial",15)).pack()
succes.pack()
lb_name.pack()
text_name.pack()

lb_lastname.pack()
text_lastname.pack()

lb_birth.pack()
T_birth.pack()
text_birth.pack()

lb_country.pack()
text_country.pack()

lb_email.pack()
T_email.pack()
text_email.pack()

lb_number.pack()
T_number.pack()
text_number.pack()

def clear():
    text_name.delete(0,"end")
    text_lastname.delete(0,"end")
    text_birth.delete(0,"end")
    text_country.delete(0,"end")
    text_email.delete(0,"end")
    text_number.delete(0,"end")

def save():
    valid1 = valid2 = valid3 = False
    email = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', text_email.get())
    number = re.match(r'\+\d{12}', text_number.get())
    date = re.match(r'^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(19|20)\d{2}$',text_birth.get())
    if email:
        E_email.pack_forget()

        T_email.config(height=1)
        valid1 = True
    else:
        E_email.pack()

    if number:
        E_number.pack_forget()

        T_number.config(height=1)
        valid2 = True
    else:
        E_number.pack()

    if date:
        E_birth.pack_forget()

        T_birth.config(height=1)
        valid3 = True
    else:
        E_birth.pack()

    if valid3 and valid1 and valid2:
        
        user = text_email.get()
        user_name = user.split("@")[0]
        with open("files.txt","a") as file:
            file.write(user_name)
        
        with open("text/" + user_name + ".txt", "w") as file:
            file.writelines(
                [
                    text_name.get() + "\n",
                    text_lastname.get() + "\n",
                    text_birth.get() + "\n",
                    text_country.get() + "\n",
                    text_email.get() + "\n",
                    text_number.get() + "\n",
                ]
            )
        T_succes.pack()
        T_succes.after(3000,T_succes.pack_forget)
        succes.after(3000,lambda:succes.config(height=1))

        send_message(text_number.get())
        
        send_email(text_email.get(),text_name.get())
        valid1 = valid2 = valid3 = False
        

def info_window(id):
    info_win = Toplevel()

    def update():
        valid1 = valid2 = valid3 = False
        email = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', text_email.get())
        number = re.match(r'\+\d{12}', text_number.get())
        date = re.match(r'^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(19|20)\d{2}$',text_birth.get())
        if email:
            E_email.pack_forget()

            T_email.config(height=1)
            valid1 = True
        else:
            E_email.pack()

        if number:
            E_number.pack_forget()

            T_number.config(height=1)
            valid2 = True
        else:
            E_number.pack()

        if date:
            E_birth.pack_forget()

            T_birth.config(height=1)
            valid3 = True
        else:
            E_birth.pack()

        if valid3 and valid1 and valid2:
            
            user = text_email.get()
            user_name = user.split("@")[0]
            
            with open("text/" + user_name + ".txt", "w") as file:
                file.writelines(
                    [
                        text_name.get().replace("\n","") + "\n",
                        text_lastname.get().replace("\n","") + "\n",
                        text_birth.get().replace("\n","") + "\n",
                        text_country.get().replace("\n","") + "\n",
                        text_email.get().replace("\n","") + "\n",
                        text_number.get().replace("\n","") + "\n",
                    ]
                )
            valid1 = valid2 = valid3 = False
            T_succes.pack()
            T_succes.after(3000,T_succes.pack_forget)
            succes.after(3000,lambda:succes.config(height=1))
    

    def clear():
        text_name.delete(0,"end")
        text_lastname.delete(0,"end")
        text_birth.delete(0,"end")
        text_country.delete(0,"end")
        text_email.delete(0,"end")
        text_number.delete(0,"end")
        T_succes.pack_forget()
        succes.config(height=1)

    with open(f"text/{id}.txt") as file:

        name,lastname,birth,country,email,number=file.readlines()

        info_win.geometry("600x500")

        succes = Frame(info_win)
        T_succes = Label(succes,text="Information updated succesfully", fg="green")
        T_succes.pack_forget()

        lb_name = Label(info_win, text="Name:")
        lb_lastname = Label(info_win, text="Lastname:")
        lb_birth = Label(info_win, text="Birthday (MM/DD/YYYY):")
        lb_country = Label(info_win, text="Country:")
        lb_email = Label(info_win, text="Email:")
        lb_number = Label(info_win, text="Phone number (+584125030478):")

        text_name = Entry(info_win)
        text_lastname = Entry(info_win)
        text_birth = Entry(info_win)
        text_country = Entry(info_win)
        text_email = Entry(info_win)
        text_number = Entry(info_win)
        
        text_name.insert(string=name,index=0)
        text_lastname.insert(string=lastname,index=0)
        text_birth.insert(string=birth,index=0)
        text_country.insert(string=country,index=0)
        text_email.insert(string=email,index=0)
        text_number.insert(string=number,index=0)
        
        Label(info_win,text="Update information",font=("Arial",15)).pack()
        succes.pack()
        T_email = Frame(info_win)

        E_email = Label(T_email, text= "Error entering email", fg="red")
        E_email.pack_forget()

        T_number = Frame(info_win)

        E_number = Label(T_number, text= "Error entering number", fg="red")
        E_number.pack_forget()

        T_birth = Frame(info_win)

        E_birth = Label(T_birth, text= "Error entering date", fg="red")
        E_birth.pack_forget()

        lb_name.pack()
        text_name.pack()

        lb_lastname.pack()
        text_lastname.pack()

        lb_birth.pack()
        T_birth.pack()
        text_birth.pack()

        lb_country.pack()
        text_country.pack()

        lb_email.pack()
        T_email.pack()
        text_email.pack()

        lb_number.pack()
        T_number.pack()
        text_number.pack()

        Button(info_win,text="update info", command=update, font=('Helvetica bold',10)).pack(pady=7)
        Button(info_win,text="Clear", command=clear, font=('Helvetica bold',10)).pack(pady=7)




Button(win,text="Save info", command=save, font=('Helvetica bold',10)).pack(pady=7)
Button(win,text="Clear", command=clear, font=('Helvetica bold',10)).pack(pady=7)
Button(win,text="Users", command=users_window, font=('Helvetica bold',10)).pack(pady=7)



win.mainloop()