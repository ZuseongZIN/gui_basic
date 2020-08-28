from tkinter import *

root = Tk()
root.title("Juseong GUI")
root.geometry("640x480") #가로*세로

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill="y")

#set이 없으면 스크롤을 해도 다시 올라옴
listbox = Listbox(frame, selectmode = "extended", height=10, yscrollcommand = scrollbar.set)
for i in range(1,32):
    listbox.insert(END, str(i)+ " day")

listbox.pack(side="left")

#scrollbar에도 listbox를 매핑해줘야 서로 연동이 됨
scrollbar.config(command = listbox.yview)

root.mainloop()
