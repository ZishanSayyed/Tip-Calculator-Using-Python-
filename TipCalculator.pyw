from tkinter import Tk,Radiobutton,Button,Label,StringVar,IntVar,Entry
#to built Radiobutton we write Radiobutton, StringVar and IntVar(numarical value data types) are the data types

#a class is an object constructor
class TipCalculator():     # method def__init__is a built-in function in python which always executed when class is being initiated
    def __init__(self):    #we can use this init function to assign values to object property
                           #self parameter is a reference to the current instance of the class and use to access variable belong to the class
        window=Tk()
        window.title("Tip Calculator App")
        window.configure(background="light blue")
        window.geometry("500x250")
        window.resizable(width=False,height=False)

        #adding vertiables
        self.meal_cost=StringVar()  #data type
        self.tip_percentage=IntVar() #data types
        self.tip=StringVar()
        self.total_cost=StringVar() #function in the class is call method


        #adding Labels
        tip_percents=Label(window,text="Tip Percentage",bg="black",fg="white")
        tip_percents.grid(column=0,row=0)

        bill_amt=Label(window,text="Bill Amount",bg="pink",fg="white")
        bill_amt.grid(column=1,row=0,padx=14)

        meal_cost=StringVar()  # Value which be in window is boolean
        bill_amt_entry=Entry(window,textvariable=self.meal_cost,width=14)
        bill_amt_entry.grid(column=2,row=0)



        # creating Radiobutton
        tip_percentage=IntVar()
        five_percent_tip=Radiobutton(window,text="0.5%",variable=self.tip_percentage,value=5)
        five_percent_tip.grid(column=0,row=1)

        ten_percent_tip=Radiobutton(window,text="10%",variable=self.tip_percentage,value=10)
        ten_percent_tip.grid(column=0,row=2)

        fifteen_percent_tip=Radiobutton(window,text="15%",variable=self.tip_percentage,value=15)
        fifteen_percent_tip.grid(column=0,row=3)

        twenty_percent_tip=Radiobutton(window,text="20%",variable=self.tip_percentage,value=20)
        twenty_percent_tip.grid(column=0,row=4)

        twentyfive_percent_tip=Radiobutton(window,text="25%",variable=self.tip_percentage,value=25)
        twentyfive_percent_tip.grid(column=0,row=5)

        thirty_percent_tip=Radiobutton(window,text="30%",variable=self.tip_percentage,value=30)
        thirty_percent_tip.grid(column=0,row=6)


        tip_amt_lbl=Label(window,text="Tip Amount",bg="black",fg="white")
        tip_amt_lbl.grid(column=1,row=2,padx=14)
        tip_amt_entry=Entry(window,textvariable=self.tip,width=14)
        tip_amt_entry.grid(column=2,row=2)

        bill_total_lbl=Label(window,text="Total Bill Amt",bg="red",fg="white")
        bill_total_lbl.grid(column=1,row=4,padx=15)
        bill_total_entry=Entry(window,textvariable=self.total_cost,width=14)
        bill_total_entry.grid(column=2,row=4)

        #creating Button
        calculate_btn=Button(window,text="Calculate",bg="green",fg="white",command=self.calulate)
        calculate_btn.grid(column=1,row=6,padx=15)

        clear_btn=Button(window,text="Clear",bg="black",fg="white",command=self.clear)
        clear_btn.grid(column=2,row=6)

        window.mainloop()   #run the app

        #creating function which perform the req task

    def calulate(self):
        pre_tip=float(self.meal_cost.get())
        percentage=self.tip_percentage.get()/100
        tip_amt_entry=pre_tip*percentage
        self.tip.set(tip_amt_entry)

        final_bill=pre_tip+tip_amt_entry
        self.total_cost.set(final_bill)

    def clear(self):
        self.total_cost.set("")
        self.meal_cost.set("")
        self.tip.set("")











TipCalculator()  #which enables the app to lunch form the main loop fun
