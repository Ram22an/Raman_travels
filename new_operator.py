from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3 as sq
def Addopertor():#operatorid,operatorname,operatoraddress,operatorphone,operatoremail):
    try:
        messagebox.showinfo("Operator Entry", "Operator record added ")
        connection = sq.connect("opertor_detail.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS opertor_details_real (
                    op_id int(5) , 
                    op_name varchar(20),
                    op_address varchar(20),
                    op_phone int(10),
                    op_email varchar(20)
                    )''')
        cursor.execute("INSERT INTO opertor_details_real (op_id,op_name,op_address,op_phone,op_email) VALUES (?, ?, ?, ?, ?)",(int(operatorid.get()),operatorname.get(),operatoraddress.get(),int(operatorphone.get()),operatoremail.get()))
        connection.commit()
        label=Label(root,text=(operatorid.get(),operatorname.get(),operatoraddress.get(),operatorphone.get(),operatoremail.get()))
        label.grid(row=4,column=5,columnspan=10)
    except Exception as e:
        print(f"Exception {e}")
    finally:
        connection.close()
    return label
def editopertor(label):
    try:
        connection = sq.connect("opertor_detail.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE opertor_details_real SET op_name=?, op_address=?,op_phone=?, op_email=? WHERE op_id  = ?",
                       (operatorname.get(), operatoraddress.get(), int(operatorphone.get()), operatoremail.get(), int(operatorid.get())))
        connection.commit()
        messagebox.showinfo("Bus Entry","Bus Record edited")
        label.destroy()
        updated_label = Label(root, text=(operatorid.get(), operatorname.get(), operatoraddress.get(), operatorphone.get(), operatoremail.get()))
        updated_label.grid(row=4, column=5, columnspan=10)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
    return updated_label

fontFam="Arial"
root=Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
img=Image.open("starbus.png")
img = img.resize((225,175 ))
img = ImageTk.PhotoImage(img) 
Label(root,image=img).grid(padx=550,row=0,columnspan=30)
Label(root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=1,columnspan=30,pady=15)
Label(root,text="Add New Details To Database",fg="green4",font=(("Arial",30,"bold"))).grid(row=2,columnspan=30,pady=15)
Label(root,text="Operator id",font=((fontFam,15,"bold"))).grid(row=3,column=5,pady=15)
operatorid=StringVar()
Entry(root,textvariable=operatorid).grid(row=3,column=6,columnspan=1,pady=15)
Label(root,text="Name",font=((fontFam,15,"bold"))).grid(row=3,column=7,pady=15)
operatorname=StringVar()
Entry(root,textvariable=operatorname).grid(row=3,column=8,columnspan=1,pady=15)
Label(root,text="Address",font=((fontFam,15,"bold"))).grid(row=3,column=9,pady=15)
operatoraddress=StringVar()
Entry(root,textvariable=operatoraddress).grid(row=3,column=10,columnspan=1,pady=15)
Label(root,text="Phone",font=((fontFam,15,"bold"))).grid(row=3,column=11,pady=15)
operatorphone=StringVar()
Entry(root,textvariable=operatorphone).grid(row=3,column=12,columnspan=1,pady=15)
Label(root,text="Email",font=((fontFam,15,"bold"))).grid(row=3,column=13,pady=15)
operatoremail=StringVar()
Entry(root,textvariable=operatoremail).grid(row=3,column=14,columnspan=1,pady=15)
label=Button(root,text="Add",command=Addopertor,fg="black",bg="spring green",font="Arial 10 bold")
label.grid(row=3,column=16,padx=10)
Button(root,text="Edit",command=lambda:editopertor(label),fg="black",bg="spring green",font="Arial 10 bold").grid(row=3,column=17,padx=10)
house=Image.open("House.png")
house = house.resize((75,50 ))
house = ImageTk.PhotoImage(house) 
Button(root,image=house,command=root.bell,bg="spring green").grid(row=3,column=18)
root.mainloop()