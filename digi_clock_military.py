# hello im ericka bolta aka eriii mango and i will be implementing a gui digital clock in all pink interface.
# This version will be a 24 hour format
#author Ericka Bolta 3-30-21

from tkinter import*
from tkinter.ttk import*

from time import strftime

root = Tk()
root.title("Pink DiGi Clock") #window title display

def time():
    string = strftime("%H:%M:%S %p") #24hour format
    label.config(text=string)
    label.after(1000, time)

#imported a digital front from web and installed to my pc.
label = Label(root, font=("ds-digital", 80), background= "hot pink", foreground= "pink")
greeting = Label(text="by eriii mango", foreground="hot pink") #adding my tag
label.pack(anchor="center")
greeting.pack()

time()

mainloop()

