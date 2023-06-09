#트킨터 import
from tkinter import *
from random import shuffle
import tkinter.font as tkFont
#from winsound import Beep
from time import sleep
# 프로그램 창 만들기
root = Tk()
root.title("자리 배치 프로그램")

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

root.geometry("{}x{}+0+0".format(monitor_width, monitor_height))

# 반 이름 리스트 선언(여자, 남자)
with open("mac_save\practice\list.txt", "r", encoding="UTF8") as file:
    contents = file.read()
l1 = contents.split(sep = '\n', maxsplit = 1)


list_w = l1[0].split(sep = ',') # 여자 리스트 ex)1. 김수인
list_m = l1[1].split(sep = ',') # 남자 리스트 ex)17. 강우현

# 전체 좌석수 지정 (6열 5행)
global row_range
row_range = range(0,5)
global column_range
column_range = range(0,6)

class RandomSeats:
    
    def __init__(self, list_w,list_m):

        # 남자 리스트, 여자 리스트 필수로 불러오기
        self.list_m = list_m
        self.list_w = list_w

        # text 하나하나 좌표마다 지정하기 위한 반복문
        for repeat_row in row_range:

            for repeat_col in column_range:
                globals()['text{},{}'.format(repeat_row, repeat_col)] = StringVar() # 전역변수 추가
        
        # 라벨 하나하나 지정
        for repeat_row in row_range:

            for repeat_col in column_range:
                globals()['lab{},{}'.format(repeat_row,repeat_col)] = \
                Label(root, textvariable= globals()['text{},{}'.format(repeat_row,repeat_col)],font = tkFont.Font(size = 10, weight = "bold"))\
                .grid(row = repeat_row, column = repeat_col, padx = int(monitor_width//24), pady = int(monitor_height//20) )


    def changeText(self):

        self.list_m = l1[1].split(sep = ',')
        self.list_w = l1[0].split(sep = ',')
        
        try:
            btn.place_forget()

            for repeat_row in row_range:
                for repeat_col in column_range:
                    globals()['text{},{}'.format(repeat_row, repeat_col)].set('')
            root.update()
        except:
            pass

        # 나머지 자리 추가
        leftover_seats(self.list_m, self.list_w)

        # 리스트 각각 섞기
        shuffle(self.list_m)
        shuffle(self.list_w)
        
        # 반복할 때 카운트 (man, woman)
        m = 0
        w = 0

        #왼쪽 좌석과 오른쪽 좌석 배치
        left = [0,2,4]
        right = [1,3,5]

        for count in [5,4,3,2,1]:

            time_counted = Label(root, text = count, font = tkFont.Font(size = 300, weight = "bold"))
            time_counted.place(relx= 0.5, rely=0.5, anchor = "center")
            root.update()
            sleep(1)
            time_counted.place_forget()
        
        # try구문을 이용하여 사람 수가 적어 indexing 오류가 발생해도 무시
        try:

            for repeat_row in row_range:

                for repeat_col in left:
                    globals()['text{},{}'.format(repeat_row, repeat_col)].set(self.list_w[w])
                    w += 1
                
        except:
            pass

        try:

            for repeat_row in row_range:

                for repeat_col in right:

                    globals()['text{},{}'.format(repeat_row, repeat_col)].set(self.list_m[m])
                    m += 1

        except:
            pass
        
        btn.place(relx = 0.5, rely = 0.85, anchor = 'center')
        btn.config(text = '다시뽑기')



def leftover_seats(l_1, l_2):
        # l_1을 기준으로 넘으면 l_2로 옮김
        shuffle(l_1)
        shuffle(l_2)
        while len(l_1) > 15:
            
            l_2.append(l_1[-1])
            del l_1[-1]
        while len(l_2) > 15:
            
            l_1.append(l_2[-1])
            del l_2[-1]



# 클래스 선언
haneul = RandomSeats(list_w,list_m)

# 이제 디자인 하자
copyright = Label(root, text = 'Made by 11기 김우진\nEdited by 12기 박준용', font = tkFont.Font(size = 16, weight = 'bold', slant = 'italic'))
copyright.place(relx = 1, rely = 1, anchor = "se")
# 뽑기 버튼
btn = Button(root, padx = 30, pady = 10, text = "랜덤뽑기", font = tkFont.Font(size = 40, weight = 'bold'), command = haneul.changeText)
btn.place(relx = 0.38, rely = 0.85)
root.mainloop()