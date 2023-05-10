# ELLA MARIE A. MALLARI
# BSCPE 1-4 

# CALCULATOR APP

# handling unchecked exception 
try: 
    def button_click(number):
        current = input_box.get()
        input_box.delete(0, tk.END)
        input_box.insert(0, str(current) + str(number))
except TypeError:
    print("ERRORRRR")
except IndentationError:
    print("Indentation error found.")

except:
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

root.mainloop()

