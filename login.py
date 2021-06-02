import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
import os

root = Tk()
root.title('Login Page')
root.geometry("700x600")
root.resizable(0,0)
root.configure(bg="black")




# Creating User Entry
username_label = Label(root, bg="black", fg="white", text="Username: ", font=("Times New Roman", 20, "bold")).place(x=80, y=103)

username = Entry(root, width=30, borderwidth=10, fg="black", bg="white", font=("Times New Roman", 20, "bold"), justify=LEFT)
username.place(x=220, y=100)



# Creating Password Entry
password_label = Label(root, bg="black", fg="white", text="Password: ", font=("Times New Roman", 20, "bold")).place(x=80, y=183)

password = Entry(root, width=30, borderwidth=10, fg="white", bg="white", font=("Times New Roman", 20, "bold"), justify=LEFT)
password.config(show="*",fg="black")
password.place(x=220, y=180)



def login_successful():
    messagebox.showinfo("ADMIN","Welcome !")
    root.destroy()
    os.system("python main.py")


def try_login():
    conn = sqlite3.connect('registration.db')

    c = conn.cursor()

    c.execute("SELECT *, oid FROM login_data")
    records = c.fetchall()
    # Getting user login details from the login page
    name = username.get()
    pwd = password.get()
    # Loop through the results
    print_record = ''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[3]) + "\n"

        if record[0] != name or record[2] != pwd or record[3] != pwd:
            # login_unsuccessful
            continue
        elif record[0] == name and record[2] == pwd and record[3] == pwd:
            login_successful()
    conn.commit()
    conn.close()

def new_registration():
    root.destroy()
    reg_page = Tk()
    reg_page.title('Registration Page')
    reg_page.geometry("650x500")
    reg_page.resizable(0, 0)
    reg_page.configure(bg="black")
    # # Creating a database or connect to one
    conn = sqlite3.connect('registration.db')

    # Create Cursor
    c = conn.cursor()


    # # Create Table for storing registration details
    #
    # c.execute(""" CREATE TABLE login_data(
    #         user_name text,
    #         user_address text,
    #         user_pass text,
    #         user_confirm_pass text
    # )
    # """)
    # messagebox.showinfo("User Registration Table Created Successfully", "You can now add the data")

    # Creating text boxes
    new_reg_label = Label(reg_page, text="New Registration", font=("Times New Roman", 23, "bold"),fg='white', bg='black', bd=4, relief=RAISED).place(x=150, y=30)

    user_name_label = Label(reg_page, text="User Name:", font=("Times New Roman", 23, "bold"),bg="black",fg="white").place(x=30, y=110)

    user_name = Entry(reg_page, font=("Times New Roman", 23, "bold"))
    user_name.place(x=300, y=110)

    address_label = Label(reg_page, text="Address:", font=("Times New Roman", 21, "bold"),bg="black",fg="white").place(x=30, y=170)

    address = Entry(reg_page, font=("Times New Roman", 23, "bold"))
    address.place(x=300, y=170)

    password_label = Label(reg_page, text="Password:", font=("Times New Roman", 21, "bold"),bg="black",fg="white").place(x=30, y=230)

    password = Entry(reg_page, font=("Times New Roman", 23, "bold"))
    password.place(x=300, y=230)

    confirm_password_label = Label(reg_page, text="Confirm Password:", font=("Times New Roman", 21, "bold"),bg="black",fg="white").place(x=30,
                                                                                                                  y=290)

    confirm_password = Entry(reg_page, font=("Times New Roman", 23, "bold"))
    confirm_password.place(x=300, y=290)

    # Creating a  submit button for the database

    def register():
        # Create a database or connect to one
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()

        # Insert into table
        c.execute("INSERT INTO login_data VALUES (:user_name, :address, :password, :confirm_password)", {
            'user_name': user_name.get(),
            'address': address.get(),
            'password': password.get(),
            'confirm_password': confirm_password.get()
        })

        conn.commit()
        conn.close()

        user_name.delete(0, END)
        address.delete(0, END)
        password.delete(0, END)
        confirm_password.delete(0, END)

        messagebox.showinfo("User Data", "You are Good To GO!")
        reg_page.destroy()
        os.system("python login.py")

    # Creating a function for showing the records to check if the data is being stored

    def view_records():
        # Creating a database or connect to one
        conn = sqlite3.connect('registration.db')
        # Create Cursor
        c = conn.cursor()
        # Query of the databse
        c.execute("SELECT *, oid FROM login_data")
        records = c.fetchall()
        print(records)
        conn.commit()
        conn.close()

    # Creating a submit button
    register_btn = Button(reg_page, text="Register", font=("Times New Roman", 21, "normal"), command=register)
    register_btn.place(x=330, y=350)

    # View Record Button to test if the data is being stored
    show_record_btn = Button(text="Show Records", font=('Century Gothic', 20, 'normal'), command=view_records)
    show_record_btn.place(x=60, y=350)
    reg_page.mainloop()

# Creating Login Button
login_btn = Button(root, width=20, borderwidth=10, bg="white", text="Login", font=("Times New Roman", 22, "bold"),command=try_login )\
    .place(x=250, y=250)

new_user_reg_label = Button(root, width=20, borderwidth=10, bg="white", text="For New User", font=("Times New Roman", 22, "bold"), command=new_registration)\
    .place(x=250, y=350)

root.mainloop()