from tkinter import * # tkinter 불러오기
import time

def start(): # 시작 함수
    global name # 주인공 이름
    name = name_ent.get() # str 활용
    if not name: # bool 활용
        error_lab.place(relx = 0.5, rely = 0.3, anchor = "center") # 이름 안쓰면 에러 메세지 띄우기
    else:
        try: # try except 구문으로 에러메세지 지우기
            error_lab.destroy()
        except:
            pass
        date.config(text = "3월 2일") # 날짜 설정
        date.place(relx = 0, rely = 0, anchor = "nw") # 날짜 배치
        
        name_ent.destroy() # 이름 입력칸 지우기
        lab_title.destroy() # 제목 지우기
        start_btn.destroy() # 스타트 버튼 지우기
        
        text.config(text = "새학기에 앞에 앉아있는 남자애가 뒤를 돌아봤다.\n인사를 해야겠다") # 내용
        text.place(relx = 0.5, rely = 0.2, anchor = "n")
        
        btn_1.config(text = "뭘 봐", font = "맑은고딕 20") # 선택지1
        btn_1.config(width = int(win_width), height = 1)
        btn_1.config(justify = "left")
        btn_1.config(command = scene_1_1)
        btn_1.place(relx = 0, rely = 0.8, anchor = "sw")

        btn_2.config(text = "수줍게 안녕", font = "맑은고딕 20") # 선택지2
        btn_2.config(width = int(win_width), height = 1)
        btn_2.config(command = scene_1_2)
        btn_2.place(relx = 0, rely = 0.9, anchor = "sw")

        btn_3.config(text = "하이 에이치 아이", font = "맑은고딕 20") # 선택지3
        btn_3.config(width = int(win_width), height = 1)
        btn_3.config(command = scene_1_3)
        btn_3.place(relx = 0, rely = 1, anchor = "sw")

def scene_1_1():
    global score
    score += 2 # 점수 올리기
    response.config(text = "그 아이가 눈을 피하며 운다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "center")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second: # while문 활용
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")

    date.config(text = "3월 3일")
    text.config(text = "수업이 시작되고 나는 준성이를 생각하느라 내용은 하나도 못들었다.\n준성이는 피곤한지 졸고 있다.\n조는 모습도 너무 귀엽다.\n마침 내 가방에 마이쮸가 있다.")
    
    btn_1.config(text = "포도맛", command = scene_2_1)
    btn_2.config(text = "사과맛", command = scene_2_2)
    btn_3.config(text = "복숭아맛", command = scene_2_3)

def scene_1_2():
    global score
    score += 10
    response.config(text = "그 아이가 인사를 한다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")

    date.config(text = "3월 3일")
    text.config(text = "수업이 시작되고 나는 준성이를 생각하느라 내용은 하나도 못들었다.\n준성이는 피곤한지 졸고 있다.\n조는 모습도 너무 귀엽다.\n마침 내 가방에 마이쮸가 있다.")
    
    btn_1.config(text = "포도맛", command = scene_2_1)
    btn_2.config(text = "사과맛", command = scene_2_2)
    btn_3.config(text = "복숭아맛", command = scene_2_3)

def scene_1_3():
    global score
    score += 6
    response.config(text = "마스크 밖으로 황당한 표정이 흘러나왔지만 그 아이가 인사를 한다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")

    date.config(text = "3월 3일")
    text.config(text = "수업이 시작되고 나는 준성이를 생각하느라 내용은 하나도 못들었다.\n준성이는 피곤한지 졸고 있다.\n조는 모습도 너무 귀엽다.\n마침 내 가방에 마이쮸가 있다.")
    
    btn_1.config(text = "포도맛", command = scene_2_1)
    btn_2.config(text = "사과맛", command = scene_2_2)
    btn_3.config(text = "복숭아맛", command = scene_2_3)

def scene_2_1():
    global score
    score += 10
    response.config(text = "준성이가 기뻐하며 고마워라고 말했다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "점심시간이 한참 남았는데 벌써 배가 고프다.\n준성이 앞에서 꼬르륵 소리가 나면 부끄러우니 매점에 가야겠다.\n준성이가 복도로 나간다. \n{}: “매점 같이 갈래?”\n준성: “좋아”\n어색한데 무슨 말을 꺼내야할까?".format(name))
    
    btn_1.config(text = "너 파이썬 할 줄 아니?", command = scene_3_1)
    btn_2.config(text = "하늘고에서 연애할 생각 있어?", command = scene_3_2)
    btn_3.config(text = "너 모쏠 이지?", command = scene_3_3)

def scene_2_2():
    global score
    score += 5
    response.config(text = "준성이가 마이쮸를 까서 먹었다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "점심시간이 한참 남았는데 벌써 배가 고프다.\n준성이 앞에서 꼬르륵 소리가 나면 부끄러우니 매점에 가야겠다.\n준성이가 복도로 나간다. \n{}: “매점 같이 갈래?”\n준성: “좋아”\n어색한데 무슨 말을 꺼내야할까?".format(name))
    
    btn_1.config(text = "너 파이썬 할 줄 아니?", command = scene_3_1)
    btn_2.config(text = "하늘고에서 연애할 생각 있어?", command = scene_3_2)
    btn_3.config(text = "너 모쏠 이지?", command = scene_3_3)

def scene_2_3():
    global score
    score += 1
    response.config(text = "준성이 심기가 불편해 보인다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "점심시간이 한참 남았는데 벌써 배가 고프다.\n준성이 앞에서 꼬르륵 소리가 나면 부끄러우니 매점에 가야겠다.\n준성이가 복도로 나간다. \n{}: “매점 같이 갈래?”\n준성: “좋아”\n어색한데 무슨 말을 꺼내야할까?".format(name))
    
    btn_1.config(text = "너 파이썬 할 줄 아니?", command = scene_3_1)
    btn_2.config(text = "하늘고에서 연애할 생각 있어?", command = scene_3_2)
    btn_3.config(text = "너 모쏠 이지?", command = scene_3_3)

def scene_3_1():
    global score
    score += 5
    date.config(text = "3월 4일")
    response.config(text = "약간 당황하면서도 싫어하진 않는거 같다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "종례가 끝났다.\n오늘은 201에 가서 딴짓을 할 예정이다.\n사람1: “준성아 너 어디가?”\n준성: “ 나 201”\n이건 기회다")
    
    btn_1.config(text = "준성아 나랑 201 갈래?", command = scene_4_1)
    btn_2.config(text = "준성아 너 컴퓨터 뺏꼈지 않아?", command = scene_4_2)
    btn_3.config(text = "제갈준성 같이가!", command = scene_4_3)

def scene_3_2():
    global score
    score += 10
    date.config(text = "3월 4일")
    response.config(text = "준성: “하고 싶긴 한데 좋아하는 사람이 딱히 없어서”")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "종례가 끝났다.\n오늘은 201에 가서 딴짓을 할 예정이다.\n사람1: “준성아 너 어디가?”\n준성: “ 나 201”\n이건 기회다")
    
    btn_1.config(text = "준성아 나랑 201 갈래?", command = scene_4_1)
    btn_2.config(text = "준성아 너 컴퓨터 뺏꼈지 않아?", command = scene_4_2)
    btn_3.config(text = "제갈준성 같이가!", command = scene_4_3)

def scene_3_3():
    global score
    score += 2
    date.config(text = "3월 4일")
    response.config(text = "준성이가 슬퍼하며 어… 라고 말했다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "종례가 끝났다.\n오늘은 201에 가서 딴짓을 할 예정이다.\n사람1: “준성아 너 어디가?”\n준성: “ 나 201”\n이건 기회다")
    
    btn_1.config(text = "준성아 나랑 201 갈래?", command = scene_4_1)
    btn_2.config(text = "준성아 너 컴퓨터 뺏꼈지 않아?", command = scene_4_2)
    btn_3.config(text = "제갈준성 같이가!", command = scene_4_3)

def scene_4_1():
    global score
    score += 10
    response.config(text = "준성이가 웃으면서 알겠다고 말했다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "면학 1타임이 끝났다.\n간식을 받으러 가야하는데 준성이랑 같이 가고 싶다….\n마침 준성이가 지나가고 있다.\n무슨 말을 해야 준성이랑 같이 갈수 있을까?")
    
    btn_1.config(text = "준성아 너 간식 신청했어? 같이 갈래?", command = scene_5_1)
    btn_2.config(text = "간식 받고 테라스 가서 놀래?", command = scene_5_2)
    btn_3.config(text = "(면학실 앞에서 큰 소리로) 나랑 간식 먹을 사람!", command = scene_5_3)

def scene_4_2():
    global score
    score += 2
    response.config(text = "준성이가 살짝 불편해하는거 같다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "면학 1타임이 끝났다.\n간식을 받으러 가야하는데 준성이랑 같이 가고 싶다….\n마침 준성이가 지나가고 있다.\n무슨 말을 해야 준성이랑 같이 갈수 있을까?")
    
    btn_1.config(text = "준성아 너 간식 신청했어? 같이 갈래?", command = scene_5_1)
    btn_2.config(text = "간식 받고 테라스 가서 놀래?", command = scene_5_2)
    btn_3.config(text = "(면학실 앞에서 큰 소리로) 나랑 간식 먹을 사람!", command = scene_5_3)

def scene_4_3():
    global score
    score += 5
    response.config(text = "준성이가 살짝 부담스러워 했지만 같이 가기로 했다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "면학 1타임이 끝났다.\n간식을 받으러 가야하는데 준성이랑 같이 가고 싶다….\n마침 준성이가 지나가고 있다.\n무슨 말을 해야 준성이랑 같이 갈수 있을까?")
    
    btn_1.config(text = "준성아 너 간식 신청했어? 같이 갈래?", command = scene_5_1)
    btn_2.config(text = "간식 받고 테라스 가서 놀래?", command = scene_5_2)
    btn_3.config(text = "(면학실 앞에서 큰 소리로) 나랑 간식 먹을 사람!", command = scene_5_3)

def scene_5_1():
    global score
    score += 5
    date.config(text = "3월 5일")
    response.config(text = "준성이랑 같이 간식을 받고 헤어졌다. 이게 아니였는데;")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "면학이 끝났다. 기숙사에 가려는데 바로 앞에 준성이가 보인다.\n같이... 갈까?\n가즈아.\n{}: “준성아, 너 혹시 혼자 가니?”".format(name))
    
    btn_1.config(text = "친구가 없나 보구나!", command = scene_6_1)
    btn_2.config(text = "그럼…나랑 같이 갈래?", command = scene_6_2)
    btn_3.config(text = "잘가!", command = scene_6_3)

def scene_5_2():
    global score
    score += 10
    date.config(text = "3월 5일")
    response.config(text = "간식을 받아서 준성이랑 테라스에서 여러 얘기를 했다. 많이 친해진 것 같다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "면학이 끝났다. 기숙사에 가려는데 바로 앞에 준성이가 보인다.\n같이... 갈까?\n가즈아.\n{}: “준성아, 너 혹시 혼자 가니?”".format(name))
    
    btn_1.config(text = "친구가 없나 보구나!", command = scene_6_1)
    btn_2.config(text = "그럼…나랑 같이 갈래?", command = scene_6_2)
    btn_3.config(text = "잘가!", command = scene_6_3)

def scene_5_3():
    global score
    score += 2
    date.config(text = "3월 5일")
    response.config(text = "준성이가 이상한 사람 보듯이 쳐다봤다 혼자 먹는 간식이지만 참 맛있었다…\n눈물맛이 섞여서 그런가…")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "면학이 끝났다. 기숙사에 가려는데 바로 앞에 준성이가 보인다.\n같이... 갈까?\n가즈아.\n{}: “준성아, 너 혹시 혼자 가니?”".format(name))
    
    btn_1.config(text = "친구가 없나 보구나!", command = scene_6_1)
    btn_2.config(text = "그럼…나랑 같이 갈래?", command = scene_6_2)
    btn_3.config(text = "잘가!", command = scene_6_3)

def scene_6_1():
    global score
    score += 0
    date.config(text = "3월 6일")
    response.config(text = "준성이가 상처받은 것 같다… 대답도 안하고 가버렸다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "저녁시간을 알리는 종이 울렸다.\n오늘 저녁은 맛있는 게 나오기 때문에 준성이를 데리고 급식실에 왔다.\n같이 밥을 먹는데 준성이가 옷에 음식을 흘렸다\n{}: “헉. 괜찮아?”\n준성: “아..괜찮아. 흰 티인데 걱정이네”".format(name))
    
    btn_1.config(text = "안 그래도 냄새났는데 잘됐다. 이참에 좀 빨아", command = scene_7_1)
    btn_2.config(text = "아.. 유감이야", command = scene_7_2)
    btn_3.config(text = "아구.. 내가 얼른 물티슈 가져올게! 잠깐만ㅎㅎ", command = scene_7_3)

def scene_6_2():
    global score
    score += 10
    date.config(text = "3월 6일")
    response.config(text = "준성이와 같이 걸어가는 이 길이 너무 짧았다. 오늘 잠은 다 잔듯하다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "저녁시간을 알리는 종이 울렸다.\n오늘 저녁은 맛있는 게 나오기 때문에 준성이를 데리고 급식실에 왔다.\n같이 밥을 먹는데 준성이가 옷에 음식을 흘렸다\n{}: “헉. 괜찮아?”\n준성: “아..괜찮아. 흰 티인데 걱정이네”".format(name))
    
    btn_1.config(text = "안 그래도 냄새났는데 잘됐다. 이참에 좀 빨아", command = scene_7_1)
    btn_2.config(text = "아.. 유감이야", command = scene_7_2)
    btn_3.config(text = "아구.. 내가 얼른 물티슈 가져올게! 잠깐만ㅎㅎ", command = scene_7_3)

def scene_6_3():
    global score
    score += 2
    date.config(text = "3월 6일")
    response.config(text = "준성이도 잘가!라고 인사해줬다. 역시 용기내길 잘한 것 같다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "저녁시간을 알리는 종이 울렸다.\n오늘 저녁은 맛있는 게 나오기 때문에 준성이를 데리고 급식실에 왔다.\n같이 밥을 먹는데 준성이가 옷에 음식을 흘렸다\n{}: “헉. 괜찮아?”\n준성: “아..괜찮아. 흰 티인데 걱정이네”".format(name))
    
    btn_1.config(text = "안 그래도 냄새났는데 잘됐다. 이참에 좀 빨아", command = scene_7_1)
    btn_2.config(text = "아.. 유감이야", command = scene_7_2)
    btn_3.config(text = "아구.. 내가 얼른 물티슈 가져올게! 잠깐만ㅎㅎ", command = scene_7_3)

def scene_7_1():
    global score
    score += 0
    date.config(text = "3월 10일")
    response.config(text = "준성이가 밥을 남기고 일찍 자리에서 나왔다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "오늘은 대망의 고백날이다.\n떨리는 마음으로 준성이를 간식시간에 불렀다\n저기 멀리서 준성이가 걸어온다.\n{}: “왔어? 하고 싶은 말이 있어서 불렀어”\n준성: “무슨 말?”\n{}: “나 너 좋아해. 우리 사귈래?”".format(name, name))
    
    btn_1.config(text = "결과 보기", command = end)
    btn_2.destroy()
    btn_3.destroy()

def scene_7_2():
    global score
    score += 3
    date.config(text = "3월 10일")
    response.config(text = "준성이의 표정이 좋지는 않아보였지만 밥을 같이 먹었다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "오늘은 대망의 고백날이다.\n떨리는 마음으로 준성이를 간식시간에 불렀다\n저기 멀리서 준성이가 걸어온다.\n{}: “왔어? 하고 싶은 말이 있어서 불렀어”\n준성: “무슨 말?”\n{}: “나 너 좋아해. 우리 사귈래?”".format(name, name))
    
    btn_1.config(text = "결과 보기", command = end)
    btn_2.destroy()
    btn_3.destroy()

def scene_7_3():
    global score
    score += 10
    date.config(text = "3월 10일")
    response.config(text = "준성이가 조금은 부끄러워하면서도 고마워했다.")
    response.place(relx = 0.5, rely = 0.4, anchor = "n")
    now = time.time()
    text.place_forget()
    win.update()
    while time.time() - now < wait_second:
        pass
    response.place_forget()
    text.place(relx = 0.5, rely = 0.2, anchor = "n")
    text.config(text = "오늘은 대망의 고백날이다.\n떨리는 마음으로 준성이를 간식시간에 불렀다\n저기 멀리서 준성이가 걸어온다.\n{}: “왔어? 하고 싶은 말이 있어서 불렀어”\n준성: “무슨 말?”\n{}: “나 너 좋아해. 우리 사귈래?”".format(name, name))
    
    btn_1.config(text = "결과 보기", command = end)
    btn_2.destroy()
    btn_3.destroy()

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
    if score >= 45:
        text.config(text = "HAPPY ENDING")
    elif score >= 25:
        text.config(text = "준성이와는 친구로 지내기로 했다. 봄이었다.")
    else:
        text.config(text = "준성이와 화장실에서 만났다. 인사했는데 씹혔다… 아…")

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
win.title("하늘고에서 연애하기") # 제목
win.geometry("894x500") # 창 크기


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

# 이름 입력칸
name_ent = Entry(win)
name_ent.place(relx = 0.5, rely = 0.4, anchor = "center")
name = name_ent.get()

# 제목
lab_title = Label(win)
lab_title.config(text = "하늘고에서 연애하기", font = "맑은고딕 40")
lab_title.place(relx = 0.5, rely = 0.06, anchor = "center")

# 스타트 버튼
start_btn = Button(win)
start_btn.config(text = "시작", command = start)
start_btn.place(relx = 0.5, rely = 0.9, anchor = "center")

win.mainloop() # 창 띄우기