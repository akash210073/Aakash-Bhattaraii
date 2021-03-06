import os
from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import sqlite3
# from tabulate import tabulate
import sys

root=tk.Tk()
root.title('SUBSCRIBER MANAGEMENT SYSTEM')
root.geometry('1700x700')

# Creating Table
# Creating a database or connect to one
conn = sqlite3.connect('aakash.db')

# Create Cursor
c = conn.cursor()

# Create Table for storing registration details
# c.execute(""" CREATE TABLE store_data(
#         subscriber_userid text,
#         subscriber_name text,
#         subscriber_email text,
#         subscriber_contact text,
#         subscriber_package text,
#         subscriber_address text
# )
# """)
# messagebox.showinfo("User Registration Table Created Successfully", "You can now add the data")

myLabel = Label(root, text='SUBSCRIBER MANAGEMENT SYSTEM', font=('Calibri',30, 'bold'), fg='white', bg='black', bd=4, relief=RAISED)
myLabel.pack(side=TOP, fill=X)

#manage frame
my_frame = Frame(root, bd=4, relief = RIDGE, bg= 'black')
my_frame.place(x=20, y= 80, width=550, height=600)

#manage title
M_title=Label(my_frame,text='MANAGE SUBSCRIBER', font=('Calibri',30, 'bold'), fg='white', bg='black', bd=4, relief=RAISED)
M_title.grid(row=0, columnspan=2, padx=20, pady=20)

#labels
lbl_userid=Label(my_frame, text='USER ID', font=('Calibri',18,'bold'),fg='white',bg='black')
lbl_userid.grid(row=1, column=0, padx=20, pady=10, sticky=W)

userid_entry=Entry(my_frame,font=('Calibri',18,'bold'))
userid_entry.grid(row=1, column=1, padx=20, pady=10, sticky=W)

lbl_name=Label(my_frame, text='NAME', font=('Calibri',18,'bold'),fg='white',bg='black')
lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky=W)

name_entry=Entry(my_frame,font=('Calibri',18,'bold'))
name_entry.grid(row=2, column=1, padx=20, pady=10, sticky=W)

lbl_email=Label(my_frame, text='EMAIL', font=('Calibri',18,'bold'),fg='white',bg='black')
lbl_email.grid(row=3, column=0, padx=20, pady=10, sticky=W)

email_entry=Entry(my_frame,font=('Calibri',18,'bold'))
email_entry.grid(row=3, column=1, padx=20, pady=10, sticky=W)

lbl_gender=Label(my_frame, text='GENDER', font=('Calibri',18,'bold'),fg='white',bg='black')
lbl_gender.grid(row=4, column=0, padx=20, pady=10, sticky=W)

def show():
    myLabel= Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set('male')

drop = OptionMenu(root, clicked,'male','female', 'other')
drop.pack(anchor='nw',pady=315,padx=188,ipadx=108)

# myButton = Button(root, text='gender', command=show) .pack()
#myButton.grid(row=4, column=1, padx=10, pady=10, sticky=W)

lbl_contact=Label(my_frame, text='CONTACT', font=('Calibri',18,'bold'),fg='white',bg='black')
lbl_contact.grid(row=5, column=0, padx=20, pady=10, sticky=W)

contact_entry=Entry(my_frame,font=('Calibri',18,'bold'))
contact_entry.grid(row=5, column=1, padx=20, pady=10, sticky=W)

lbl_package=Label(my_frame, text='PACKAGE', font=('Calibri',18,'bold'),fg='white',bg='black')
lbl_package.grid(row=6, column=0, padx=20, pady=10, sticky=W)

package_entry=Entry(my_frame,font=('Calibri',18,'bold'))
package_entry.grid(row=6, column=1, padx=20, pady=10, sticky=W)

lbl_address=Label(my_frame, text='ADDRESS', font=('Calibri',18,'bold'),fg='white',bg='black')
lbl_address.grid(row=7, column=0, padx=20, pady=10, sticky=W)

add_entry=Entry(my_frame,font=('Calibri',18,'bold'))
add_entry.grid(row=7, column=1, padx=20, pady=10, sticky=W)


def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('aakash.db')

    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO store_data VALUES (:userid_entry, :name_entry, :email_entry, :contact_entry, :package_entry, :add_entry)",{
        'userid_entry' : userid_entry.get(),
        'name_entry': name_entry.get(),
        'email_entry': email_entry.get(),
        'contact_entry': contact_entry.get(),
        'package_entry': package_entry.get(),
        'add_entry': add_entry.get()
    })

    messagebox.showinfo("User Data", "YOUR DATA IS REGISTERED")

    conn.commit()

    conn.close()

    userid_entry.delete(0, END)
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    contact_entry.delete(0, END)
    package_entry.delete(0, END)
    add_entry.delete(0, END)


def delete():
    con1 = sqlite3.connect("aakash.db")

    cur1 = con1.cursor()

    cur1.execute("DELETE from store_data WHERE subscriber_user_id = " + userid_entry.get())

    messagebox.showinfo("Yes", "Deleted Successfully")

    con1.commit()
    con1.close()

def update():
    # Creating a database or connect to one
    con1 = sqlite3.connect('aakash.db')

    # Create cursor
    cur1 = con1.cursor()

    record_id = userid_entry.get()

    cur1.execute(""" UPDATE store_data SET
            subscriber_user_id = :sub_user_id,
            subscriber_name = :sub_name,
            subscriber_email = :sub_email,
            subscriber_contact = :sub_contact,
            subscriber_package = :sub_dob,
            subscriber_address = :sub_address
            WHERE subscriber_user_id = :subscriber_user_id""",
            {'sub_roll_no': subscriber_userid_editor.get(),
            'sub_name': subscriber_name_editor.get(),
            'sub_email': subscriber_email_editor.get(),
            'sub_contact': subscriber_contact_editor.get(),
            'sub_package': subscriber_package_editor.get(),
            'sub_address': subscriber_address_editor.get(),
            'subscriber_user_id': record_id
            }
    )
    con1.commit()
    con1.close()
    # Updating all the data and closing window
    messagebox.showinfo("UPDATE","Your data has been updated!")
    editor.destroy()

def edit():
    global editor

    editor = Tk()
    editor.title('Update Data')
    editor.geometry('500x500')
    editor.config(bg="silver")

    # Create a database or connect to one
    con1 = sqlite3.connect('aakash.db')

    # Create cursor
    cur1 = con1.cursor()

    record_id = userid_entry.get()

    # Query of the database
    cur1.execute("SELECT * FROM sto_data WHERE subscriber_user_id=" + record_id)

    records = cur1.fetchall()

    # Creating global variable for all text boxes
    global subscriber_userid_editor
    global subscriber_name_editor
    global subscriber_email_editor
    global subscriber_contact_editor
    global subscriber_package_editor
    global subscriber_address_editor

    # Creating texy boxes
    subscriber_userid = Label(editor, font=("Calibri", 14, "bold"), width=18, text="Subscriber User Id ")
    subscriber_userid.place(x=10, y=50)

    subscriber_userid_editor = Entry(editor, font=("Calibri", 14, "bold"), width=18)
    subscriber_userid_editor.place(x=260, y=50)

    subscriber_name = Label(editor, font=("Calibri", 14, "bold"), width=18, text="Subscriber Name")
    subscriber_name.place(x=10, y=100)

    subscriber_name_editor = Entry(editor, font=("Calibri", 14, "bold"), width=18)
    subscriber_name_editor.place(x=260, y=100)

    subscriber_email = Label(editor, font=("Calibri", 14, "bold"), text="Subscriber Email", width=18)
    subscriber_email.place(x=10, y=150)

    subscriber_email_editor = Entry(editor, font=("Calibri", 14, "bold"), width=18)
    subscriber_email_editor.place(x=260, y=150)

    subscriber_contact = Label(editor, font=("Calibri", 14, "bold"), text="Subscriber Contact", width=18)
    subscriber_contact.place(x=10, y=200)

    subscriber_contact_editor = Entry(editor, font=("Calibri", 14, "bold"), width=18)
    subscriber_contact_editor.place(x=260, y=200)

    subscriber_dob = Label(editor, font=("Calibri", 14, "bold"), width=18, text="Subscriber package")
    subscriber_dob.place(x=10, y=250)

    subscriber_package_editor = Entry(editor, font=("Calibri", 14, "bold"), width=18)
    subscriber_package_editor.place(x=260, y=250)

    subscriber_address = Label(editor, font=("Calibri", 14, "bold"), width=18, text="Subscriber Address")
    subscriber_address.place(x=10, y=300)

    subscriber_address_editor = Entry(editor, font=("Calibri", 14, "bold"), width=18)
    subscriber_address_editor.place(x=260, y=300)

    save_btn = Button(editor, font=("Calibri", 14, "bold"), text="Save", command=update)
    save_btn.place(x=200, y=400)

    # Loop through the results
    for record in records:
        subscriber_userid_editor.insert(0, record[0])
        subscriber_name_editor.insert(0, record[1])
        subscriber_email_editor.insert(0, record[2])
        subscriber_contact_editor.insert(0, record[3])
        subscriber_package_editor.insert(0, record[4])
        subscriber_address_editor.insert(0, record[5])


# Button Frame
btn_frame=Frame(root,bd = 4, relief=RIDGE, bg='grey')
btn_frame.place(x=30, y=600, width=500)

add_btn=Button(btn_frame, text='ADD', width=13, height=2,font=("Times New Roman", 8, "bold"), fg='black', bg='yellow', command=submit)
add_btn.grid(row=0, column=0, padx=10, pady=10, ipadx=20)

update_btn=Button(btn_frame, text='UPDATE', width=13, height=2, font=("Times New Roman", 8, "bold"), fg='black', bg='yellow', command=edit)
update_btn.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

delete_btn=Button(btn_frame, text='DELETE', width=13, height=2, font=("Times New Roman", 8, "bold"), fg='black', bg='yellow', command=delete)
delete_btn.grid(row=0, column=2, padx=10, pady=10, ipadx=20)


#detail frame
Details_frame = Frame(root, bd=4, relief = RIDGE, bg= 'grey')
Details_frame.place(x=600, y= 80, width=900, height=600)

search_lbl=Label(Details_frame, text='INFORMATIONS OF SUBSCRIBER', font=('Calibri", 14,',20,'bold'),fg='black',bg='grey')
search_lbl.grid(row=1, column=0, padx=20, pady=10, sticky=W)

# Function for viewing data
def View():
    con1 = sqlite3.connect("aakash.db")
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM store_data")
    rows = cur1.fetchall()
    for row in rows:
        Subscriber_table.insert("", tk.END, values=row)
    con1.close()


show11_btn=Button(Details_frame, text='SHOW ALL', width=13, height=2,font=("Calibri", 10, "bold"), fg='white', bg='black', command=View)
show11_btn.grid(row=1, column=4, padx=10, pady=10, ipadx=20)

# Table frame
Table_frame= Frame(Details_frame , bd=4, relief=RIDGE, bg='grey')
Table_frame.place(x=15, y=60, width=865, height=490)


scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(Table_frame, orient=VERTICAL)

Subscriber_table= ttk.Treeview(Table_frame,columns=("userid", "name", "email", "contact", "package", "address"),
                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=Subscriber_table.xview)
scroll_y.config(command=Subscriber_table.yview)


Subscriber_table.heading("userid", text="UserId")
Subscriber_table.column("userid", width=100)
Subscriber_table.heading("name", text="Name")
Subscriber_table.column("name", width=100)
Subscriber_table.heading("email", text="Email")
Subscriber_table.column("email", width=100)

Subscriber_table.heading("contact", text="Contact")
Subscriber_table.column("contact", width=100)
Subscriber_table.heading("package", text="Package")
Subscriber_table.column("package", width=100)
Subscriber_table.heading("address", text="Address")
Subscriber_table.column("address", width=100)
Subscriber_table['show'] = 'headings'
Subscriber_table.pack(fill=BOTH, expand=1)

def endProgam():
    raise SystemExit
    sys.exit()


exit_btn=Button(root, text='EXIT', width=13, height=2, font=("Times New Roman", 10, "bold"), fg='white', bg='black', command = endProgam)
exit_btn.place(x=1393, y=635 )

mainloop()