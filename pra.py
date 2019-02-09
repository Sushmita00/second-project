import datetime
from stegano import lsb
import time

#hide the message inside the image
#hide=lsb.hide('2.png','Hello')
#msg_time=time.asctime().replace(' ','')
#msg_time=msg_time.replace(':','')
#save the image with new name
#hide.save('secret-pic'+msg_time+'.png')

#to get the secret message from the image
#msg=lsb.reveal('secret-pic.png')
#print th msg
#print(msg)

hide=lsb.hide('2.png',"what r u doing")
hide.save('secret_msg.png')

msg=lsb.reveal('secret_msg.png')
print(" the Secret message is ",msg)



'''

from tkinter import  *
from tkinter import  filedialog
root=Tk()
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
upload_button=Button(root,text="Upload File",foreground="red",command=lambda : select_image(path_entry.get()))
upload_button.grid(row=3,column=2,padx=10,pady=10)
reset_but=Button(root,text="Reset",foreground="blue",command=lambda: clear_field(path_entry))
reset_but.grid(row=3,column=3,padx=10,pady=10)
root.mainloop()

from tkinter import  *
from tkinter import  filedialog
from tkinter import ttk

root=Tk()
tabcontrol = ttk.Notebook(root)
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text="encoding the image")
tabcontrol.add(tab2, text="dEcoding the image")
Label(tab1,text="this is tab1").pack()
Label(tab2,text="this is tab2").pack()
tabcontrol.pack()
'''
root.mainloop()