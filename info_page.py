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
Label(root,image=img).pack()
Label(root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).pack(pady=30)
Label(root,text="Created by: Raman Soni",fg="Dark Blue",font=(fontFam,20)).pack(pady=20)
Label(root,text="github: https://github.com/Ram22an",fg="Dark Blue",font=(fontFam,20)).pack(pady=20)
Label(root,text="linkedin: https://www.linkedin.com/in/raman-soni-09764524a",fg="Dark Blue",font=(fontFam,20)).pack(pady=20)
Label(root,text="Project based learing",fg="Dark Blue",font=(fontFam,20)).pack()
root.mainloop()
