from tkinter import *
from tkinter import ttk
#def digitdeleteTextDisplay():
 #   global operator
  #  operator=""
   # text_Input.set("")
#button=Button(root,text="Reset",command=digitdeleteTextDisplay)
#button.place(relx=0.45,rely=0.40)

root=Tk()
root.title("tkinter window")
root.resizable(0,0)
button=Button(root,text="select the picture")
button.place(relx=0.01,rely=0.09)
ent=Entry(root)
ent.place(relx=0.52,rely=0.09)
root.config(background='green')
button=Button(root,text="Browser")
button.place(relx=0.70,rely=0.30)
#def digitdeleteTextDisplay():
 #   global operator
  #  operator=""
   # text_Input.set("")
#delete = Button(root, fg="black", font=("arial", 10, "bold"), text="reset",
 #                   command=digitdeleteTextDisplay, bg="Brown").place(relx=0.45,rely=0.40)



button=Button(root,text="Reset",command=lambda:digitdeleteTextDisplay("Reset"))
button.place(relx=0.45,rely=0.40)


button=Buttt="update")
button.place(relx=0.15,rely=0.40)on(root,tex

#button=Button(root,text="Reset")
#button.place(relx=0.45,rely=0.40)

button=Button(root,text="send")
button.place(relx=0.40,rely=0.80)

button=Button(root,text="enter the message")
button.place(relx=0.01,rely=0.65)
ent=Entry(root)
ent.place(relx=0.55,rely=0.65)

uenterthemessage=StringVar()
enterthemessage=ttk.Entry(root,width=12, textvariable=uenterthemessage)
#nameEntered.grid(column=1, row=1)
#enterthemessageEntered.focus()

root.mainloop()