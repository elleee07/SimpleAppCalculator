# ELLA MARIE MALLARI
# BSCPE 1-4

# Calculator App 

# importing tkinter
from tkinter import *

root = Tk() 
root.title("Calculator")
root.configure(bg="gray")

entry_num = Entry(root, width=50, borderwidth=25)
root.resizable(0,0)
entry_num.grid(row=0, column=0, columnspan=80, padx=30)

# defining buttons 
def button_click(number):
    current = entry_num.get()
    entry_num.delete(0, END)
    entry_num.insert(0, str(current) + str(number))

# define clear button 
def button_clear():
    entry_num.delete(0, END)

# define clear entry button
def button_clearEntry():
    entry_num.delete(0, END)

# define percentage button
def button_percentage():
    entry_num.delete(0, END)

# define decimal button
def button_decimal():
    entry_num.delete(0, END)

# define add button
def button_add():
    first_number = entry_num.get()
    global first_num
    global math 
    math = "add"
    first_num = int(first_number)
    entry_num.delete(0, END)

# define subtract button 
def button_subtract():
    first_number = entry_num.get()
    global first_num
    global math 
    math = "subtract"
    first_num = int(first_number)
    entry_num.delete(0, END)
   
# define multiplication button 
def button_multiplication():
    first_number = entry_num.get()
    global first_num
    global math 
    math = "multiplication"
    first_num = int(first_number)
    entry_num.delete(0, END)

# define division button 
def button_division():
    first_number = entry_num.get()
    global first_num
    global math 
    math = "division"
    first_num = int(first_number)
    entry_num.delete(0, END)

# define equal button
def button_equal():
    second_number = entry_num.get()
    entry_num.delete(0, END)

    if math == "add":
        entry_num.insert(0, first_num + int(second_number))
    if math == "subtract":
        entry_num.insert(0, first_num - int(second_number))
    if math == "multiplication":
        entry_num.insert(0, first_num * int(second_number))
    if math == "division":
        entry_num.insert(0, first_num / int(second_number))

button_1 = Button(root, text="1", padx=45, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=50, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=45, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=50, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=45, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=50, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=45, pady=20, command=lambda: button_click(0))

# add button
button_add = Button(root, text="+", padx=41, pady=20, command=button_add)

# subtract button 
button_subtract = Button(root, text="-", padx=42, pady=20, command=button_subtract)

# multiplication button 
button_multiplication = Button(root, text="*", padx=42, pady=20, command=button_multiplication)

# division button 
button_division = Button(root, text="/", padx=42, pady=20, command=button_division)

# function buttons 
button_equal = Button(root, text="=", padx=88, pady=20, command=button_equal)
button_clearEntry = Button(root, text="CE", padx=46, pady=20, command=button_clearEntry)
button_clear = Button(root, text="C", padx=39, pady=20, command=button_clear)
button_percentage = Button(root, text="%", padx=43, pady=20, command=button_percentage)
button_decimal = Button(root, text=".", padx=52, pady=20, command=button_decimal)

# putting the buttons on the screen
button_percentage.grid(row=1, column=0)
button_clearEntry.grid(row=1, column=1) 
button_clear.grid(row=1, column=2) 
button_add.grid(row=1, column=3) 
button_subtract.grid(row=2, column=3) 
button_multiplication.grid(row=3, column=3) 
button_division.grid(row=4, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_decimal.grid(row=5, column=1)
button_equal.grid(row=5, column=2, columnspan=3)


root.mainloop()