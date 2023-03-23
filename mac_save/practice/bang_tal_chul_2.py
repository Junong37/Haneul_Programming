from tkinter import * # tkinter 불러오기
import time

def start(): # 시작 함수
    try: # try except 구문으로 에러메세지 지우기
        error_lab.destroy()
    except:
        pass

    lab_title.destroy() # 제목 지우기
    start_btn.destroy() # 스타트 버튼 지우기
    
    response.config(text = "내 보물을 훔치려 하다니 너흰 이제 끝이야! ")
    response.place(relx = 0.5, rely = 0.4, anchor = "center")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second: # while문 활용
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")

    response.config(text = "음..이건 좀 심했나?")
    response.place(relx = 0.5, rely = 0.4, anchor = "center")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second: # while문 활용
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")



    text.config(text = "그래도 괘씸하니까 나랑 좀 놀아줘\n간단하게 퀴즈를 맞히는거야. 어때??") # 내용
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    
    btn_1.config(text = "엑 싫어; 니가 뭔데", font = "맑은고딕 20") # 선택지1
    btn_1.config(width = int(win_width), height = 1)
    btn_1.config(justify = "left")
    btn_1.config(command = scene_1_1)
    btn_1.place(relx = 0.25, rely = 0.6, anchor = "sw")

    btn_2.config(text = "야레야레 문제라니 설레는구만..ㅋ", font = "맑은고딕 20") # 선택지2
    btn_2.config(width = int(win_width), height = 1)
    btn_2.config(command = scene_1_2)
    btn_2.place(relx = 0.25, rely = 0.7, anchor = "sw")


def scene_1_1():
    response.config(text = "실망이야..다시 해보도록 해")
    response.place(relx = 0.5, rely = 0.4, anchor = "center")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second: # while문 활용
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")

    win.destroy()

def scene_1_2():
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    response.config(text = "좀 치는 아이구나?\n좋아 그럼 바로 게임을 시작할게!")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()

    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "첫 번째 문제야.\n “PYTHON”을 올바르게 발음한 것은?")
    
    btn_1.config(text = "파이똔", command = scene_2_1) # 선택지 1
    btn_1.place(relx = 0.25, rely = 0.6, anchor = "sw")
    btn_2.config(text = "피와이티에이치오엔", command = scene_2_2) # 선택지 2
    btn_2.place(relx = 0.25, rely = 0.7, anchor = "sw")
    btn_3.config(text = "파이썬", font = "맑은고딕 20") # 선택지 3
    btn_3.config(width = int(win_width), height = 1)
    btn_3.place(relx = 0.25, rely = 0.8, anchor = "sw")
    btn_3.config(command = scene_2_3)




def scene_2_1():
    global score
    score += 10
    response.config(text = "..겠냐? ㅋㅋㅋ 다시해봐!")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()

    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "첫 번째 문제야.\n “PYTHON”을 올바르게 발음한 것은?")


def scene_2_2():
    global score
    score += 10
    response.config(text = "맞는거 같아? 난 아니라고 생각하는데? ㅋ\n 다시 해봐!")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()

    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "첫 번째 문제야.\n “PYTHON”을 올바르게 발음한 것은?")


def scene_2_3():
    global score
    score += 1
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    response.config(text = "음..틀렸어..")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    response.config(text = "라고 할뻔~")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    btn_3.place_forget()

    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "어때? 쉽지? 이런식으로 쭉 하면 돼!")
    
    btn_1.config(text = "간단하네! 재밌다!", command = scene_3_1)
    btn_1.place(relx = 0.25, rely = 0.6, anchor = "sw")
    btn_2.config(text = "으음..;; 알겠어 빨리 하자", command = scene_3_2)
    btn_2.place(relx = 0.25, rely = 0.7, anchor = "sw")


def scene_3_1():
    global score
    score += 1
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    response.config(text = "게임을 즐길줄 아는 친구구나! \n 좀 뜬금없긴 해도 기억해둬..내 생일은 8월 20일이야^^")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()

    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "좋아! 그럼 두번째 퀴즈!\n 알고리즘의 동아리 이적 부원은 몇명이게?")
    
    btn_1.config(text = "0명", command = scene_4_1)
    btn_1.place(relx = 0.25, rely = 0.6, anchor = "sw")
    btn_2.config(text = "3명", command = scene_4_2)
    btn_2.place(relx = 0.25, rely = 0.7, anchor = "sw")
    btn_3.config(text = "5명", command = scene_4_3)
    btn_3.place(relx = 0.25, rely = 0.8, anchor = "sw")

def scene_3_2():
    global score
    score += 2
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    response.config(text = "너무 서두르지마ㅎ 역시 한국인인건가?")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()

    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "좋아! 그럼 두번째 퀴즈!\n 알고리즘의 동아리 이적 부원은 몇명이게?")
    
    btn_1.config(text = "0명", command = scene_4_1)
    btn_1.place(relx = 0.25, rely = 0.6, anchor = "sw")
    btn_2.config(text = "3명", command = scene_4_2)
    btn_2.place(relx = 0.25, rely = 0.7, anchor = "sw")
    btn_3.config(text = "5명", command = scene_4_3)
    btn_3.place(relx = 0.25, rely = 0.8, anchor = "sw")

def scene_4_1():
    global score
    score += 1
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    response.config(text = "정답!! 이러니까 알고리즘이 갓동이지! 그치?")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "하늘고 매점 요맘때 3개의 가격은 몇개게?")

    input_ent.place(relx=0.5, rely=0.5, anchor="center")
    enter_button.config(command=scene_test_4)
    enter_button.place(relx=0.5, rely=0.6, anchor="center")

def scene_4_2():
    global score
    score += 6
    response.config(text = "...음 다시해볼래?")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()

    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "좋아! 그럼 두번째 퀴즈!\n 알고리즘의 동아리 이적 부원은 몇명이게?")

def scene_4_3():
    global score
    score += 10
    response.config(text = "하하..그건 망동 아니니?")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "좋아! 그럼 두번째 퀴즈!\n 알고리즘의 동아리 이적 부원은 몇명이게?")

def scene_test_4():
    if input_ent.get() == "3600":
        scene_4_5()
    else:
        scene_4_4()

def scene_4_4():
    global score
    score += 10
    text.place_forget()
    enter_button.place_forget()
    input_ent.place_forget()
    response.config(text = "틀렸어!")
    response.place(relx = 0.5, rely = 0.3, anchor = "n")
    input_ent.delete(0, 'end')
    win.update()
    time.sleep(wait_second)
    text.place(relx=0.5, rely=0.2, anchor="n")
    response.place_forget()
    enter_button.place(relx=0.5, rely=0.6, anchor="center")
    input_ent.place(relx=0.5, rely=0.5, anchor="center")

def scene_4_5():
    global score
    score += 1
    input_ent.place_forget()
    text.place_forget()
    enter_button.place_forget()
    input_ent.delete(0, 'end')
    response.config(text="맞았어!")
    response.place(relx=0.5, rely=0.3, anchor="n")
    win.update()
    time.sleep(wait_second)
    response.place_forget()

    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "따뜻하고 폭신한 물체를 잘 찾아봐!")
    text.place(relx=0.5, rely=0.2, anchor="n")
    input_ent.place(relx=0.5, rely=0.5, anchor="center")
    enter_button.config(command=scene_test_5)
    enter_button.place(relx=0.5, rely=0.6, anchor="center")

def scene_test_5():
    if input_ent.get() == "31":
        scene_4_7()
    else:
        scene_4_6()

def scene_4_6():
    global score
    score += 10
    text.place_forget()
    enter_button.place_forget()
    input_ent.place_forget()
    response.config(text = "틀렸어!")
    response.place(relx = 0.5, rely = 0.3, anchor = "n")
    input_ent.delete(0, 'end')
    win.update()
    time.sleep(wait_second)
    text.place(relx=0.5, rely=0.2, anchor="n")
    response.place_forget()
    enter_button.place(relx=0.5, rely=0.6, anchor="center")
    input_ent.place(relx=0.5, rely=0.5, anchor="center")

def scene_4_7():
    global score
    score += 1
    enter_button.place_forget()
    input_ent.place_forget()
    response.config(text = "맞았어!")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "자! 이제 마지막문제야! 이번엔 기회가 한번이야!\n        “알고리즘의 목적은?”")

    btn_1.config(text = "연애", command = scene_5_1)
    btn_1.place(relx = 0.25, rely = 0.6, anchor = "sw")
    btn_2.config(text = "파이썬 마스터", command = scene_5_2)
    btn_2.place(relx = 0.25, rely = 0.7, anchor = "sw")
    btn_3.config(text = "롤(League Of Legend)", command = scene_5_3)
    btn_3.place(relx = 0.25, rely = 0.8, anchor = "sw")

def scene_5_1():
    global score
    score += 5
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    response.config(text = "하하...어째서 눈물이.. 아쉽게도 아니야")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()

    btn_1.place(relx = 0.25, rely = 0.6, anchor = "sw")
    btn_1.config(text='다음', command= end)

def scene_5_2():
    global score
    score += 1
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    response.config(text = "그렇지! 맞아 정답이야!!")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()

    btn_1.place(relx = 0.25, rely = 0.6, anchor = "sw")
    btn_1.config(text='다음', command= end)

def scene_5_3():
    global score
    score += 100
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    response.config(text = "ㅎ...ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ 그러셔?\n내가 너 이름 저장해놓음 ㅅㄱ")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()

    btn_1.place(relx = 0.25, rely = 0.6, anchor = "sw")
    btn_1.config(text='다음', command= end)

def end(): # 엔딩 씬
    global dot_num
    btn_1.destroy()
    date.destroy()
    response.destroy()
    text.place_forget()
    
    dot.place(relx = 0.5, rely = 0.5, anchor = "center")
    for i in range(dot_num + 1): # for문 활용
        dot.config(text = "." * i, font = "맑은고딕 50")
        win.update()
        time.sleep(1)
    
    dot.destroy()
    text.place(relx = 0.5, rely = 0.5, anchor = "center")
    if score <= 7:
        text.config(text = "잘했어! 지금까지 다 맞았네! 그럼 힌트를 주도록 할께에 \n 뒤를 돌아봐. 누가 보여? \n그 사람에게 4자리 비밀번호를 말해!\n그럼 무운을 빌게!!")
    elif 7 < score <= 100:
        text.config(text = "다 맞히지는 못했지만 잘했어! \n그럼, 잘 탈출해봐! 무운을 빌게!")
    else:
        text.config(text = "...탈출해봐 ㅋ 평생 갇혀있지 말고")

    close_btn = Button(win)
    close_btn.config(text = "끝", command = close)
    close_btn.place(relx = 0.5, rely = 0.8, anchor = "center")

def close(): # 창 닫기
    win.destroy()

win = Tk() # 창 생성

# 변수
score = 0
name = ""
dot_num = 3
wait_second = 2

win_width = int(win.winfo_width() * 0.33) # int 활용

win.option_add("*Font", "맑은고딕 25") # 폰트
win.title("어서와! 이런곳은 처음이지?") # 제목
win.geometry("1000x500") # 창 크기


error_lab = Label(win) # 이름 에러 메세지
error_lab.config(text = "이름을 입력하세요")

# 위젯 미리 생성
response = Label(win)
date = Label(win)
text = Label(win)
text.config(justify = "left")
btn_1 = Button(win)
btn_2 = Button(win)
btn_3 = Button(win)
dot = Label(win)

# 입력칸
input_ent = Entry(win)

# 제목
lab_title = Label(win)
lab_title.config(text = "어서와! 이런곳은 처음이지?", font = "맑은고딕 40")
lab_title.place(relx = 0.5, rely = 0.06, anchor = "center")

# 스타트 버튼
start_btn = Button(win)
start_btn.config(text = "시작", command = start)
start_btn.place(relx = 0.5, rely = 0.9, anchor = "center")

enter_button = Button()
enter_button.config(text="입력")

win.mainloop() # 창 띄우기