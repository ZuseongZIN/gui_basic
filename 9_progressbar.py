import time
import tkinter.ttk as ttk   #콤보 박스는 여기에서 불러와야함
from tkinter import *

root = Tk()
root.title("Juseong GUI")
root.geometry("640x480") #가로*세로

#progressbar = ttk.Progressbar(root, maximum=100, mode = "indeterminate")
#indeterminate : 작업이 언제 끝날지 모름

#progressbar = ttk.Progressbar(root, maximum=100, mode = "determinate")
#indeterminate : 작업이 언제 끝날지 모름

#progressbar.start(10) # 10ms 마다 움직임
#progressbar.pack()

#def btncmd():
#    progressbar.stop() # 작동 중지

#btn = Button(root, text = "stop", command = btncmd)
#btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101): #1~100
        time.sleep(0.01)#0.01 초 대기

        p_var2.set(i) #이렇게만 하면 100 될 때까지 기다렸다가 한번에 반영
        progressbar2.update() #ui 업데이트
        print(p_var2.get())

btn = Button(root, text = "start", command = btncmd2)
btn.pack()
root.mainloop()
