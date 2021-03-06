from tkinter import*
root=Tk()
root.title('Subscriber Management System')
root.geometry('1800x800')
myLabel = Label(root, text='SUBSCRIBER MANAGEMENT SYSTEM', font=('times new roman',25, 'bold'), fg='red', bg='black', bd=4, relief=RAISED)
myLabel.pack(side=TOP, fill=X)
#manage frame
my_frame = Frame(root, bd=4, relief = RIDGE, bg= 'BLACK')
my_frame.place(x=10, y= 80, width=600, height=650)
#manage title
M_title=Label(my_frame,text='MANAGE SUBSCRIBER', font=('Arial Black',20, 'bold'), fg='white', bg='black', bd=4, relief=RAISED)
M_title.grid(row=0, columnspan=2, padx=20, pady=20)
#labels
lbl_id=Label(my_frame, text='CUSTOMER ID:', font=('Arial Black',16,'bold'),fg='white',bg='black')
lbl_id.grid(row=1, column=0, padx=20, pady=10, sticky=W)
id_entry=Entry(my_frame,font=('Arial Black',16,'bold'))
id_entry.grid(row=1, column=1, padx=20, pady=10, sticky=W)
lbl_name=Label(my_frame, text='NAME:', font=('Arial Black',16,'bold'),fg='white',bg='black')
lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky=W)
name_entry=Entry(my_frame,font=('Arial Black',16,'bold'))
name_entry.grid(row=2, column=1, padx=20, pady=10, sticky=W)
lbl_package=Label(my_frame, text='PACKAGE:', font=('Arial Black',16,'bold'),fg='white',bg='black')
lbl_package.grid(row=4, column=0, padx=20, pady=10, sticky=W)
def show():
    myLabel= Label(root, text=clicked.get()).pack()
clicked = StringVar()
clicked.set('10 Mbps')
drop = OptionMenu(root, clicked,'10 Mbps','20 Mbps', '30 Mbps','40 Mbps','50 Mbps')
drop.pack(anchor='nw', pady=250, padx=250, ipadx=98)
# myButton = Button(root, text='gender', command=show) .pack()
#myButton.grid(row=4, column=1, padx=10, pady=10, sticky=W)
lbl_contact=Label(my_frame, text='CONTACT NO.:', font=('Arial Black',16,'bold'),fg='WHITE',bg='BLACK')
lbl_contact.grid(row=5, column=0, padx=20, pady=10,ipady=20, sticky=W)
contact_entry=Entry(my_frame,font=('Arial Black',16,'bold'))
contact_entry.grid(row=5, column=1, padx=20, pady=10, sticky=W)
lbl_address=Label(my_frame, text='ADDRESS:', font=('Arial Black',16,'bold'),fg='WHITE',bg='BLACK')
lbl_address.grid(row=6, column=0, padx=20, pady=10, sticky=W)
add_entry=Entry(my_frame,font=('Arial Black',16,'bold'))
add_entry.grid(row=6, column=1, padx=20, pady=10, sticky=W)
lbl_username=Label(my_frame, text='USERNAME:', font=('Arial Black',16,'bold'),fg='WHITE',bg='BLACK')
lbl_username.grid(row=6, column=0, padx=20, pady=0, sticky=W)
username_entry=Entry(my_frame,font=('Arial Black',16,'bold'))
username_entry.grid(row=6, column=1, padx=20, pady=10, sticky=W)
lbl_email=Label(my_frame, text='EMAIL:', font=('Arial Black',16,'bold'),fg='WHITE',bg='BLACK')
lbl_email.grid(row=7, column=0, padx=20, pady=10, sticky=W)
email_entry=Entry(my_frame,font=('Arial Black',16,'bold'))
email_entry.grid(row=7, column=1, padx=20, pady=10, sticky=W)
lbl_duration=Label(my_frame, text='DURATION:', font=('Arial Black',16,'bold'),fg='white',bg='black')
lbl_duration.grid(row=8, column=0, padx=20, pady=45, sticky=W)
def show():
    myLabel= Label(root, text=clicked.get()) #.pack()
clicked = StringVar()
clicked.set('MONTHLY')
drop = OptionMenu(root, clicked, 'YEARLY','HALF-YEARLY', 'QUATERLY','MONTHLY','WEEKLY')
# drop.grid(row=5, column=1, padx= 20, pady=10, ipadx=20, sticky=W)
drop.pack(anchor='nw',pady=10,padx=238,ipadx=98, ipady=5)
# Button Frame
btn_frame=Frame(root,bd = 4, relief=RIDGE, bg='BLACK')
btn_frame.place(x=40, y=650, width=500)
add_btn=Button(btn_frame, text='ADD', width=13, height=2, fg='BLACK', bg='WHITE')
add_btn.grid(row=9, column=0, padx=10, pady=10)
update_btn=Button(btn_frame, text='UPDATE', width=13, height=2, fg='BLACK', bg='WHITE')
update_btn.grid(row=9, column=1, padx=10, pady=10)
delete_btn=Button(btn_frame, text='DELETE', width=13, height=2, fg='BLACK', bg='WHITE')
delete_btn.grid(row=9, column=2, padx=10, pady=10)
clear_btn=Button(btn_frame, text='CLEAR', width=13, height=2, fg='BLACK', bg='WHITE')
clear_btn.grid(row=9, column=3, padx=10, pady=10)
#detail frame
Details_frame = Frame(root, bd=4, relief = RIDGE, bg= 'BLACK')
Details_frame.place(x=620, y= 80, width=900, height=650)
search_lbl=Label(Details_frame, text='SEARCH BY:', font=('Arial Black',16,'bold'),fg='WHITE',bg='BLACK')
search_lbl.grid(row=1, column=0, padx=20, pady=10, sticky=W)
def show():
    myLabel= Label(Details_frame, text=clicked.get()).pack()
clicked = StringVar()
clicked.set('')
drop = OptionMenu(Details_frame, clicked,'CUSTOMER ID', 'NAME','USERNAME','CONTACT NO.','USERNAME')
drop.grid(row=1, column=1, padx= 15, pady=10, ipadx=5, sticky=W)
search_entry=Entry(Details_frame,font=('Arial Black',16,'bold'))
search_entry.grid(row=1, column=2, padx=3, pady=10,ipadx=5, sticky=W)
search_btn=Button(Details_frame, text='SEARCH', width=13, height=2, fg='BLACK', bg='WHITE')
search_btn.grid(row=1, column=3, padx=10, pady=10)
show11_btn=Button(Details_frame, text='SHOW ALL', width=13, height=2, fg='BLACK', bg='WHITE')
show11_btn.grid(row=1, column=4, padx=10, pady=10)
#table frame
table_frame = Frame(Details_frame, bd=4, relief = RIDGE, bg= 'WHITE')
table_frame.place(x=10, y= 70, width=865, height=550)
SVBar = Scrollbar(table_frame)
SVBar.pack(side=RIGHT, fill="y")
SHBar = Scrollbar(table_frame, orient=HORIZONTAL)
SHBar.pack(side=BOTTOM, fill="x")

root.mainloop()