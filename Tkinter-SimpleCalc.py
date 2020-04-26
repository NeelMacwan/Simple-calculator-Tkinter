# ###### Simple Calculator

#Coded by Neel Macwan


from tkinter import *
root= Tk()
root.title("MyCalculator")
e=Entry(root,width=30,borderwidth=2)
e.grid(row=0,column=0,columnspan=2, padx=10,pady=10)
#def button_add():
    
 #   return
def button_Click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def button_Clear():
    e.delete(0,END)

def button_Add():
    first_number = e.get()
    global f_number
    global math
    math="Addition"
    f_number = int(first_number)
    e.delete(0,END)
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math == "Addition":
        e.insert(0, f_number +int(second_number))
    if math == "Subtraction":
        e.insert(0, f_number -int(second_number))
    if math == "Division":
        e.insert(0, f_number /int(second_number))
    if math == "Multiplication":
        e.insert(0, f_number *int(second_number))

def button_sub():
    first_number = e.get()
    global f_number
    global math
    math="Subtraction"
    f_number = int(first_number)
    e.delete(0,END)
    
def button_Mul():
    first_number = e.get()
    global f_number
    global math
    math="Multiplication"
    f_number = int(first_number)
    e.delete(0,END)
    
def button_Div():
    first_number = e.get()
    global f_number
    global math
    math="Division"
    f_number = int(first_number)
    e.delete(0,END)
#DefTheBt
button1 = Button(root, text="1",padx=35,pady=20,bg="orange" ,fg="white",command=lambda:button_Click(1))
button2 = Button(root, text="2",padx=35,pady=20,bg="orange" ,fg="white",command=lambda:button_Click(2))
button3 = Button(root, text="3",padx=35,pady=20,bg="orange" ,fg="white",command=lambda:button_Click(3))
button4 = Button(root, text="4",padx=35,pady=20,bg="orange" ,fg="white",command=lambda:button_Click(4))
button5 = Button(root, text="5",padx=35,pady=20,bg="orange" ,fg="white",command=lambda:button_Click(5))
button6 = Button(root, text="6",padx=35,pady=20,bg="orange",fg="white",command=lambda:button_Click(6))
button7 = Button(root, text="7",padx=35,pady=20,bg="orange" ,fg="white",command=lambda:button_Click(7))
button8 = Button(root, text="8",padx=35,pady=20,bg="orange" ,fg="white",command=lambda:button_Click(8))
button9 = Button(root, text="9",padx=35,pady=20,bg="orange" ,fg="white",command=lambda:button_Click(9))
button0 = Button(root, text="0",padx=35,pady=20,bg="orange" ,fg="white",command=lambda:button_Click(0))

button_add = Button(root,text="+",padx=35,pady=20,bg="green",command=button_Add)
button_Cl = Button(root,text="C",padx=35,pady=20,bg="green",command=button_Clear)
button_EQ = Button(root,text="=", padx=35,pady=20,bg="blue",fg="white",command=button_equal)
button_sub = Button(root, text="-",padx=35,pady=20,bg="orange" ,fg="white",command=button_sub)
button_Mul = Button(root, text="x",padx=35,pady=20,bg="orange" ,fg="white",command=button_Mul)
button_Div = Button(root, text="/",padx=35,pady=20,bg="orange" ,fg="white",command=button_Div)
#Display Button on Screen
button_EQ.grid(row=4,column=2)
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=1)
button_sub.grid(row=3,column=3)
button_Mul.grid(row=2,column=3)
button_Div.grid(row=4,column=3)
button_add.grid(row=1,column=3)
button_Cl.grid(row=4,column=0)
root.mainloop()

