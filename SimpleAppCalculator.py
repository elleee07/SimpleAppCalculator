# ELLA MARIE MALLARI
# BSCPE 1-4

# Calculator App 

# importing tkinter
from tkinter import *

root = Tk() 
root.title("Calculator")

entry_num = Entry(root, width=35, borderwidth=5)
entry_num.grid(row=0, column=0, columnspan=3, padx=10)

entry_num.insert(0, "Insert number: ")

# defining buttons 
def button_add():
    return

button_1 = Button(root, text="7", padx=40, pady=20, command=button_add)
button_2 = Button(root, text="8", padx=40, pady=20, command=button_add)
button_3 = Button(root, text="9", padx=40, pady=20, command=button_add)
button_4 = Button(root, text="4", padx=40, pady=20, command=button_add)
button_5 = Button(root, text="5", padx=40, pady=20, command=button_add)
button_6 = Button(root, text="6", padx=40, pady=20, command=button_add)
button_7 = Button(root, text="1", padx=40, pady=20, command=button_add)
button_8 = Button(root, text="2", padx=40, pady=20, command=button_add)
button_9 = Button(root, text="3", padx=40, pady=20, command=button_add)
button_0 = Button(root, text="0", padx=40, pady=20, command=button_add)
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=39, pady=20, command=button_add)
button_multiplication = Button(root, text="x", padx=39, pady=20, command=button_add)
button_division = Button(root, text="÷", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=39, pady=20, command=button_add)
button_clearEntry = Button(root, text="CE", padx=39, pady=20, command=button_add)
button_clear = Button(root, text="C", padx=39, pady=20, command=button_add)

# putting the buttons on the screen 
button_clearEntry.grid(row=1, column=0) 
button_clear.grid(row=1, column=1) 
button_add.grid(row=1, column=2) 
button_subtract.grid(row=2, column=2) 
button_multiplication.grid(row=3, column=2) 
button_division.grid(row=4, column=2)

root.mainloop()