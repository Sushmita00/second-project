
reg=input(" Do you want to register as y/n")
name='Sushmita'
if reg=="n":
   #name=input("enter the name")
   name = input("enter the name")
   while name.isdigit() == True or len(name) < 4:
       name = input("please enter the name")
       print("Name:", name)
   age = input("enter the age")
   while age.isalpha() == True or int(age) < 18 or int(age) > 40:
       age = input("please enter the age")
   print("Age:", age)
   place=input("enter the place")
   print("PLACE;",place)
   passw = 1234
   password = input("enter the password")
   while passw == password:
       password = input("enter the correct password")
   print("PASSWORD:", password)

#print("Hello",name,"Now,lets start secret conversation ")
else:
    passw = 1234
    password = input("enter the password")
    while passw == password:
        password = input("enter the correct password")
    print("PASSWORD:", password)

print("Hello",name,"Now,lets start secret conversation ")

from tkinter import  *
from tkinter import  filedialog
from tkinter import ttk
from tkinter import messagebox as mBox

root=Tk()

def browsefunction():
    import re
    filename = filedialog.askopenfilename()
    if re.search(r'\.jpg$',filename):
        entry1.config(text="Path to the File :" + filename)
        entry1.insert(0, filename)

    else:
        print("not accepted")
        mBox.showwarning("warning message box", "ENTER THE IMAGES ONLY")

def select_image(path):
    print(path)
def clear_field(widget):
    widget.delete(0,END)


root.title("Never give up")
root.resizable(0,0)
root.geometry("400x300")
tabControl=ttk.Notebook(root)
tab1=ttk.Frame(tabControl)
root.config(background='green')


tabControl.add(tab1,text="Encoding the image")
tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text="Decoding the image")
tabControl.pack(expand=1,fill="both")


browsebutton = Button(tab1, text="Browse to Path",width=20,height=1, command= lambda : browsefunction())
browsebutton.place(relx=0.60,rely=0.4)

button=Button(tab1,text="enter the image").place(relx=0.07,rely=0.09)
entry1 = Entry(tab1,width=30,borderwidth=2,relief="groove")
entry1.place(relx=0.35,rely=0.09)
entry1.config(font=('Times New Roman',12),)



upload_button=Button(tab1,text="Upload File",foreground="red",command=lambda : select_image(entry1.get()))
upload_button.place(relx=0.15,rely=0.40)
reset_but=Button(tab1,text="Reset",foreground="blue",command=lambda: clear_field(entry1))
reset_but.place(relx=0.40,rely=0.40)

button=Button(tab1,text=" message",foreground="green").place(relx=0.20,rely=0.65)
ent=Entry(tab1).place(relx=0.55,rely=0.65)
umessage=StringVar()
message=Entry(tab1,textvariable=umessage)
message.place(relx=0.55,rely=0.65)

import datetime as dt
from stegano import lsb
import time

#hide the message inside the image
hide=lsb.hide('fav.jpg','Hello')
msg_time=time.asctime().replace(' ','')
msg_time=msg_time.replace(':','')
#save the image with new name
hide.save('secret-pic'+msg_time+'.jpg')

#to get the secret message from the image
msg=lsb.reveal('secret-pic'+msg_time+'.jpg')
#print th msg
print(msg)
def show_details():
   answer=mBox.askyesno("Python Dual Choice Box", 'Are you sure you want to send message:')

button=Button(tab1,text="ENCODE",foreground="blue",command= show_details).place(relx=0.40,rely=0.80)


#tab2

def browsefunc():
    filename = filedialog.askopenfilename()
    path_entry2.config(text="Path to the File :" + filename)
    path_entry2.insert(0, filename)
def select_image(path):
    print(path)
def clear_field(widget):
    widget.delete(0,END)
browsebutton = Button(tab2, text="Browse to Path",width=20,height=1, command= lambda : browsefunc())
browsebutton.place(relx=0.60,rely=0.4)
button=Button(tab2,text="enter the image").place(relx=0.07,rely=0.09)

path_entry2 = Entry(tab2,width=30,borderwidth=2,relief="groove")
path_entry2.place(relx=0.35,rely=0.09)
path_entry2.config(font=('Times New Roman',12),)


reset_but=Button(tab2,text="Reset",foreground="blue",command=lambda: clear_field(path_entry2))
reset_but.place(relx=0.15,rely=0.40)




def show_details():
    answer = mBox.askyesno("Python Dual Choice Box", 'Are you sure you want to see message:')
    toplevel=Toplevel(tab2)
    Label(toplevel, text= umessage.get(), font=("", 20)).pack()
button=Button(tab2,text="DECODE",foreground="red",command=show_details).place(relx=0.40,rely=0.80)




root.mainloop()