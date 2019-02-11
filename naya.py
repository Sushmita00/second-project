
from tkinter import  *
from tkinter import  filedialog
from tkinter import ttk
root=Tk()
'''
#root=tk.Tk()
root.title("Never give up")
root.resizable(0,0)
root.geometry("300x150")
tabControl=ttk.Notebook(root)
tab1=ttk.Frame(tabControl)
root.config(background='green')


tabControl.add(tab1,text="Encoding the image")
tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text="Decoding the image")
tabControl.pack(expand=1,fill="both")


lab=Button(tab1,text="BROWSER",command=lambda :browsefunc()).grid(row=3,column=1,padx=10,pady=10)

path_entry = Entry(root,width=40,borderwidth=2,relief="groove").grid(row=2,column=1,padx=10,pady=10).config(font=('Times New Roman',12),)


lab=Button(tab1,text="SEND").place(relx=0.40,rely=0.80)

lab=Button(tab1,text="Enter the message").place(relx=0.03,rely=0.65)
ent=Entry(tab1).place(relx=0.55,rely=0.65)

button=Button(tab1,text="enter the image").place(relx=0.07,rely=0.09)
ent=Entry(tab2).place(relx=0.52,rely=0.09)

button=Button(tab1,text="UPDATE",foreground="red",command=lambda : select_image(path_entry.get()).grid(row=3,column=2,padx=10,pady=10)

button=Button(tab1,text="RESET",foreground="blue",command=lambda: clear_field(path_entry))
button.grid(row=3,column=3,padx=10,pady=10)

def browsefunc():
    filename = filedialog.askopenfilename()
    path_entry.config(text="Path to the File :" + filename)
    path_entry.insert(0, filename)
def select_image(path):
    print(path)
def clear_field(widget):
    widget.delete(0,END)

browsebutton = Button(root, text="Browse to Path",width=20,height=1, command= lambda : browsefunc())
browsebutton.grid(row=3,column=1,padx=10,pady=10)

path_entry = Entry(root,width=40,borderwidth=2,relief="groove")
path_entry.grid(row=2,column=1,padx=10,pady=10)
path_entry.config(font=('Times New Roman',12),)
upload_button=Button(root,text="Upload File",foreground="red",mand=lambda : select_image(path_entry.get()))
upload_button.grid(row=3,column=2,padx=10,pady=10)
reset_but=Button(root,text="Reset",foreground="blue",command=lambda: clear_field(path_entry))
reset_but.grid(row=3,column=3,padx=10,pady=1
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
msg=lsb.reveal('secret-pic.jpg')
#print th msg
print(msg)
'''

def _msgBox():
    mBox.showinfo('This is a Title','A python GUI created using tkinter:\n The year 2019')

root.mainloop()