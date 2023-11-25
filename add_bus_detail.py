from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3 as sq
def add_bus_detail():
    # print(int(bus_id.get()),bus_type.get(),int(bus_capacity.get()),int(bus_fare.get()),int(bus_op_id.get()),int(bus_rout_id.get()))
    try:
        connection=sq.connect("Add_bus_detail.db")
        cursor=connection.cursor()
        cursor.execute('''create table IF NOT EXISTS Add_bus_detail_real(
                       bus_id int(5),
                       bus_type varchar(10),
                       capacity int,
                       Fare int,
                       operator_id int(5),
                       rout_id int
        )''')
        cursor.execute("INSERT INTO Add_bus_detail_real(bus_id,bus_type,capacity,Fare,operator_id,rout_id) VALUES(?,?,?,?,?,?)"
                       ,(int(bus_id.get()),bus_type.get(),int(bus_capacity.get()),int(bus_fare.get()),int(bus_op_id.get()),int(bus_rout_id.get())))
        connection.commit()
        messagebox.showinfo("Bus Entry", "Bus record added ")
        label=Label(root,text=(int(bus_id.get()),bus_type.get(),int(bus_capacity.get()),int(bus_fare.get()),int(bus_op_id.get()),int(bus_rout_id.get())))
        label.grid(row=4,column=7)
    except Exception as es:
        print(f"Exception {es}")
    finally:
        connection.close()
    return label
def edit_bus_detail(label):
    try:
        connection=sq.connect("Add_bus_detail.db")
        cursor=connection.cursor()
        cursor.execute("UPDATE Add_bus_detail_real SET bus_type=?,capacity=?,Fare=?,rout_id=? WHERE bus_id=? AND operator_id=?",
                       (bus_type.get(), int(bus_capacity.get()), int(bus_fare.get()), int(bus_rout_id.get()), int(bus_id.get()), int(bus_op_id.get())))
        connection.commit()
        messagebox.showinfo("Bus Entry", "Bus record edited ")
        label.destroy()
        label=Label(root,text=(int(bus_id.get()),bus_type.get(),int(bus_capacity.get()),int(bus_fare.get()),int(bus_op_id.get()),int(bus_rout_id.get())))
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
Label(root,text="Add Bus Details",fg="green4",font=(("Arial",30,"bold"))).grid(row=2,columnspan=50,pady=15)
Label(root,text="Bus id",font=((fontFam,12,'bold'))).grid(row=3,column=1)
bus_id=StringVar()
Entry(root,textvariable=bus_id).grid(row=3,column=2)
Label(root,text="Bus Type",font=((fontFam,12,'bold'))).grid(row=3,column=3)
bus_type=StringVar()
bus_type.set("Bus Type")
option=["AC_3X2","AC_2X2","nonAC_3X2","nonAC_2X2"]
OptionMenu(root,bus_type,*option).grid(row=3,column=4)
Label(root,text="Capacity",font=((fontFam,12,'bold'))).grid(row=3,column=5)
bus_capacity=StringVar()
Entry(root,textvariable=bus_capacity).grid(row=3,column=6)
Label(root,text="Fare Rs",font=((fontFam,12,'bold'))).grid(row=3,column=7)
bus_fare=StringVar()
Entry(root,textvariable=bus_fare).grid(row=3,column=8)
Label(root,text="Operator ID",font=((fontFam,12,'bold'))).grid(row=3,column=9)
bus_op_id=StringVar()
Entry(root,textvariable=bus_op_id).grid(row=3,column=10)
Label(root,text="Rout ID",font=((fontFam,12,'bold'))).grid(row=3,column=11)
bus_rout_id=StringVar()
Entry(root,textvariable=bus_rout_id).grid(row=3,column=12)
label=Button(root,text="Add",command=add_bus_detail,fg="black",bg="spring green",font="Arial 10 bold")
label.grid(row=3,column=16,padx=10)
Button(root,text="Edit",command=lambda:edit_bus_detail(label),fg="black",bg="spring green",font="Arial 10 bold").grid(row=3,column=17,padx=10)
house=Image.open("House.png")
house = house.resize((75,50 ))
house = ImageTk.PhotoImage(house) 
Button(root,image=house,command=root.bell,bg="spring green").grid(row=3,column=18)
root.mainloop()