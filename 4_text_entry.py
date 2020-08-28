from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로*세로

txt = Text(root, width=30,height=5)
txt.pack()

txt.insert(END, "Write text please") #여러줄 입력 가능, 워드 같은 것

e = Entry(root, width=30) #엔터 입력 불가능, 즉 단일 줄  ex 로그인 아이디 비번
e.pack()
e.insert(0, "한 줄만 입력해주세요")

def btncmd():
    print(txt.get("1.0",END))#1: 첫번째 줄을 의미 , 0 : 0번째 컬럼 의미
    print(e.get())

    #내용 삭제제
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()
root.mainloop()
