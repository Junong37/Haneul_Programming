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
        """
        자주차의 센서 정보를 바탕으로 조향과 속도를 결정하는 함수
        t: 주행 시점으로부터의 시간 (초)
		frontImage: 전면 카메라 이미지
		rearImage: 후면 카메라 이미지
		frontLidar: 전면 거리 센서 (mm), 0은 오류를 의미함
		rearLidar: 후면 거리 센서 (mm), 0은 오류를 의미함
        """

        # [1] 라이다 처리

        # canny 이미지 보기
        canny = self.canny(frontImage)
        # self.imshow('canny', canny)

        # 차선 정보 파악
        V, L, R = self.gridFront(frontImage, cols=7, rows=3)
        # V, L, R = self.gridFront(frontImage, cols=7, rows=3) : 전방 이미지 행선, 열선 그리기
        # rearV, rearL, rearR = self.gridRear(rearImage, cols=4, rows=6) : 후방 이미지도 가능
        # rows : 행선값  cols : 열선값 (row, column) ex) rows=3 : 행선이 3개이고, 총 4개의 행 칸이 생성
        # L[0], L[1], L[2], R[0], R[1], R[2], V[0]~v[6]

        e = 0

        # 각 변수의 최댓값
        #if V[3] == 255:  # V[i]가 잡히지 않은 경우
        #    pass
        #if L[2] == 325:  # L[i]가 잡히지 않은 경우  (중앙 픽셀이 324라서 왼쪽으로 최대 324)
        #    pass
        #if R[2] == 316:  # R[i]가 잡히지 않은 경우  (중앙 픽셀이 324라서 오른쪽으로 최대 315)
        #    pass

        # [2] 주행 처리

        # 정지
        if frontLidar <= 200:
            velocity = 0
            print("stop")

        # 직진
        if -30 <= R[0] - L[0] <= 30 and -30 <= R[1] - L[1] <= 30 and -30 <= R[2] - L[2] <= 30:
            e = 0
            print("straight")
        elif R[0] - L[0] > 30 or R[1] - L[1] > 30 or R[2] - L[2] > 30:
            e = (R[1] - L[1]) * 0.3
            print("right")
        elif R[0] - L[0] < -30 or R[1] - L[1] < -30 or R[2] - L[2] < -30:
            print("left")
            e = (R[1] - L[1]) * 0.3

        # 회전
        if 0:
            print("left turn")
        elif R[0] == 316 and R[1] == 316:
            print("right turn")
            e = 50 + V[0] * 0.3 # 수치 설정
            if V[0] != 255 and V[1] != 255:
                pass

        # 둘 다 잡히지 않은 경우
        #else:
        #    e = 0
        #else:
        #    return self.vars.steer, self.vars.velocity  # 이전 명령

        #cv2.imshow('Front Grid Image', frontImage)

        steer = int(e / 3) - 20  # 계수 1/3, 조정 -20
        if steer > 100:
            steer = 50
        elif steer < -100:
            steer = -50
        velocity = 90
        

        print ('L[0]=', L[0], 'L[1]=', L[1], 'L[2]=', L[2], end="  //  ")
        print ('R[0]=', R[0], 'R[1]=', R[1], 'R[2]=', R[2])
        print ('V[0]=', V[0], 'V[1]=', V[1], 'V[2]=', V[2], 'V[3]=', V[3], 'V[4]=', V[4], 'V[5]=', V[5], 'V[6]=', V[6])
        print('frontLidar=', frontLidar, end="..//..")
        print('rearLidar=', rearLidar, end="       => => =>    ")
        print('[e=', e, end="]  ")
        print('[steer=', steer, end="]  ")
        print('[velocity=', velocity, "]")
        print()

        self.vars.steer = steer
        self.vars.velocity = velocity
        return self.vars.steer, self.vars.velocity  #값을 차에 보내주는 과정


if __name__ == "__main__":
    g = Graphics(Planning)  # 자주차 컨트롤러 실행
    g.root.mainloop()  # 클릭 이벤트 처리
    g.exit()  # 자주차 컨트롤러 종료