from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로*세로

listbox = Listbox(root, selectmode="extended",height=0) #single 하나만 선택, extended 여러개 선택 가능
#height의 경우 0을 입력하면 모든 선택지가 보이지만, 나머지 숫자를 입력하면 그 숫자만큼만 선택지로 보여짐

listbox.insert(0, "apple")
listbox.insert(1,"strawberry")
listbox.insert(2,"banana")
listbox.insert(END,"watermelon")
listbox.insert(END,"grape")
listbox.pack()

def btncmd():
    #삭제
    #listbox.delete(END)#맨 뒤에 있는 항목을 삭제, 0이면 맨 앞 항목 삭제

    #갯수 확인
    print("there are", listbox.size(),"thing(s)")

    #항목 확인
    print("fromt first to third things: ", listbox.get(0,2))

    #선택된 항목 확인 위치로 반환 ex ) 0 ,1, 2
    print("clicked things : ", listbox.curselection())
btn = Button(root, text = "클릭", command = btncmd)
btn.pack()

root.mainloop()
