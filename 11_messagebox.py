import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Juseong GUI")
root.geometry("640x480") #가로*세로

#기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo("notification", "success! happy trip!")

def warn():
    msgbox.showwarning("warning", "this seat is already reserved")

def okcancel():
    msgbox.askokcancel("Yes / No" , "this seat used with kids.\nwould you like to make a reservation?")

def err():
    msgbox.showerror("error", "pay error!")

def retrycancel():
    msgbox.askretrycancel("retry / cancel", "temporal error occur! Do you try again?")

def yesno():
    msgbox.askyesno("yes / no", "this seat is revesrse! Do you make a reservation?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message = "reservation is not saved.\n Do you want to save?")
# 네: 저장 후 종료
# 아니오: 저장하지 않고 종료
# 취소: 프로그램 종료 취소(현재 화면에서 계속 작업)

    print("response: ", response) # true false none -> 예 1, 아니오 0, 그 외는 취소
    if response == 1:
        print("yes")
    elif response==0:
        print("no")
    else:
        print("cancel")
Button(root, command= info, text="notification").pack()
Button(root, command= warn, text="warning").pack()
Button(root, command= err, text="error").pack()

Button(root, command= okcancel, text="okay cancel").pack()
Button(root, command= retrycancel, text="retry cancel").pack()
Button(root, command= yesno, text="yes no").pack()
Button(root, command= yesnocancel, text="yes no cancel").pack()

root.mainloop()
