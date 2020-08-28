from tkinter import *

root = Tk()
root.title("Juseong GUI")
root.geometry("640x480") #가로*세로

Label(root, text = "Please choose Menu").pack(side="top")

Button(root, text = "Order").pack(side="bottom")
#Menu frame
frame_burger = Frame(root, relief = "solid", bd=1)
frame_burger.pack(side="left", fill="both", expand= True)

Button(frame_burger, text = "hamburger").pack()
Button(frame_burger, text = "cheeseburger").pack()
Button(frame_burger, text = "chickenburger").pack()

#Drink frame
frame_drink = LabelFrame(root, text = "drink")
frame_drink.pack(side = "right", fill = "both", expand = "True")
Button(frame_drink, text = "Coke").pack()
Button(frame_drink, text = "DrPepper").pack()
root.mainloop()
