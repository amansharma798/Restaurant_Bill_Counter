from tkinter import *
top=Tk()
top.resizable(0,0)
top.geometry("1366x768")
c1=Canvas(top,bg="pink",height=768,width=566).place(x=800,y=0)
l1=Label(top,text="SNACK SPOT", font=("Courier", 30),bg="pink",padx=20).place(x=940,y=20)
l2=Label(top,text="MENU",font=("Courier",25),bg="pink").place(x=1050,y=80)
l3=Label(top,text="Veg Noodles",font=("Lucida Handwriting",20),bg="pink").place(x=850,y=180)
l3=Label(top,text="80",font=("Lucida Handwriting",20),bg="pink").place(x=1250,y=180)
l4=Label(top,text="Egg Noodles",font=("Lucida Handwriting",20),bg="pink").place(x=850,y=250)
l4=Label(top,text="100",font=("Lucida Handwriting",20),bg="pink").place(x=1250,y=250)
l5=Label(top,text="Chilli Potato",font=("Lucida Handwriting",20),bg="pink").place(x=850,y=320)
l5=Label(top,text="60",font=("Lucida Handwriting",20),bg="pink").place(x=1250,y=320)
l6=Label(top,text="Spring Roll",font=("Lucida Handwriting",20),bg="pink").place(x=850,y=390)
l6=Label(top,text="50",font=("Lucida Handwriting",20),bg="pink").place(x=1250,y=390)
l7=Label(top,text="Burger",font=("Lucida Handwriting",20),bg="pink").place(x=850,y=460)
l7=Label(top,text="40",font=("Lucida Handwriting",20),bg="pink").place(x=1250,y=460)
l8=Label(top,text="Pizza Burger",font=("Lucida Handwriting",20),bg="pink").place(x=850,y=530)
l8=Label(top,text="60",font=("Lucida Handwriting",20),bg="pink").place(x=1250,y=530)
l9=Label(top,text="Sandwich",font=("Lucida Handwriting",20),bg="pink").place(x=850,y=600)
l9=Label(top,text="40",font=("Lucida Handwriting",20),bg="pink").place(x=1250,y=600)
l10=Label(top,text="Cheese Sandwich",font=("Lucida Handwriting",20),bg="pink").place(x=850,y=670)
l10=Label(top,text="60",font=("Lucida Handwriting",20),bg="pink").place(x=1250,y=670)



c2=Canvas(top,height=768,width=800,bg="gold").place(x=0,y=0)

scvalue=StringVar()
scvalue1=StringVar()
value=""
total=""

Noodles1=StringVar()
Egg_Noodles1=StringVar()
Chilli_Potato1=StringVar()
Spring_Roll1=StringVar()
Burger1=StringVar()
Pizza_Burger1=StringVar()
Sandwich1=StringVar()
Cheese_Sandwich1=StringVar()

l12=Label(top,text="Noodles",font=("Elephant",12),bg="gold").place(x=20,y=130)
l13=Label(top,text="Egg Noodles",font=("Elephant",12),bg="gold").place(x=20,y=180)
l14=Label(top,text="Chilli Potato",font=("Elephant",12),bg="gold").place(x=20,y=230)
l15=Label(top,text="Spring Roll",font=("Elephant",12),bg="gold").place(x=20,y=280)
l16=Label(top,text="Burger",font=("Elephant",12),bg="gold").place(x=400,y=130)
l17=Label(top,text="Pizza Burger",font=("Elephant",12),bg="gold").place(x=400,y=180)
l18=Label(top,text="Sandwich",font=("Elephant",12),bg="gold").place(x=400,y=230)
l18=Label(top,text="Cheese Sandwich",font=("Elephant",12),bg="gold").place(x=400,y=280)
l20=Label(top,text="Total With GST",font=("Elephant",12),bg="gold").place(x=10,y=524)
l19=Label(top,text="18% GST APPLICABLE",font=("Lucida Handwriting",15),bg="gold").place(x=10,y=600)

s1=Spinbox(top,from_ = 0, to = 25,textvariable=Noodles1).place(x=160,y=130)
s2=Spinbox(top,from_ = 0, to = 25,textvariable=Egg_Noodles1).place(x=160,y=180)
s3=Spinbox(top,from_ = 0, to = 25,textvariable=Chilli_Potato1).place(x=160,y=230)
s4=Spinbox(top,from_ = 0, to = 25,textvariable=Spring_Roll1).place(x=160,y=280)
s5=Spinbox(top,from_ = 0, to = 25,textvariable=Burger1).place(x=570,y=130)
s6=Spinbox(top,from_ = 0, to = 25,textvariable=Pizza_Burger1).place(x=570,y=180)
s7=Spinbox(top,from_ = 0, to = 25,textvariable=Sandwich1).place(x=570,y=230)
s8=Spinbox(top,from_ = 0, to = 25,textvariable=Cheese_Sandwich1).place(x=570,y=280)






def total1():
    global value
    a=float(Noodles1.get())
    b=float(Egg_Noodles1.get())
    c=float(Chilli_Potato1.get())
    d=float(Spring_Roll1.get())
    e=float(Burger1.get())
    f=float(Pizza_Burger1.get())
    g=float(Sandwich1.get())
    h=float(Cheese_Sandwich1.get())

    gs=(a * 80 + b * 100 + c * 60 + d * 50 + e * 40 + f * 60 + g * 40 + h * 60)
    value=gs
    scvalue.set(value)
    gst=(gs*18)/100
    value = (a * 80 + b * 100 + c * 60 + d * 50 + e * 40 + f * 60 + g * 40 + h * 60)+gst
    scvalue1.set(value)

def clear():
    global value
    value=""
    Noodles1.set("0")
    Egg_Noodles1.set("0")
    Chilli_Potato1.set("0")
    Spring_Roll1.set("0")
    Burger1.set("0")
    Pizza_Burger1.set("0")
    Sandwich1.set("0")
    Cheese_Sandwich1.set("0")
    scvalue.set(value)
    scvalue1.set(value)

b1=Button(top,text="TOTAL",font=("Elephant",12),command=total1).place(x=20,y=450)
b2=Button(top,text="CLEAR",font=("Elephant",12),command=clear).place(x=550,y=450)
t1=Entry(top,textvariable=scvalue,state=DISABLED,font=("Elephant",17)).place(x=150,y=450)
t2=Entry(top,textvariable=scvalue1,state=DISABLED,font=("Elephant",17)).place(x=150,y=520)
top.mainloop()