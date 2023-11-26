from tkinter import *
from PIL import ImageTk,Image
fontFam="Arial"
root=Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
img=Image.open("starbus.png")
img = img.resize((225,175 ))
img = ImageTk.PhotoImage(img) 
Label(root,image=img).grid(padx=550,row=1,columnspan=20)
Label(root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=2,columnspan=20,pady=40)
Button(root,text="SEAT BOOKING",command=root.bell,font=f"{fontFam} 20 bold",bg="lime green").grid(padx=100,row=3,column=1,pady=50)
Button(root,text="CHECK BOOKED SEAT",command=root.bell,font=f"{fontFam} 20 bold",bg="lime green").grid(padx=100,row=3,column=2,pady=50)
Button(root,text="ADD BUS DETAIL",command=root.bell,font=f"{fontFam} 20 bold",bg="lime green").grid(padx=100,row=3,column=3,pady=50)
Label(root,text="For Admin Only",fg="red",font=f"{fontFam} 15 bold").grid(row=4,column=3)
root.mainloop()