from tkinter import *
import time

text1 = """케빈: 내 보물을 훔치려 하다니 너흰 이제 끝이야! 
이건 좀 심한가..?  그래도 괘씸하니까 나랑 좀 놀아줘
놀이는 간단해 내가 제시하는 문제를 맞추는 거야
*
엑 싫어; 니가 뭔데

야레야레 문제라니 설레는구만..ㅋ
*
실망이야..#

케빈: 좋아좋아 그럼 바로 게임을 시작할게!
첫 번째 문제야
“PYTHON”을 올바르게 발음한 것은?
*
파이똔

바이든

파이썬
*
음,, 다시 생각해봐!#

ㅋㅋㅋㅋㅋ 이러네#

틀렸어!.........
라고 할 뻔 ~
어때 쉽지? 이런식으로 하면 돼!
*
좋아! 그럼 두 번째 문제
“12기 알고리즘 탈퇴 부원은 몇명일까?”
*
맞아! 역시 알고리즘은 갓동이지 그치?

이런..다시해봐#

으음…그건 망동 아니니? 알고리즘은 갓동이라구!
다시 한 번 풀어봐#
*
자! 이제 마지막문제야!
""" # *, \n\n으로 대사 구분

text1 = text1.split("\n*\n")

for i in range(len(text1)):
    if "\n\n" in text1[i]:
        text1[i] = text1[i].split("\n\n")

print(text1)

def ready():
    lab_title.destroy()
    start_btn.destroy()
    start(0)

def start(scene_num):
    text.config(text=text1[scene_num])
    text.place(relx=0.5, rely=0.2, anchor="center")

    if len(text1[scene_num + 1]) == 2:
        btn_1.config(text=text1[scene_num + 1][0])
        btn_1.config(width = int(win_width), height = 1)
        btn_1.config(command=lambda: start(scene_num + 2))
        btn_1.place(relx=0.5, rely=0.7, anchor = "center")

        btn_2.config(text=text1[scene_num + 1][1])
        btn_2.config(width = int(win_width), height = 1)
        btn_2.place(relx=0.5, rely=0.8, anchor = "center")
    else:
        btn_1.config(text=text1[scene_num + 1][0])
        btn_1.config(width = int(win_width), height = 1)
        btn_1.place(relx=0.5, rely=0.7, anchor = "center")

        btn_2.config(text=text1[scene_num + 1][1])
        btn_2.config(width = int(win_width), height = 1)
        btn_2.place(relx=0.5, rely=0.8, anchor = "center")

        btn_3.config(text=text1[scene_num + 1][2])
        btn_3.config(width = int(win_width), height = 1)
        btn_3.place(relx=0.5, rely=0.9, anchor = "center")

win = Tk() # 창 생성

# 변수
score = 0
dot_num = 3
wait_second = 2

win_width = int(win.winfo_width() * 0.33) # int 활용

win.option_add("*Font", "맑은고딕 50") # 폰트
win.title("방탈출") # 제목
win.geometry("{}x{}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight())) # 창 크기

# 위젯 미리 생성
response = Label(win)
date = Label(win)
text = Label(win)
text.config(justify = "left")
btn_1 = Button(win)
btn_2 = Button(win)
btn_3 = Button(win)
dot = Label(win)

# 제목
lab_title = Label(win)
lab_title.config(text = "방탈출", font = "맑은고딕 100")
lab_title.place(relx = 0.5, rely = 0.1, anchor = "center")

# 스타트 버튼
start_btn = Button(win)
start_btn.config(text = "시작", command = ready)
start_btn.place(relx = 0.5, rely = 0.9, anchor = "center")

win.mainloop() # 창 띄우기