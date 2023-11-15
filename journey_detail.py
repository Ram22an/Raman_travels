from tkinter import *
from tkinter.messagebox import askyesno
from PIL import ImageTk,Image
import sqlite3 as sq
def finctioncall():
    displaydetail(desto_var, desfrom_var, desdate_var)
def functioncall2(noseat,listofval,i):
    askyesornoinfun(noseat,listofval,i)
def askyesornoinfun(noseatreal,listofval,i):
    noseatreal1=noseatreal.get()
    result = askyesno("Fare Confirmation !!", f"Total amount to be paid Rs {noseatreal1*listofval[i][4]}")

def bookingdetail(listofval,i):
    # useable varibale name_val,v1,noseatreal,mobilenoreal
    Label(root,text="FILL PASSENGER DETAILS TO BOOK THE BUS TICKET",fg="red",bg="CadetBlue1",font="Arial 30 bold").grid(row=8,columnspan=50,pady=10)
    Label(root,text="Name:").grid(row=9,column=12)
    name_var=StringVar()
    name_val=Entry(root,textvariable=name_var).grid(row=9,column=13)
    Label(root,text="Gender:").grid(row=9,column=14)
    v1=StringVar()
    v1.set("click to select")
    option=["Male","female"]
    OptionMenu(root,v1,*option).grid(row=9,column=15)
    Label(root,text="No of Seats:").grid(row=9,column=16)
    noseat=IntVar()
    noseatreal=Entry(root,textvariable=noseat).grid(row=9,column=17)
    Label(root,text="Mobile no:").grid(row=9,column=18)
    mobileno=IntVar()
    mobilenoreal=Entry(root,textvariable=mobileno).grid(row=9,column=19)
    Label(root,text="Age:").grid(row=9,column=20)
    age=IntVar()
    agereal=Entry(root,textvariable=age).grid(row=9,column=21)
    Button(root,text="Book Seat",command=functioncall2(noseat,listofval,i)).grid(row=9,column=22)



def displaydetail(desto, desfrom, desdate):
    Label(root,text="Select bus",fg="green4",font="Arial 10 bold").grid(row=5,column=13)
    Label(root,text="Operator",fg="green4",font="Arial 10 bold").grid(row=5,column=14)        
    Label(root,text="Bus type",fg="green4",font="Arial 10 bold").grid(row=5,column=15)
    Label(root,text="Available/Capacity",fg="green4",font="Arial 10 bold").grid(row=5,column=16)
    Label(root,text="Fare",fg="green4",font="Arial 10 bold").grid(row=5,column=17)
    destoval=desto.get()
    desfromval=desfrom.get()
    desdatevale=desdate.get()
    busdetailval = cursor.execute("select Operator, Bus_type, Available, Capacity, Fare from local_bus_real where To_dest=? and FROM_dest=? and Journey_date=?", (destoval, desfromval, desdatevale))
    listofval = busdetailval.fetchall()
    busch=IntVar()
    r1=IntVar()
    busch.set(-1)
    for i in range(0,len(listofval)):
        r1=Radiobutton(root,text=f"Bus {i}",variable=busch,value=1).grid(row=i+6,column=13)
        Label(root,text=f"{listofval[i][0]}",fg="blue2",font="Arial 12 bold").grid(row=i+6,column=14)
        Label(root,text=f"{listofval[i][1]}",fg="blue2",font="Arial 12 bold").grid(row=i+6,column=15)
        Label(root,text=f"{listofval[i][2]}/{listofval[i][3]}",fg="blue2",font="Arial 12 bold").grid(row=i+6,column=16)
        Label(root,text=f"{listofval[i][4]}",fg="blue2",font="Arial 12 bold").grid(row=i+6,column=17)
        Button(root,text="Proceed to book",command=bookingdetail(listofval,i),bg="pale green").grid(row=i+6,column=20)


fontFam="Arial"
root=Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
img=Image.open("starbus.png")
img = img.resize((225,175 ))
img = ImageTk.PhotoImage(img) 
Label(root,image=img).grid(padx=550,row=1,columnspan=50)
Label(root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=2,columnspan=50,pady=20)
Label(root,text="Enter Journey Details",fg="green4",bg="spring green",font="Arial 18 bold").grid(row=3,columnspan=50,pady=20)
Label(root,text="TO").grid(row=4,column=13)
desto_var = StringVar() 
desto=Entry(root,textvariable=desto_var)
desto.grid(row=4,column=14)
Label(root,text="FROM").grid(row=4,column=15)
desfrom_var = StringVar() 
desfrom=Entry(root,textvariable=desfrom_var).grid(row=4,column=16)
Label(root,text="DATE").grid(row=4,column=17)
desdate_var = StringVar() 
desdate=Entry(root,textvariable=desdate_var).grid(row=4,column=18)
Button(root,text="SHOW BUS",command=finctioncall,fg="black",bg="spring green",font="Arial 10 bold").grid(row=4,column=20)
house=Image.open("House.png")
house = house.resize((75,50 ))
house = ImageTk.PhotoImage(house) 
Button(root,image=house,command=root.bell,bg="spring green").grid(row=4,column=22)
connection = sq.connect("busdetail.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS local_bus_real (
                    To_dest varchar(20),
                    FROM_dest varchar(20),
                    Journey_date varchar(10),
                    Operator varchar(15),
                    Bus_type varchar(10),
                    Available int,
                    Capacity int,
                    Fare int
                )''')
cursor.execute("select * from local_bus_real")
table_exists=cursor.fetchall()
if not table_exists:
    with open('busdetail.txt', 'r') as file:
        for line in file:
            words=line.split()
            cursor.execute("INSERT INTO local_bus_real (To_dest, FROM_dest, Journey_date, Operator, Bus_type, Available, Capacity, Fare) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(words[0], words[1], words[2], words[3], words[4], int(words[5]), int(words[6]), int(words[7])))
    connection.commit()
else:
    pass
root.mainloop()