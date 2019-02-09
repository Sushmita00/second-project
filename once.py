from tkinter import  *
from tkinter import  filedialog
from tkinter import ttk
root=Tk()

def browsefunction():
    filename = filedialog.askopenfilename()
    entry1.config(text="Path to the File :" + filename)
    entry1.insert(0, filename)
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

button=Button(tab1,text=" message").place(relx=0.20,rely=0.65)
ent=Entry(tab1).place(relx=0.55,rely=0.65)

button=Button(tab1,text="ENCODE").place(relx=0.40,rely=0.80)

'''
import datetime as dt
from stegano import lsb
import time

#hide the message inside the image
hide=lsb.hide('2.png','Hello')
msg_time=time.asctime().replace(' ','')
msg_time=msg_time.replace(':','')
#save the image with new name
hide.save('secret-pic'+msg_time+'.png')

#to get the secret message from the image
msg=lsb.reveal('secret-pic.png')
#print th msg
print(msg)

'''

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


upload_button=Button(tab2,text="Upload File",foreground="red",command=lambda : select_image(path_entry2.get()))
upload_button.place(relx=0.15,rely=0.40)
reset_but=Button(tab2,text="Reset",foreground="blue",command=lambda: clear_field(path_entry2))
reset_but.place(relx=0.40,rely=0.40)

button=Button(tab2,text=" message box").place(relx=0.20,rely=0.65)
ent=Entry(tab2).place(relx=0.55,rely=0.65)
button=Button(tab2,text="DECODE").place(relx=0.40,rely=0.80)
#lab=Button(tab2,text="ENCODE").place(relx=0.60,rely=0.80)


root.mainloop()