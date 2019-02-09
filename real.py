from tkinter import *
from tkinter import ttk
def digitdeleteTextDisplay():
   global operator
   operator=""
   text_Input.set("")
root=Tk()
root.title("tkinter window")
root.resizable(0,0)
operator=""
text_Input=StringVar()


digit6=Button(root,fg="black",font=("arial",10,"bold"),text="enter the message",command=lambda:digitClick("enter the message"),bg="Brown").place(relx=0.45,rely=0.40)
textDisplay=Entry(root,font=("arial",10,"bold"),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)

#digit7=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="7",command=lambda:digitClick(7),bg="Brown",bd=10).grid(row=1,column=1)
#digit8=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="8",command=lambda:digitClick(8),bg="Brown",bd=10).grid(row=1,column=2)
#digit9=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="9",command=lambda:digitClick(9),bg="Brown",bd=10).grid(row=1,column=3)
#digit4=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="4",command=lambda:digitClick(4),bg="Brown",bd=10).grid(row=2,column=0)
#digit5=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="5",command=lambda:digitClick(5),bg="Brown",bd=10).grid(row=2,column=1)
#subtraction=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="-",command=lambda:digitClick("-"),bg="Brown",bd=10).grid(row=2,column=2)
#addition=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="+",command=lambda:digitClick("+"),bg="Brown",bd=10).grid(row=2,column=3)
#digit2=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="2",command=lambda:digitClick(2),bg="Brown",bd=10).grid(row=3,column=0)
#digit3=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="3",command=lambda:digitClick(3),bg="Brown",bd=10).grid(row=3,column=1)
#multiply=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="*",command=lambda:digitClick("*"),bg="Brown",bd=10).grid(row=3,column=2)
#divide=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="/",command=lambda:digitClick("/"),bg="Brown",bd=10).grid(row=3,column=3)
#digit0=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="0",command=lambda:digitClick("0"),bg="Brown",bd=10).grid(row=4,column=0)
#digit1=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="1",command=lambda:digitClick("1"),bg="Brown",bd=10).grid(row=4,column=1)
#delete=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="D",command=digitdeleteTextDisplay,bg="Brown",bd=10).grid(row=4,column=2)
#equalto=Button(root,padx=16,pady=16,fg="black",font=("arial",20,"bold"),text="=",command= digitEqualinput,bg="Brown",bd=10).grid(row=4,column=3)

root.mainloop()