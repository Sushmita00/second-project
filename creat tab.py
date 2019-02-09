import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("Never give up")
tabControl=ttk.Notebook(root)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text="ENCODER")
tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text="DECODER")
tabControl.pack(expand=1,fill="both")
monty=ttk.LabelFrame(tab1,text='Monty python')
monty.grid(column=0,row=0,padx=8,pady=4)
ttk.Label(monty,text="enter the name:").grid(column=0,row=0)

sticky='W'
root.mainloop()