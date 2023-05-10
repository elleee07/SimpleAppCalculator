# ELLA MARIE A. MALLARI
# BSCPE 1-4 

# CALCULATOR APP

# handling unchecked exception 
try: 
    import tkinter as tk

    root = tk.Tk()
    root.title("Calculator")
    root.geometry("345x460")
    root.resizable(0,0) 
    root.configure(bg="black")

except ImportError:
    print("Error alert.")

finally:
    print("No error found.")




#import tkinter to make the calculator visible (GUI/UI)
import tkinter as tk 

root = tk.Tk()
root.title("Calculator")
root.geometry("345x460")
root.resizable(0,0)
root.configure(bg="black")


