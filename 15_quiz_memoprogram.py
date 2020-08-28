import os
from tkinter import *

root = Tk()
root.title("None")
root.geometry("640x480") #가로*세로
#root.geometry("640x480+300+100")  #가로*세로 + x좌표+y좌표

#파일 열기 및 저장
filename = "mynote.txt"
def open_file():
    if os.path.isfile(filename): # 파일 있으면 true, 아니면 false
        with open(filename, "r" , encoding="utf8") as file:
            txt.delete("1.0",END) #텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0",END)) #모든 내용을 가져와서 저장
    tname = ""
    for i in txt.get("1.0", END):
        if i == ' ' or i == '\n':
            break
        else:
            tname+=i

    if os.path.isfile(filename):
        root.title(tname)

menu = Menu(root)
menu_file = Menu(menu, tearoff=0) #tearoff -> 하위 메뉴의 분리 기능 사용 유/무
menu_file.add_command(label="Open" ,command = open_file)
menu_file.add_command(label="Save" , command = save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command= root.quit)
menu.add_cascade(label="file", menu= menu_file)

menu.add_cascade(label="Edit")
menu.add_cascade(label="Frame")
menu.add_cascade(label="View")
menu.add_cascade(label="Help")

#scroll bar, root를 프레임으로 생각
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

#본문
txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(fill="both", expand = True)
scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()
