from tkinter import *
from time import sleep
from random import shuffle
import tkinter.font as tkFont

def random_seats():
    global ori_people
    global people
    global seats_1
    global seats_2
    global seats_2_3
    global seats_3
    global wait_time

    title.destroy()
    start_btn.destroy()
    
    wait = Label(win)

    for i in range(wait_time):
        wait.config(text = wait_time - i, font = "맑은고딕 200")
        wait.place(relx = 0.5, rely = 0.5, anchor = "center")
        win.update()
        sleep(1)
    wait.destroy()

    contents = "김수인,김제니,김예은,김이경,김하빈,류이레,박서현,안유진,양가인,윤혜지,이수린,이윤아,이채연,진현진,차은솔,최혜린,강우현,김민호,김정윤,김주영,김현우,박보규,박성빈,박승재,박준용,신호영,이유찬,전지우,정은우"
    people = contents.split(',')

    for i in range(len(people)):
        ori_people[i] = people[i]
    shuffle(people)

    seats_1 = [0 for i in range(15)]
    for i in range(3):
        for j in range(5):
            seats_1[j + i * 3] = Label(win)
            seats_1[j + i * 3].config(text = people[0], relief = "solid", padx = 22, pady = 22)
            del people[0]
            if not i:
                x = 0.2
                y = 0.1 + j * 0.12
            elif i == 1:
                x = 0.3
                y = 0.1 + j * 0.12
            else:
                x = 0.4
                y = 0.1 + j * 0.12
            seats_1[j + i * 3].place(relx = x, rely = y, anchor = "center")
    seats_2 = [0 for i in range(12)]
    for i in range(3):
        for j in range(4):
            seats_2[j + i * 3] = Label(win)
            seats_2[j + i * 3].config(text = people[0], relief = "solid", padx = 22, pady = 22)
            del people[0]
            if not i:
                x = 0.595
                y = 0.22 + j * 0.12
            elif i == 1:
                x = 0.6995 # 0.1045
                y = 0.22 + j * 0.12
            else:
                x = 0.8037
                y = 0.22 + j * 0.12
            seats_2[j + i * 3].place(relx = x, rely = y, anchor = "center")
    seats_2_1 = [0 for i in range(2)]
    for i in range(2):
        seats_2_1[i] = Label(win)
        seats_2_1[i].config(text = people[0], relief = "solid", padx = 22, pady = 22)
        del people[0]
        if not i:
            x = 0.595
            y = 0.099
        else:
            x = 0.699
            y = 0.099
        seats_2_1[i].place(relx = x, rely = y, anchor = "center")
    end_btn.place(relx = 0.5, rely = 0.8, anchor = "center")


def end():
    win.destroy()


win = Tk()
win.option_add("*Font", "맑은고딕 40")
win.title("자리 배치 프로그램")
win.geometry("{}x{}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight()))

ori_people = [0 for i in range(29)]
people = []
seats_1 = []
seats_2 = []
seats_2_1 = []
wait_time = 0

title = Label(win)
title_font = tkFont.Font(family = "맑은고딕", size = 80)
title.config(text = "자리 배치 프로그램", font = title_font)
title.place(relx = 0.5, rely = 0, anchor = 'n')

start_btn = Button(win)
start_btn.config(text = "시작", command = random_seats)
start_btn.place(relx = 0.5, rely = 0.8, anchor = "center")

end_btn = Button(win)
end_btn.config(text = "닫기", command = end)

win.mainloop()