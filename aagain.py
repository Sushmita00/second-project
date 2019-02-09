import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
root=tk.Tk()
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
lab=tk.Button(tab1,text="enter the image").place(relx=0.07,rely=0.09)
ent=tk.Entry(tab1).place(relx=0.52,rely=0.09)
uentertheimage=tk.StringVar()
entertheimage=tk.Entry(root,textvariable=uentertheimage)

lab=tk.Button(tab1,text="UPDATE").place(relx=0.15,rely=0.40)
uupdate=tk.StringVar()
update=tk.Entry(root,textvariable=uupdate)

lab=tk.Button(tab1,text="RESET").place(relx=0.45,rely=0.40)
ureset=tk.StringVar()
reset=tk.Entry(root,textvariable=ureset)
def browsefunc():
    filename = filedialog.askopenfilename()
    path_entry.config(text="Path to the File :" + filename)
    path_entry.insert(0, filename)
def select_image(path):
    print(path)
def clear_field(widget):
    widget.delete(0,END)
path_entry =tk. Entry(root, width=40, borderwidth=2, relief="groove")
#path_entry.grid(row=2, column=1, padx=10, pady=10)
path_entry.config(font=('Times New Roman', 12), )
upload_button=tk.Button(root,text="Upload File",foreground="red",command=lambda : select_image(path_entry.get()))
#upload_button.grid(row=3,column=2,padx=10,pady=10)
#reset_but=tk.Button(root,text="Reset",foreground="blue",command=lambda: clear_field(path_entry))
#reset_but.grid(row=3,column=3,padx=10,pady=10)
#browsebutton = Button(root, text="Browse to Path",width=20,height=1, command= lambda : browsefunc())
#browsebutton.grid(row=3,column=1,padx=10,pady=10)


lab=tk.Button(tab1,text="BROWSER",command=lambda :browsefunc()).place(relx=0.70,rely=0.4)

lab=tk.Button(tab1,text="SEND").place(relx=0.40,rely=0.80)
lab=tk.Button(tab1,text="Enter the message").place(relx=0.03,rely=0.65)
ent=tk.Entry(tab1).place(relx=0.55,rely=0.65)

lab=tk.Button(tab2,text="enter the image").place(relx=0.07,rely=0.09)
ent=tk.Entry(tab2).place(relx=0.52,rely=0.09)

lab=tk.Button(tab2,text="UPDATE").place(relx=0.15,rely=0.40)

lab=tk.Button(tab1,text="RESET",foreground="blue",command=lambda: clear_field(path_entry)).grid(row=3,column=3,padx=10,pady=10)
#reset_but.grid(row=3,column=3,padx=10,pady=10)
#lab=tk.Button(tab2,text="BROWSER").place(relx=0.70,rely=0.40)


#lab=tk.Button(tab2,text=" message").place(relx=0.20,rely=0.65))
#ent=tk.Entry(tab2).place(relx=0.55,rely=0.65)

#tabControl.pack()
root.mainloop()