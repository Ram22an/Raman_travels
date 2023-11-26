from tkinter import *
from tkinter.messagebox import askyesno
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3 as sq
class Bus_Service:
    def __init__(self):
        self.root=None
        self.house=Image.open("House.png")   
    def first_page(self):
        fontFam="Arial"
        self.root=Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        img=Image.open("starbus.png")
        img = img.resize((225,175 ))
        img = ImageTk.PhotoImage(img) 
        Label(self.root,image=img).pack()
        Label(self.root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).pack(pady=30)
        Label(self.root,text="Created by: Raman Soni",fg="Dark Blue",font=(fontFam,20)).pack(pady=20)
        Label(self.root,text="github: https://github.com/Ram22an",fg="Dark Blue",font=(fontFam,20)).pack(pady=20)
        Label(self.root,text="linkedin: https://www.linkedin.com/in/raman-soni-09764524a",fg="Dark Blue",font=(fontFam,20)).pack(pady=20)
        Label(self.root,text="Project based learing",fg="Dark Blue",font=(fontFam,20)).pack()
        Label(self.root,text="Please Wait for 5 seconds",fg="red",font=(fontFam,12)).pack(pady=20)
        self.root.after(5000, self.second_page)
        self.root.mainloop()
    def second_page(self):
        self.root.destroy()
        fontFam="Arial"
        self.root=Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        img=Image.open("starbus.png")
        img = img.resize((225,175 ))
        img = ImageTk.PhotoImage(img) 
        Label(self.root,image=img).grid(padx=550,row=1,columnspan=20)
        Label(self.root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=2,columnspan=20,pady=40)
        Button(self.root,text="SEAT BOOKING",command=self.Seat_booking,font=f"{fontFam} 20 bold",bg="lime green").grid(padx=100,row=3,column=1,pady=50)
        Button(self.root,text="CHECK BOOKED SEAT",command=self.Check_booking,font=f"{fontFam} 20 bold",bg="lime green").grid(padx=100,row=3,column=2,pady=50)
        Button(self.root,text="ADD BUS DETAIL",command=self.Book_frontpage_bus_detail,font=f"{fontFam} 20 bold",bg="lime green").grid(padx=100,row=3,column=3,pady=50)
        Label(self.root,text="For Admin Only",fg="red",font=f"{fontFam} 15 bold").grid(row=4,column=3)
        self.root.mainloop()
    def Seat_booking(self):
        self.root.destroy()
        def displaydetailcover():
            displaydetail(desto_var, desfrom_var, desdate_var)
        def askyesornoinfuncover(name_var,optionmenu,noseatreal,mobilenoreal,agereal,val):
            askyesornoinfun(name_var,optionmenu,noseatreal,mobilenoreal,agereal,val)
        def bookingdetailcover(val):
            bookingdetail(val)
        def bookingdetail(val):
            # useable varibale name_val,v1,noseat,mobileno,age
            Label(self.root,text="FILL PASSENGER DETAILS TO BOOK THE BUS TICKET",fg="red",bg="CadetBlue1",font="Arial 30 bold").grid(row=8,columnspan=50,pady=10)
            Label(self.root,text="Name:").grid(row=9,column=12)
            name_var=StringVar()
            name_val=Entry(self.root,textvariable=name_var).grid(row=9,column=13)
            Label(self.root,text="Gender:").grid(row=9,column=14)
            v1=StringVar(self.root)
            v1.set("click to select")
            option=["Male","female"]
            optionmenu=OptionMenu(self.root,v1,*option).grid(row=9,column=15)
            Label(self.root,text="No of Seats:").grid(row=9,column=16)
            noseat=IntVar()
            noseatreal=Entry(self.root,textvariable=noseat).grid(row=9,column=17)
            Label(self.root,text="Mobile no:").grid(row=9,column=18)
            mobileno=IntVar()
            mobilenoreal=Entry(self.root,textvariable=mobileno).grid(row=9,column=19)
            Label(self.root,text="Age:").grid(row=9,column=20)
            age=IntVar()
            agereal=Entry(self.root,textvariable=age).grid(row=9,column=21)
            Button(self.root,text="Book Seat",command=lambda:askyesornoinfuncover(name_var,v1,noseat,mobileno,age,val)).grid(row=9,column=22)
        def askyesornoinfun(name_val,v1,noseat,mobileno,age,val):
            nameval=name_val.get()
            noseatval=noseat.get()
            mobilval=mobileno.get()
            ageval=age.get()
            v1val=v1.get()
            result = askyesno("Fare Confirmation !!", f"Total amount to be paid Rs {noseatval*val}")
            connection1 = sq.connect("customer_detail.db")
            cursor1 = connection1.cursor()
            cursor1.execute('''CREATE TABLE IF NOT EXISTS customer_detail_real (
                            name varchar(20),
                            no_of_seat int,
                            mobile_no int(10),
                            age int,
                            gender varchar(7),
                            fare int
                        )''')
            
            cursor1.execute("INSERT INTO customer_detail_real(name,no_of_seat,mobile_no,age,gender,fare) VALUES(?,?,?,?,?,?)",(nameval,noseatval,mobilval,ageval,v1val,val))
            connection1.commit()
            connection1.close()
            if result :
                self.Final_bookking(nameval,noseatval,mobilval,ageval,v1val,val)
            else:
                self.second_page()
        def displaydetail(desto, desfrom, desdate):
            Label(self.root,text="Select bus",fg="green4",font="Arial 10 bold").grid(row=5,column=13)
            Label(self.root,text="Operator",fg="green4",font="Arial 10 bold").grid(row=5,column=14)        
            Label(self.root,text="Bus type",fg="green4",font="Arial 10 bold").grid(row=5,column=15)
            Label(self.root,text="Available/Capacity",fg="green4",font="Arial 10 bold").grid(row=5,column=16)
            Label(self.root,text="Fare",fg="green4",font="Arial 10 bold").grid(row=5,column=17)
            destoval=desto.get()
            desfromval=desfrom.get()
            desdatevale=desdate.get()
            busdetailval = cursor.execute("select Operator, Bus_type, Available, Capacity, Fare from local_bus_real where To_dest=? and FROM_dest=? and Journey_date=?", (destoval, desfromval, desdatevale))
            listofval = busdetailval.fetchall()
            busch=IntVar()
            r1=IntVar()
            busch.set(-1)
            for i in range(0,len(listofval)):
                r1=Radiobutton(self.root,text=f"Bus {i}",variable=busch,value=1).grid(row=i+6,column=13)
                Label(self.root,text=f"{listofval[i][0]}",fg="blue2",font="Arial 12 bold").grid(row=i+6,column=14)
                Label(self.root,text=f"{listofval[i][1]}",fg="blue2",font="Arial 12 bold").grid(row=i+6,column=15)
                Label(self.root,text=f"{listofval[i][2]}/{listofval[i][3]}",fg="blue2",font="Arial 12 bold").grid(row=i+6,column=16)
                Label(self.root,text=f"{listofval[i][4]}",fg="blue2",font="Arial 12 bold").grid(row=i+6,column=17)
                Button(self.root,text="Proceed to book",command=lambda:bookingdetailcover(listofval[i][4]),bg="pale green").grid(row=i+6,column=20)
            connection.close()
        fontFam="Arial"
        self.root=Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        img=Image.open("starbus.png")
        img = img.resize((225,175 ))
        img = ImageTk.PhotoImage(img) 
        Label(self.root,image=img).grid(padx=550,row=1,columnspan=50)
        Label(self.root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=2,columnspan=50,pady=20)
        Label(self.root,text="Enter Journey Details",fg="green4",bg="spring green",font="Arial 18 bold").grid(row=3,columnspan=50,pady=20)
        Label(self.root,text="TO").grid(row=4,column=13)
        desto_var = StringVar() 
        desto=Entry(self.root,textvariable=desto_var)
        desto.grid(row=4,column=14)
        Label(self.root,text="FROM").grid(row=4,column=15)
        desfrom_var = StringVar() 
        desfrom=Entry(self.root,textvariable=desfrom_var).grid(row=4,column=16)
        Label(self.root,text="DATE").grid(row=4,column=17)
        desdate_var = StringVar() 
        desdate=Entry(self.root,textvariable=desdate_var).grid(row=4,column=18)
        Button(self.root,text="SHOW BUS",command=displaydetailcover,fg="black",bg="spring green",font="Arial 10 bold").grid(row=4,column=20)
        house=Image.open("House.png")
        house = house.resize((75,50 ))
        house = ImageTk.PhotoImage(house) 
        Button(self.root,image=house,command=self.second_page,bg="spring green").grid(row=4,column=22)
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
            print("There is an error in first insertion or databse is already there")
        self.root.mainloop()
    def Final_bookking(self,nameval,noseatval,mobilval,ageval,v1val,val):
        self.root.destroy()
        connection1 = sq.connect("customer_detail.db")
        cursor1 = connection1.cursor()
        cursor1.execute("select * from customer_detail_real WHERE name=? AND no_of_seat =? AND mobile_no =? AND age =? AND gender=? AND fare=?",
                        ((nameval,noseatval,mobilval,ageval,v1val,val)))
        detail_of_customer=cursor1.fetchall()
        name_of_customer=detail_of_customer[0][0]
        no_of_seat=detail_of_customer[0][1]
        mobile_no=detail_of_customer[0][2]
        age_of_customer=detail_of_customer[0][3]
        gender_of_customer=detail_of_customer[0][4]
        total_fare=detail_of_customer[0][5]
        fontFam="Arial"
        self.root=Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        img=Image.open("starbus.png")
        img = img.resize((225,175 ))
        img = ImageTk.PhotoImage(img) 
        Label(self.root,image=img).grid(padx=550,row=1,columnspan=50)
        Label(self.root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=2,columnspan=50,pady=20)
        frame = Frame(self.root, bd=3, relief=SUNKEN)
        frame.grid(row=3,columnspan=50, padx=20, pady=20)
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
        messagebox.showinfo("Success","Seat Booked ....")
        # house=Image.open("House.png")
        self.house = self.house.resize((75,50 ))
        self.house = ImageTk.PhotoImage(self.house) 
        Button(self.root,image=self.house,command=self.second_page,bg="spring green").grid(row=7,column=22)
        connection1.close()
        self.root.mainloop()
    def Check_booking(self):
        self.root.destroy()
        fontFam="Arial"
        def printticket(phone_no):
            connection1 = sq.connect("customer_detail.db")
            cursor1 = connection1.cursor()
            cursor1.execute("SELECT * FROM customer_detail_real WHERE mobile_no = ? LIMIT 1", (int(phone_no.get()),))
            detail_of_customer = cursor1.fetchall()
            if not detail_of_customer:
                result = askyesno("NO BOOKING RECORD", "Do you want to book seat now")
                if result:
                    self.second_page()
                else:
                    self.first_page()
            else:
                name_of_customer=detail_of_customer[0][0]
                no_of_seat=detail_of_customer[0][1]
                mobile_no=detail_of_customer[0][2]
                age_of_customer=detail_of_customer[0][3]
                gender_of_customer=detail_of_customer[0][4]
                total_fare=detail_of_customer[0][5]
                frame = Frame(self.root, bd=3, relief=SUNKEN)
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
            self.house = self.house.resize((75,50 ))
            self.house = ImageTk.PhotoImage(self.house) 
            Button(self.root,image=self.house,command=self.second_page,bg="spring green").grid(row=7,column=22)
        self.root=Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        img=Image.open("starbus.png")
        img = img.resize((225,175 ))
        img = ImageTk.PhotoImage(img) 
        Label(self.root,image=img).grid(padx=550,row=1,columnspan=50)
        Label(self.root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=2,columnspan=50,pady=20)
        Label(self.root,text="Check Your Booking",fg="green4",bg="lawn green",font="Arial 24 bold").grid(padx=550,row=3,columnspan=50,pady=20)
        Label(self.root,text="Enter Your mobile no :-",font="Arial 12 bold").grid(row=4,column=23)
        phone_no=StringVar()
        phone_no1=Entry(self.root,textvariable=phone_no).grid(row=4,column=24)
        Button(self.root,command=lambda:printticket(phone_no),text="Check booking").grid(row=4,column=25)
        self.root.mainloop()
    def Book_frontpage_bus_detail(self):
        self.root.destroy()
        fontFam="Arial"
        self.root=Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        img=Image.open("starbus.png")
        img = img.resize((225,175 ))
        img = ImageTk.PhotoImage(img) 
        Label(self.root,image=img).grid(padx=550,row=0,columnspan=50)
        Label(self.root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=1,columnspan=50,pady=20)
        Label(self.root,text="Add New Details To Database",fg="green4",font=(("Arial",30,"bold"))).grid(row=2,columnspan=50,pady=25)
        Button(self.root,text="New Operator",command=self.New_operator,bg="pale green",font=((fontFam,15))).grid(row=3,column=15,pady=10)
        Button(self.root,text="New Bus",command=self.Add_bus_detail,bg="tomato",font=((fontFam,15))).grid(row=3,column=20,pady=10)
        Button(self.root,text="New Route",command=self.Add_bus_route,bg="SteelBlue1",font=((fontFam,15))).grid(row=3,column=25,pady=10)
        Button(self.root,text="New Run",command=self.Add_new_run,bg="MistyRose3",font=((fontFam,15))).grid(row=3,column=30,pady=10)
        self.root.mainloop()
    def New_operator(self):
        self.root.destroy()
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
                label=Label(self.root,text=(operatorid.get(),operatorname.get(),operatoraddress.get(),operatorphone.get(),operatoremail.get()))
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
                updated_label = Label(self.root, text=(operatorid.get(), operatorname.get(), operatoraddress.get(), operatorphone.get(), operatoremail.get()))
                updated_label.grid(row=4, column=5, columnspan=10)
            except Exception as e:
                print(f"Error: {e}")
            finally:
                connection.close()
            return updated_label

        fontFam="Arial"
        self.root=Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        img=Image.open("starbus.png")
        img = img.resize((225,175 ))
        img = ImageTk.PhotoImage(img) 
        Label(self.root,image=img).grid(padx=550,row=0,columnspan=30)
        Label(self.root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=1,columnspan=30,pady=15)
        Label(self.root,text="Add New Details To Database",fg="green4",font=(("Arial",30,"bold"))).grid(row=2,columnspan=30,pady=15)
        Label(self.root,text="Operator id",font=((fontFam,15,"bold"))).grid(row=3,column=5,pady=15)
        operatorid=StringVar()
        Entry(self.root,textvariable=operatorid).grid(row=3,column=6,columnspan=1,pady=15)
        Label(self.root,text="Name",font=((fontFam,15,"bold"))).grid(row=3,column=7,pady=15)
        operatorname=StringVar()
        Entry(self.root,textvariable=operatorname).grid(row=3,column=8,columnspan=1,pady=15)
        Label(self.root,text="Address",font=((fontFam,15,"bold"))).grid(row=3,column=9,pady=15)
        operatoraddress=StringVar()
        Entry(self.root,textvariable=operatoraddress).grid(row=3,column=10,columnspan=1,pady=15)
        Label(self.root,text="Phone",font=((fontFam,15,"bold"))).grid(row=3,column=11,pady=15)
        operatorphone=StringVar()
        Entry(self.root,textvariable=operatorphone).grid(row=3,column=12,columnspan=1,pady=15)
        Label(self.root,text="Email",font=((fontFam,15,"bold"))).grid(row=3,column=13,pady=15)
        operatoremail=StringVar()
        Entry(self.root,textvariable=operatoremail).grid(row=3,column=14,columnspan=1,pady=15)
        label=Button(self.root,text="Add",command=Addopertor,fg="black",bg="spring green",font="Arial 10 bold")
        label.grid(row=3,column=16,padx=10)
        Button(self.root,text="Edit",command=lambda:editopertor(label),fg="black",bg="spring green",font="Arial 10 bold").grid(row=3,column=17,padx=10)
        self.house = self.house.resize((75,50 ))
        self.house = ImageTk.PhotoImage(self.house) 
        Button(self.root,image=self.house,command=self.second_page,bg="spring green").grid(row=3,column=18)
        self.root.mainloop()
    def Add_bus_detail(self):
        self.root.destroy()
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
                label=Label(self.root,text=(int(bus_id.get()),bus_type.get(),int(bus_capacity.get()),int(bus_fare.get()),int(bus_op_id.get()),int(bus_rout_id.get())))
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
                label=Label(self.root,text=(int(bus_id.get()),bus_type.get(),int(bus_capacity.get()),int(bus_fare.get()),int(bus_op_id.get()),int(bus_rout_id.get())))
                label.grid(row=4,column=7)
            except Exception as es:
                print(f"Exception {es}")
            finally:
                connection.close()
            return label
        fontFam="Arial"
        self.root=Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        img=Image.open("starbus.png")
        img = img.resize((225,175 ))
        img = ImageTk.PhotoImage(img) 
        Label(self.root,image=img).grid(padx=550,row=0,columnspan=50)
        Label(self.root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=1,columnspan=50,pady=15)
        Label(self.root,text="Add Bus Details",fg="green4",font=(("Arial",30,"bold"))).grid(row=2,columnspan=50,pady=15)
        Label(self.root,text="Bus id",font=((fontFam,12,'bold'))).grid(row=3,column=1)
        bus_id=StringVar()
        Entry(self.root,textvariable=bus_id).grid(row=3,column=2)
        Label(self.root,text="Bus Type",font=((fontFam,12,'bold'))).grid(row=3,column=3)
        bus_type=StringVar()
        bus_type.set("Bus Type")
        option=["AC_3X2","AC_2X2","nonAC_3X2","nonAC_2X2"]
        OptionMenu(self.root,bus_type,*option).grid(row=3,column=4)
        Label(self.root,text="Capacity",font=((fontFam,12,'bold'))).grid(row=3,column=5)
        bus_capacity=StringVar()
        Entry(self.root,textvariable=bus_capacity).grid(row=3,column=6)
        Label(self.root,text="Fare Rs",font=((fontFam,12,'bold'))).grid(row=3,column=7)
        bus_fare=StringVar()
        Entry(self.root,textvariable=bus_fare).grid(row=3,column=8)
        Label(self.root,text="Operator ID",font=((fontFam,12,'bold'))).grid(row=3,column=9)
        bus_op_id=StringVar()
        Entry(self.root,textvariable=bus_op_id).grid(row=3,column=10)
        Label(self.root,text="Rout ID",font=((fontFam,12,'bold'))).grid(row=3,column=11)
        bus_rout_id=StringVar()
        Entry(self.root,textvariable=bus_rout_id).grid(row=3,column=12)
        label=Button(self.root,text="Add",command=add_bus_detail,fg="black",bg="spring green",font="Arial 10 bold")
        label.grid(row=3,column=16,padx=10)
        Button(self.root,text="Edit",command=lambda:edit_bus_detail(label),fg="black",bg="spring green",font="Arial 10 bold").grid(row=3,column=17,padx=10)
        self.house = self.house.resize((75,50 ))
        self.house = ImageTk.PhotoImage(self.house) 
        Button(self.root,image=self.house,command=self.second_page,bg="spring green").grid(row=3,column=18)
        self.root.mainloop()
    def Add_bus_route(self):
        self.root.destroy()
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
                label=Label(self.root,text=(int(route_id.get()),route_station_name.get(),int(route_station_id.get())))
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
                label=Label(self.root,text=(int(route_id.get()),route_station_name.get(),int(route_station_id.get())))
                label.grid(row=4,column=7)
            except Exception as es:
                print(f"Exception {es}")
            finally:
                connection.close()
            return label
        fontFam="Arial"
        self.root=Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        img=Image.open("starbus.png")
        img = img.resize((225,175 ))
        img = ImageTk.PhotoImage(img) 
        Label(self.root,image=img).grid(padx=550,row=0,columnspan=50)
        Label(self.root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=1,columnspan=50,pady=15)
        Label(self.root,text="Add Bus Route Details",fg="green4",font=(("Arial",30,"bold"))).grid(row=2,columnspan=50,pady=15)
        Label(self.root,text="Route Id",font=((fontFam,12,'bold'))).grid(row=3,column=5)
        route_id=StringVar()
        Entry(self.root,textvariable=route_id).grid(row=3,column=6)
        Label(self.root,text="Station Name",font=((fontFam,12,'bold'))).grid(row=3,column=7)
        route_station_name=StringVar()
        Entry(self.root,textvariable=route_station_name).grid(row=3,column=8)
        Label(self.root,text="Station Id",font=((fontFam,12,'bold'))).grid(row=3,column=9)
        route_station_id=StringVar()
        Entry(self.root,textvariable=route_station_id).grid(row=3,column=10)
        label=None
        label=Button(self.root,text="Add Route",command=lambda:add_route(label),fg="black",bg="spring green",font="Arial 10 bold")
        label.grid(row=3,column=15,padx=10)
        label=Button(self.root,text="Delete Route",command=lambda:delete_route(label),fg="red",bg="spring green",font="Arial 10 bold")
        label.grid(row=3,column=18,padx=10)
        self.house = self.house.resize((75,50 ))
        self.house = ImageTk.PhotoImage(self.house) 
        Button(self.root,image=self.house,command=self.second_page,bg="spring green").grid(row=3,column=21)
        self.root.mainloop()
    def Add_new_run(self):
        self.root.destroy()
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
                label=Label(self.root,text=(int(bus_id.get()),running_date.get(),int(running_seat.get())))
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
                label=Label(self.root,text=(int(bus_id.get()),running_date.get(),int(running_seat.get())))
                label.grid(row=4,column=7)
            except Exception as es:
                print(f"Exception {es}")
            finally:
                connection.close()
            return label
        fontFam="Arial"
        self.root=Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        img=Image.open("starbus.png")
        img = img.resize((225,175 ))
        img = ImageTk.PhotoImage(img) 
        Label(self.root,image=img).grid(padx=550,row=0,columnspan=50)
        Label(self.root,text="Online Bus Booking System",fg="red",bg="sky blue",font=(fontFam,30)).grid(padx=550,row=1,columnspan=50,pady=15)
        Label(self.root,text="Add Bus Running Details",fg="green4",font=(("Arial",30,"bold"))).grid(row=2,columnspan=50,pady=15)
        Label(self.root,text="Bus Id",font=((fontFam,12,'bold'))).grid(row=3,column=5)
        bus_id=StringVar()
        Entry(self.root,textvariable=bus_id).grid(row=3,column=6)
        Label(self.root,text="Running Date",font=((fontFam,12,'bold'))).grid(row=3,column=7)
        running_date=StringVar()
        Entry(self.root,textvariable=running_date).grid(row=3,column=8)
        Label(self.root,text="Seat Available",font=((fontFam,12,'bold'))).grid(row=3,column=9)
        running_seat=StringVar()
        Entry(self.root,textvariable=running_seat).grid(row=3,column=10)
        label=None
        label=Button(self.root,text="Add Run",command=lambda:add_run(label),fg="black",bg="spring green",font="Arial 10 bold")
        label.grid(row=3,column=15,padx=10)
        label=Button(self.root,text="Delete Run",command=lambda:delete_run(label),fg="red",bg="spring green",font="Arial 10 bold")
        label.grid(row=3,column=18,padx=10)
        self.house = self.house.resize((75,50 ))
        self.house = ImageTk.PhotoImage(self.house) 
        Button(self.root,image=self.house,command=self.second_page,bg="spring green").grid(row=3,column=21)
        self.root.mainloop()
bus_service=Bus_Service()
bus_service.first_page()