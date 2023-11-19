from tkinter import *
from PIL import ImageTk,Image
import sqlite3 as sq
fontFam="Arial"
def printticket(phone_no):
    connection1 = sq.connect("customer_detail.db")
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM customer_detail_real WHERE mobile_no = ? LIMIT 1", (int(phone_no.get()),))
    detail_of_customer = cursor1.fetchall()
    print(detail_of_customer)
    name_of_customer=detail_of_customer[0][0]
    no_of_seat=detail_of_customer[0][1]
    mobile_no=detail_of_customer[0][2]
    age_of_customer=detail_of_customer[0][3]
    gender_of_customer=detail_of_customer[0][4]
    total_fare=detail_of_customer[0][5]
    frame = Frame(root, bd=3, relief=SUNKEN)
    frame.grid(row=5,columnspan=50, padx=20, pady=20)
    label = Label(frame, text=f"Passenger:- {name_of_customer}",font="Arial 12 bold")
    label.grid(row=0, column=0, padx=10, pady=10)
    label = Label(frame, text=f"Gender:- {gender_of_customer}",font="Arial 12 bold")
    label.grid(row=0, column=1, padx=10, pady=10)
    label = Label(frame, text=f"No of seat :- {no_of_seat}",font="Arial 12 bold")
    label.grid(row=1, column=0, padx=10, pady=10)
    label = Label(frame, text=f"Phone:- {mobile_no}",font="Arial 12 bold")
    label.grid(row=1, column=1, padx=10, pady=10)
    label = Label(frame, text=f"Age :- {age_of_customer}",font="Arial 12 bold")
    label.grid(row=2, column=0, padx=10, pady=10)
    label = Label(frame, text=f"Fare :- Rs {total_fare*no_of_seat}",font="Arial 12 bold")
    label.grid(row=2, column=1, padx=10, pady=10)
    label = Label(frame, text=f"*Total amount Rs {total_fare*no_of_seat} to be paid at time of boarding of bus",font="Arial 10")
    label.grid(row=3, columnspan=10, padx=10, pady=10)
root=Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
img=Image.open("starbus.png")
img = img.resize((225,175 ))
img = ImageTk.PhotoImage(img) 
Label(root,image=img).grid(padx=550,row=1,columnspan=50)
Label(root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=2,columnspan=50,pady=20)
Label(root,text="Check Your Booking",fg="green4",bg="lawn green",font="Arial 24 bold").grid(padx=550,row=3,columnspan=50,pady=20)
Label(root,text="Enter Your mobile no :-",font="Arial 12 bold").grid(row=4,column=23)
phone_no=StringVar()
phone_no1=Entry(root,textvariable=phone_no).grid(row=4,column=24)
Button(root,command=lambda:printticket(phone_no),text="Check booking").grid(row=4,column=25)
root.mainloop()