from tkinter import *

root = Tk()
root.title("Juseong GUI")
root.geometry("640x480") #가로*세로

Label(root,text="select menu").pack()

burger_var = IntVar() # 여기에 int 형으로 값을 저장한다
btn_burger1 = Radiobutton(root, text="hamburger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="cheeseburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="chickenburger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root,text="\nselect drink").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coke", value="Coke", variable= drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="DrPepper", value="DrPepper", variable= drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
   print(burger_var.get()) #햄버거 중에서 선택된 라디오 항목의 값(value)을 출력
   print(drink_var.get())

btn = Button(root, text = "order", command = btncmd)
btn.pack()

root.mainloop()
