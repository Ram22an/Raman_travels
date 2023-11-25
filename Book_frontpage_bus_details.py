from tkinter import *
from tkinter.messagebox import askyesno
from PIL import ImageTk,Image
import sqlite3 as sq
fontFam="Arial"
root=Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
img=Image.open("starbus.png")
img = img.resize((225,175 ))
img = ImageTk.PhotoImage(img) 
Label(root,image=img).grid(padx=550,row=0,columnspan=50)
Label(root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=1,columnspan=50,pady=20)
Label(root,text="Add New Details To Database",fg="green4",font=(("Arial",30,"bold"))).grid(row=2,columnspan=50,pady=25)
Button(root,text="New Operator",command=root.bell,bg="pale green",font=((fontFam,15))).grid(row=3,column=15,pady=10)
Button(root,text="New Bus",command=root.bell,bg="tomato",font=((fontFam,15))).grid(row=3,column=20,pady=10)
Button(root,text="New Route",command=root.bell,bg="SteelBlue1",font=((fontFam,15))).grid(row=3,column=25,pady=10)
Button(root,text="New Run",command=root.bell,bg="MistyRose3",font=((fontFam,15))).grid(row=3,column=30,pady=10)
root.mainloop()