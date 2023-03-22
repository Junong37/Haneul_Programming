from tkinter import *
import time

def start():
    start_btn.destroy()
    
    i = 0
    while True:
        label_list[i%len(text1)].place(relx=0.5, rely=0.5, anchor="center")
        win.update()
        time.sleep(0.05)
        label_list[i%len(text1)].place_forget()
        i += 1

win = Tk()

win.option_add("*Font", "맑은고딕 100")
win.title("생일")
win.geometry("900x500")

start_btn = Button()
start_btn.config(command=start, text="눌러")
start_btn.place(relx=0.5, rely = 0.8, anchor = "center")

text1 = "파이썬어떻게가르치지"

label_list = [Label() for i in range(len(text1))]

for i in range(len(text1)):
    label_list[i].config(text=text1[i], font="맑은고딕 500")

win.mainloop()