from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3 as sq
def add_run(label):
    try:
        connection=sq.connect("Run_detail.db")
        cursor=connection.cursor()
        cursor.execute('''create table IF NOT EXISTS run_detail_real(
                       bus_id int(5),
                       running_date varchar(10),
                       seat_available int
        )''')
        cursor.execute("INSERT INTO run_detail_real(bus_id,running_date,seat_available)VALUES(?,?,?)",
                       (int(bus_id.get()),running_date.get(),int(running_seat.get())))
        connection.commit()
        messagebox.showinfo("Run Entry", "Run record added ")
        label=Label(root,text=(int(bus_id.get()),running_date.get(),int(running_seat.get())))
        label.grid(row=4,column=7)
    except Exception as es:
        print(f"Exception {es}")
    finally:
        connection.close()
    return label
def delete_run(label):
    try:
        connection=sq.connect("Run_detail.db")
        cursor=connection.cursor()
        cursor.execute("DELETE FROM run_detail_real WHERE bus_id= ?",(int(bus_id.get()),))
        connection.commit()
        messagebox.showinfo("Route Entry", "Route record deleted ")
        label.destroy()
        label=Label(root,text=(int(bus_id.get()),running_date.get(),int(running_seat.get())))
        label.grid(row=4,column=7)
    except Exception as es:
        print(f"Exception {es}")
    finally:
        connection.close()
    return label
fontFam="Arial"
root=Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
img=Image.open("starbus.png")
img = img.resize((225,175 ))
img = ImageTk.PhotoImage(img) 
Label(root,image=img).grid(padx=550,row=0,columnspan=50)
Label(root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=1,columnspan=50,pady=15)
Label(root,text="Add Bus Running Details",fg="green4",font=(("Arial",30,"bold"))).grid(row=2,columnspan=50,pady=15)
Label(root,text="Bus Id",font=((fontFam,12,'bold'))).grid(row=3,column=5)
bus_id=StringVar()
Entry(root,textvariable=bus_id).grid(row=3,column=6)
Label(root,text="Running Date",font=((fontFam,12,'bold'))).grid(row=3,column=7)
running_date=StringVar()
Entry(root,textvariable=running_date).grid(row=3,column=8)
Label(root,text="Seat Available",font=((fontFam,12,'bold'))).grid(row=3,column=9)
running_seat=StringVar()
Entry(root,textvariable=running_seat).grid(row=3,column=10)
label=None
label=Button(root,text="Add Run",command=lambda:add_run(label),fg="black",bg="spring green",font="Arial 10 bold")
label.grid(row=3,column=15,padx=10)
label=Button(root,text="Delete Run",command=lambda:delete_run(label),fg="red",bg="spring green",font="Arial 10 bold")
label.grid(row=3,column=18,padx=10)
house=Image.open("House.png")
house = house.resize((75,50 ))
house = ImageTk.PhotoImage(house) 
Button(root,image=house,command=root.bell,bg="spring green").grid(row=3,column=21)
root.mainloop()