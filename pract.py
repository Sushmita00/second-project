import tkinter as tk
import tkinter as ttk
root=tk.Tk()
root.title("give your best")
root.resizable(0,0)
#adding a label
ttk.Label(root,text="A Label").grid(column=0,row=0)
#modifying adding a label
aLabel=ttk.Label(root,text="A Label")
aLabel.grid(column=0,row=0)
def Click_me():
    action.config(text="*** I HAVE BEEN CLICKED***")
    aLabel.config(foreground="red")
#adding a button
action=ttk.Button(root,text="CLICK ME!", command= Click_me)
action.grid(column=1,row=1)

#modification button click function
def Click_me():
    action.config(text='Hello' + name.get())
    action.grid(column=1,row=1)
#chamge your label
ttk.Label(root,text="Enter a name:").grid(column=0,row=0)
#adding textbox entry winge
name=tk.StringVar()
nameEntered=ttk.Entry(root,width=12, textvariable=name)
nameEntered.grid(column=1, row=1)
'''
#action.config(state='disable')
ttk.Label(root,text='choose a number:').grid(column=1,row=0)
number=tk.StringVar()
numberchosen=ttk.Combobox(root,width=12,textvariable=number)
numberchosen['values']=(1,2,3,5,6,8,9,70,46.457)
numberchosen.grid(column=1,row=1)
numberchosen.current(0)
'''
root.mainloop()


