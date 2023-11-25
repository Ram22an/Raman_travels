from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3 as sq
def add_route(label):
    try:
        connection=sq.connect("Route_detail.db")
        cursor=connection.cursor()
        cursor.execute('''create table IF NOT EXISTS Add_route_detail(
                       route_id int(5),
                       station_name varchar(20),
                       station_id int(5)
        )''')
        cursor.execute("INSERT INTO Add_route_detail(route_id,station_name,station_id)VALUES(?,?,?)",
                       (int(route_id.get()),route_station_name.get(),int(route_station_id.get())))
        connection.commit()
        messagebox.showinfo("Route Entry", "Route record added ")
        label=Label(root,text=(int(route_id.get()),route_station_name.get(),int(route_station_id.get())))
        label.grid(row=4,column=7)
    except Exception as es:
        print(f"Exception {es}")
    finally:
        connection.close()
    return label
def delete_route(label):
    try:
        connection=sq.connect("Route_detail.db")
        cursor=connection.cursor()
        cursor.execute("DELETE FROM Add_route_detail Where route_id=? OR station_id=? ",(int(route_id.get()),int(route_station_id.get())))
        connection.commit()
        messagebox.showinfo("Route Entry", "Route record deleted ")
        label.destroy()
        label=Label(root,text=(int(route_id.get()),route_station_name.get(),int(route_station_id.get())))
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
Label(root,text="Add Bus Route Details",fg="green4",font=(("Arial",30,"bold"))).grid(row=2,columnspan=50,pady=15)
Label(root,text="Route Id",font=((fontFam,12,'bold'))).grid(row=3,column=5)
route_id=StringVar()
Entry(root,textvariable=route_id).grid(row=3,column=6)
Label(root,text="Station Name",font=((fontFam,12,'bold'))).grid(row=3,column=7)
route_station_name=StringVar()
Entry(root,textvariable=route_station_name).grid(row=3,column=8)
Label(root,text="Station Id",font=((fontFam,12,'bold'))).grid(row=3,column=9)
route_station_id=StringVar()
Entry(root,textvariable=route_station_id).grid(row=3,column=10)
label=None
label=Button(root,text="Add Route",command=lambda:add_route(label),fg="black",bg="spring green",font="Arial 10 bold")
label.grid(row=3,column=15,padx=10)
label=Button(root,text="Delete Route",command=lambda:delete_route(label),fg="red",bg="spring green",font="Arial 10 bold")
label.grid(row=3,column=18,padx=10)
house=Image.open("House.png")
house = house.resize((75,50 ))
house = ImageTk.PhotoImage(house) 
Button(root,image=house,command=root.bell,bg="spring green").grid(row=3,column=21)
root.mainloop()