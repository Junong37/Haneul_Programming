from jajucha.planning import BasePlanning
from jajucha.graphics import Graphics
from jajucha.control import mtx
import cv2
import numpy as np
import time




class Planning(BasePlanning):
    def __init__(self, graphics):
        super().__init__(graphics)
        # --------------------------- #
        self.vars.redCnt = 0  # 변수 설정
        self.vars.greenCnt = 0  # 변수 설정
        self.vars.stop = True
        self.vars.steer = 0
        self.vars.velocity = 0
        

    def process(self, t, frontImage, rearImage, frontLidar, rearLidar):
        
        
        # 자주차의 센서 정보를 바탕으로 조향과 속도를 결정하는 함수
        # t: 주행 시점으로부터의 시간 (초)
		# frontImage: 전면 카메라 이미지
		# rearImage: 후면 카메라 이미지
		# frontLidar: 전면 거리 센서 (mm), 0은 오류를 의미함
		# rearLidar: 후면 거리 센서 (mm), 0은 오류를 의미함
        

        # [1] 라이다 처리

        # canny 이미지 보기
        canny = self.canny(frontImage)
        self.imshow('canny', canny)

        # lines, (reds, greens) = self.processFront(frontImage)
        # 차선 정보 파악
        V, L, R = self.gridFront(frontImage, cols=41, rows=21)
        # V, L, R = self.gridFront(frontImage, cols=7, rows=3) : 전방 이미지 행선, 열선 그리기
        # rearV, rearL, rearR = self.gridRear(rearImage, cols=4, rows=6) : 후방 이미지도 가능
        # rows : 행선값  cols : 열선값 (row, column) ex) rows=3 : 행선이 3개이고, 총 4개의 행 칸이 생성
        # L[0], L[1], L[2], R[0], R[1], R[2], V[0]~v[6]

        # 각 변수의 최댓값
        if V[3] == 255:  # V[i]가 잡히지 않은 경우
            ...
        if L[2] == 320:  # L[i]가 잡히지 않은 경우  (중앙 픽셀이 324라서 왼쪽으로 최대 324)
            ...
        if R[2] == 320:  # R[i]가 잡히지 않은 경우  (중앙 픽셀이 324라서 오른쪽으로 최대 315)
            ...

        # [2] 주행 처리

        standard_steer = 11
        steer = standard_steer  #기본 조향       
        velocity = 50
        # fortest = R
        # 1. 필요없는 점 무시하기 코드
        for i_1 in range (0,21) :
            if R[i_1]==316: R[i_1] = "없음"
            if L[i_1] ==325: L[i_1] = "없음"

        # 3. 중앙보정 0~20 까지의 값을 평균내어 직선보정을 하는 방식, 정확성을 높일 수 있음
        total_1 = 0
        ignore = 0
        
        for i_6 in range (20+1):

            # if R[i_6] == "무시" or L[i_6] == "무시" :
            #     ignore += 1
            if R[i_6] == "없음" or L[i_6] == "없음" :
                ignore += 1
            else:
                center = L[i_6] - R[i_6]
                if center == 0:
                    total_1 +=0 #standard_steer   #Keep going
                
                elif center < 0:
                    total_1 += -center #+standard_steer
                
                elif center > 0:
                    total_1 += -center #+standard_steer
        
        if ignore == 21: 
            steer = standard_steer
        
        else: 
            average = total_1 // (21-ignore)
            steer = average // 5 +standard_steer
        

        # 4. 커브 코드
        
        #(1) 리스트 나누기 (왼쪽, 오른쪽)
        list_left = V[0:19]
        list_right= V[40:21:-1]

        #(2) 기준점 정하기
        minLeft = min(list_left)
        minRight = min(list_right)
        Idx_L = list_left.index(minLeft)
        Idx_R = list_right.index(minRight)
        Idx_shift_L =  Idx_L
        Idx_shift_R = Idx_R
        angle_L = "미감지"
        angle_R = "미감지"
        slope_L = "미감지"
        slope_R = "미감지"

        #(3) 변화하는 곳 찾아서 돌기
        if V[20] < 200: 
        #우회전
            velocity = 40
            while  V[Idx_shift_L] > V[Idx_L] + 11 * (Idx_shift_L - Idx_L) -30 and Idx_shift_L < 19:
                Idx_shift_L += 1
            if L.count("없음") < R.count("없음") and V[Idx_shift_L] > V[Idx_L]:
                slope_L = (V[Idx_shift_L + 3] -V[Idx_shift_L]) / 3
                angle_L= np.arctan(slope_L/6)*180//3.14
                steer = int (90-angle_L) +standard_steer + 10 
                if V[10] < 70: steer = 100 +standard_steer

        #좌회전
            while  V[40-Idx_shift_R] > V[40-Idx_R] + 11 * (Idx_shift_R - Idx_R) -30 and Idx_shift_R < 19:
                Idx_shift_R += 1
            if L.count("없음") > R.count("없음") and V[40-Idx_shift_R] > V[40-Idx_R]:
                slope_R = (V[37-Idx_shift_R] - V[40-Idx_shift_R]) / 3
                angle_R = np.arctan(slope_R/6)*180//3.14
                steer =  int (angle_R - 90) +standard_steer
                if V[30] < 70 : steer = -100 +standard_steer

       # 5. 삼거리 회전
        think = 0
        think_t = 0
       # (1) 1번 삼거리 
        if frontLidar <= 3000:
            steer = -60 + standard_steer
        if L.count("없음") >= 10 :
            velocity = 60
            bunmo= V[20] // 10
            if 240 <=V[20] <= 255 and L.count("없음") <= 16: steer = -40 - 600 // bunmo + standard_steer
            elif (Idx_R >= 5 and  V[20] > 200): steer = -40 - 600 // bunmo +standard_steer
            elif Idx_R >= 15: steer = -40 - 600 //bunmo + standard_steer      #elif 구문 2개 없어도 되지 않을까?
            think = steer

       # 6. 속도 조정 코드
        if -20 + standard_steer < steer < 20 + standard_steer :
            velocity = 70

        # 7. 방향타 고장 방지
        if steer > 100 + standard_steer :
            steer = 100 + standard_steer
        if steer < -100 + standard_steer :
            steer = -100 + standard_steer

        # 8. 보행자 인식 후 멈춤
        if 0< frontLidar < 100 :
            velocity = 0



        # print ('L[20]=', L[20], 'L[19]=', L[19], 'L[18]=', L[18], end="  //  ")
        # print ('R[20]=', R[20], 'R[19]=', R[19], 'R[18]=', R[18],)
        # print ("slope_L=", slope_L, "slope_R=", slope_R, "angle_L=", angle_L, "angle_R=", angle_R)

        # print ("없음인 L 갯수", L.count("없음") , "없음인 R 갯수", R.count("없음"))
        #print ('total_1=', total_1, 'average=', average, 'ignore=', ignore)
        # print (repeat, countfortest)
        # print (countfortest)
        # print (empty)
        print (R)
        print (think, think_t)
        # print (total_2)       #점선 테스트용
        # print (21-t, "보다 작으면 무시")
        # print('벽과의 거리',V[20])
        # print(V[20], V[25], V[30], V[35])
        # print ('R의 최댓값',R[20],'L의 최댓값', L[20], 'V의 최댓값', V[20])  #측정용
        # print ('Idx_L=',Idx_L, 'Idx_R=', Idx_R)
        # print ('비어있는 칸', R_empty)
        # print ('점선의 표준편차', R_std)
        # print ('Idx_shift_L=',Idx_shift_L , 'Idx_shift_R=', Idx_shift_R )
        # print('frontLidar=', frontLidar, end="..//..")
        # print('rearLidar=', rearLidar, end="       => => =>    ")
        print('[steer=', steer, end="]  ")
        print('[velocity=', velocity, "]")
        print()

        self.vars.steer = steer
        self.vars.velocity = velocity

        # self.vars.redCnt = redCnt  # 변수 설정
        # self.vars.greenCnt = greenCnt  # 변수 설정
        # self.vars.stop = stop
        return self.vars.steer, self.vars.velocity #self.vars.redCnt, self.vars.greenCnt, self.vars.stop



if __name__ == "__main__":
    g = Graphics(Planning)  # 자주차 컨트롤러 실행
    g.root.mainloop()  # 클릭 이벤트 처리
    g.exit()  # 자주차 컨트롤러 종료