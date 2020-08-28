from tkinter import *

root = Tk()
root.title("Nado GUI")

bt1 = Button(root, text="버튼1")
bt1.pack()

btn2 = Button(root,padx=5,pady=10,text = "버튼222222222") #글자에 따라서 크기가 달라짐
btn2.pack()

btn3 = Button(root,padx=10,pady=5,text = "버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼444444444444444") #버튼 크기가 글자의 영향을 받지 않음
btn4.pack()

btn5 = Button(root, fg="red", bg = "yellow", text = "버튼5")
btn5.pack()

photo = PhotoImage(file="cat.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("Button clicked")

btn7 = Button(root, text = "동작하는 버튼", command = btncmd)
btn7.pack()

root.mainloop()
