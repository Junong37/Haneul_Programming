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

        # 직진 주행
        cutline = 230
        # canny 이미지 보기
        canny = self.canny(frontImage)
        pre_canny = canny[cutline:480,:].copy()
        pre_image = frontImage[cutline:480,:,:].copy()
        topLeft = (254, 230 - 230)
        bottomRight = (640, 390 - 230)
        topRight = (376,230-230)
        bottomLeft = (0, 390 - 230)

        pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])
        w1 = abs(bottomRight[0] - bottomLeft[0])
        w2 = abs(topRight[0] - topLeft[0])
        h1 = abs(topRight[1] - bottomRight[1])
        h2 = abs(topLeft[1] - bottomLeft[1])
        width = max([w1, w2])
        height = max([h1, h2])

        pts2 = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])
        mtrx = cv2.getPerspectiveTransform(pts1, pts2)
        result_canny = cv2.warpPerspective(pre_canny, mtrx, (width, height))
        result_image = cv2.warpPerspective(pre_image, mtrx, (width, height))

        resized_canny = cv2.resize(result_canny,dsize=(640,480), interpolation=cv2.INTER_LINEAR)
        resized_canny = cv2.cvtColor(resized_canny, cv2.COLOR_GRAY2RGB)
        cv2.imshow('r',resized_canny)

        # 차선 정보 파악
        V, L, R = self.gridFront(resized_canny, cols=7, rows=30)
        # V, L, R = self.gridFront(frontImage, cols=7, rows=3) : 전방 이미지 행선, 열선 그리기
        # rearV, rearL, rearR = self.gridRear(rearImage, cols=4, rows=6) : 후방 이미지도 가능
        # rows : 행선값  cols : 열선값 (row, column) ex) rows=3 : 행선이 3개이고, 총 4개의 행 칸이 생성
        # L[0], L[1], L[2], R[0], R[1], R[2], V[0]~v[6]

        # 각 변수의 최댓값
        if V[3] == 255:  # V[i]가 잡히지 않은 경우
            ...
        if L[2] == 325:  # L[i]가 잡히지 않은 경우  (중앙 픽셀이 324라서 왼쪽으로 최대 324)
            ...
        if R[2] == 316:  # R[i]가 잡히지 않은 경우  (중앙 픽셀이 324라서 오른쪽으로 최대 315)
            ...
        e = 0
        steer = 0
        velocity =10



        # print ('L[0]=', L[0], 'L[1]=', L[1], 'L[2]=', L[2], end="  //  ")
        # print ('R[0]=', R[0], 'R[1]=', R[1], 'R[2]=', R[2])
        # print ('V[0]=', V[0], 'V[1]=', V[1], 'V[2]=', V[2], 'V[3]=', V[3], 'V[4]=', V[4], 'V[5]=', V[5], 'V[6]=', V[6])
        # print('frontLidar=', frontLidar, end="..//..")
        # print('rearLidar=', rearLidar, end="       => => =>    ")
        # print('[e=', e, end="]  ")
        # print('[steer=', steer, end="]  ")
        # print('[velocity=', velocity, "]")
        # print()

        self.vars.steer = steer
        self.vars.velocity = velocity
        return self.vars.steer, self.vars.velocity


if __name__ == "__main__":
    g = Graphics(Planning)  # 자주차 컨트롤러 실행
    g.root.mainloop()  # 클릭 이벤트 처리
    g.exit()  # 자주차 컨트롤러 종료
