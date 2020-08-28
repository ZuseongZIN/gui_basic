import tkinter.ttk as ttk   #콤보 박스는 여기에서 불러와야함
from tkinter import *

root = Tk()
root.title("Juseong GUI")
root.geometry("640x480") #가로*세로

values = [str(i) + "(day)" for i in range(1,32)] #1~31까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("pay date") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) #0번째 인덱스 값 선택
readonly_combobox .pack()
#콤보 박스에 글자 쓰기 불가능

def btncmd():
    print(combobox.get()) #선택된 값 출력
    print(readonly_combobox.get())  # 선택된 값 출력

btn = Button(root, text = "order", command = btncmd)
btn.pack()

root.mainloop()
