from tkinter import *
import time

def start():
    global i
    global j
    global speed

    button1.place_forget()
    record_button.place(relx=0.5, rely=0.7, anchor="center")
    spd1_button.place(relx=0.2, rely=0.9, anchor="center")
    spd2_button.place(relx=0.5, rely=0.9, anchor="center")
    spd20_button.place(relx=0.8, rely=0.9, anchor="center")
    reset_button.place(relx=0.8, rely=0.7, anchor="center")

    i = 0
    j = 0
    while True:
        if i >= 60:
            i = 0
            j += 1
        label1.config(text=str(i) + "초")
        label2.config(text=str(j) + "분")
        win.update()
        time.sleep(1 / speed)
        i += 1

def record():
    global i
    global j

    record_label.config(text="{}분 {}초".format(j, i))

def spd2():
    global speed
    speed = 2

def spd1():
    global speed
    speed = 1

def spd20():
    global speed
    speed = 20

def reset():
    global i
    global j

    i = 0
    j = 0

win = Tk()

i = 0
j = 0
speed = 1

title = Label()
title.config(text="스톱워치", font="맑은고딕 20")
title.place(relx=0.5, rely=0, anchor="n")

label1 = Label()
label1.config(text="world")
label1.place(relx=0.5, rely=0.5, anchor="center")

label2 = Label()
label2.config(text="hello")
label2.place(relx=0.5, rely=0.4, anchor="center")

record_label = Label()
record_label.place(relx=0.5, rely=0.6, anchor="center")

button1 = Button()
button1.config(text="시작", command=start)
button1.place(relx=0.5, rely=0.8, anchor="center")

spd1_button = Button()
spd1_button.config(text="속도 x1", command=spd1)

spd2_button = Button()
spd2_button.config(text="속도 x2", command=spd2)

spd20_button = Button()
spd20_button.config(text="속도 x20", command=spd20)

record_button = Button()
record_button.config(text="기록", command=record)

reset_button = Button()
reset_button.config(text="리셋", command=reset)

win.mainloop()