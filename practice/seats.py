from tkinter import *
from time import sleep
from random import shuffle
from random import randrange
import tkinter.font as tkFont

def random_seats():
    global ori_people
    global people
    global seats_1
    global seats_2
    global seats_2_1
    global wait_time

    title.destroy()
    start_btn.destroy()
    
    wait = Label(win)

    x_dst = 0.10425
    y_dst = 0.12

    for i in range(wait_time):
        wait.config(text = wait_time - i, font = "맑은고딕 200")
        wait.place(relx = 0.5, rely = 0.5, anchor = "center")
        win.update()
        sleep(0)
    wait.destroy()

    contents = "김수인,김제니,김예은,김이경,김하빈,류이레,박서현,안유진,양가인,윤혜지,이수린,이윤아,이채연,진현진,차은솔,최혜린,강우현,김민호,김정윤,김주영,김현우,박보규,박성빈,박승재,박준용,신호영,이유찬,전지우,정은우"
    people = contents.split(',')

    for i in range(len(people)):
        ori_people[i] = people[i]
    shuffle(people)

    """
    rand_num = randrange(0,2)
    print("random number: ",rand_num)
    # 1. 1분단
    # 2. 2분단 1,2번
    # 3. 2분단 3번

    # 짝 O
    if rand_num == 1:
        while True:
            shuffle(people)
            if people.index("류이레") <= 14 and people.index("박준용") <= 14:
                if people.index("류이레") - people.index("박준용") == 5 \
                    or people.index("박준용") - people.index("류이레") == 5:
                    break
            elif people.index("류이레") <= 24 and people.index("박준용") <= 24:
                if people.index("류이레") <= 14 or people.index("박준용") <= 14:
                    continue
                if people.index("류이레") - people.index("박준용") == 5 \
                    or people.index("박준용") - people.index("류이레") == 5:
                    break
            else:
                if people.index("류이레") - people.index("박준용") == 4 \
                    or people.index("박준용") - people.index("류이레") == 4:
                    break
        num1 = people.index("류이레")
        num2 = people.index("박준용")

    # 짝 X
    while True:
        shuffle(people)
        if people.index("정은우") == people.index("류이레") or people.index("정은우") == people.index("박준용") \
            or people.index("강우현") == people.index("류이레") or people.index("강우현") == people.index("박준용"):
            continue
        if people.index("정은우") <= 14 and people.index("강우현") <= 14:
            if people.index("정은우") - people.index("강우현") == 5 \
                or people.index("정은우") - people.index("강우현") == 5:
                continue
        elif people.index("정은우") <= 24 and people.index("강우현") <= 24:
            if people.index("정은우") <= 14 or people.index("강우현") <= 14:
                break
            if people.index("정은우") - people.index("강우현") == 5 \
                or people.index("정은우") - people.index("강우현") == 5:
                continue
        else:
            if people.index("정은우") - people.index("강우현") == 4 \
                or people.index("정은우") - people.index("강우현") == 4:
                continue
        break

    temp_a = people.index("류이레")
    people[num1], people[temp_a] = people[temp_a], people[num1]
    temp_b = people.index("박준용")
    people[num2], people[temp_b] = people[temp_b], people[num2]
    """


    seats_1 = [0 for i in range(15)]
    for i in range(3):
        for j in range(5):
            seats_1[j + i * 3] = Label(win)
            seats_1[j + i * 3].config(text = people[0], relief = "solid", padx = 22, pady = 22)
            del people[0]
            if not i:
                x = 0.19
                y = 0.1 + j * y_dst
            elif i == 1:
                x = 0.19 + x_dst
                y = 0.1 + j * y_dst
            else:
                x = 0.19 + 2 * x_dst
                y = 0.1 + j * y_dst
            seats_1[j + i * 3].place(relx = x, rely = y, anchor = "center")
    seats_2 = [0 for i in range(10)]
    for i in range(2):
        for j in range(5):
            seats_2[j + i * 3] = Label(win)
            seats_2[j + i * 3].config(text = people[0], relief = "solid", padx = 22, pady = 22)
            del people[0]
            if not i:
                x = 0.595
                y = 0.1 + j * y_dst
            else:
                x = 0.595 + x_dst
                y = 0.1 + j * y_dst
            seats_2[j + i * 3].place(relx = x, rely = y, anchor = "center")
    seats_2_1 = [0 for i in range(4)]
    for i in range(4):
        seats_2_1[i] = Label(win)
        seats_2_1[i].config(text = people[0], relief = "solid", padx = 22, pady = 22)
        del people[0]
        x = 0.595 + x_dst * 2
        y = 0.22 + i * y_dst
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
wait_time = 5

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