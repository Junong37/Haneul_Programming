from jajucha.planning import BasePlanning
from jajucha.graphics import Graphics
from jajucha.control import mtx
import cv2
import numpy as np
import math
from cnn import model, util
import torch
import torchvision.transforms as transforms

#_______허프변환 후 각 직선의 정보 파악(직선의 길이, 직선이 이루는 각도, 직선의 중심점)_________#
class lane:             
    def __init__(self, pt1, pt2):
        self.pt1 = pt1
        self.pt2 = pt2
        self.length = math.sqrt(
            (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)//1
        self.angle = 180 - abs(math.atan2(pt1[1] - pt2[1], pt1[0] - pt2[0])*180//np.pi)
        self.center = ((pt1[0] + pt2[0]) / 2, (pt1[1] + pt2[1]) / 2)

class Planning(BasePlanning):
    def __init__(self, graphics):
        super().__init__(graphics)
        # _________________________________________________설정_________________________________________________#
        
        # --------------초기 변수 설정------------- #
        self.vars.redCnt = 0  
        self.vars.greenCnt = 0
        self.vars.stop = True
        self.vars.steer = 0
        self.vars.velocity = 0
        self.model = model.CNN(util.default_perspective).to("cpu")
        self.model.load_state_dict(torch.load("./cnn/model", map_location="cpu"))
        self.model.eval()
        self.intro = False
        self.dotted = False
        self.right_angle = False
        self.obstacle = False
        self.delay = 0
        self.delay_1 = 0
        self.count = False
        self.count_1 = False
        self.step = 0
        self.stride = -10000
        self.start_time_1 = -10000
        self.start_time_2 = -10000
        self.start_time_3 = -10000
        self.start_time_4 = -10000


        # ---------------------------------------- #
    def process(self, t, frontImage, rearImage, frontLidar, rearLidar):
        """
        자주차의 센서 정보를 바탕으로 조향과 속도를 결정하는 함수
        t: 주행 시점으로부터의 시간 (초)
                frontImage: 전면 카메라 이미지
                rearImage: 후면 카메라 이미지
                frontLidar: 전면 거리 센서 (mm), 0은 오류를 의미함
                rearLidar: 후면 거리 센서 (mm), 0은 오류를 의미함
                """
        if t == 0.00:
            self.intro = False
            self.dotted = False
            self.right_angle = False
            self.obstacle = False
            self.delay = 0
            self.delay_1 = 0
            self.count = False
            self.count_1 = False
            self.step = 0
            self.stride = -10000
            self.start_time_1 = -10000
            self.start_time_2 = -10000
            self.start_time_3 = -10000
            self.start_time_4 = -10000
            print('reset')
        #----------------격자점 나타내기------------------#
        V, L, R = self.gridFront(frontImage, cols=7, rows=3)

        # 각 변수의 최댓값
        if V[3] == 255:  # V[i]가 잡히지 않은 경우
            ...
        if L[2] == 320:  # L[i]가 잡히지 않은 경우  (중앙 픽셀이 324라서 왼쪽으로 최대 324)
            ...
        if R[2] == 321:  # R[i]가 잡히지 않은 경우  (중앙 픽셀이 324라서 오른쪽으로 최대 315)
            ...
        # ----------------시점 변환--------------------- #

        perspective = util.JajuchaCV.cv_perspective_area(frontImage, util.default_perspective)

        for val in (util.default_perspective.left_bottom, util.default_perspective.left_top, util.default_perspective.right_bottom, util.default_perspective.right_top):
            cv2.circle(frontImage, (int(val[0]), int(
                val[1])), 5, (0, 0, 255), -1)
        cv2.imshow("front", frontImage)
        
        # ----------------canny 엣지--------------------- #
        canny = util.JajuchaCV.cv_canny(perspective)
        cv2.imshow("canny", canny)

        # ----------------확률적 허프변환--------------------- #
        lines = cv2.HoughLinesP(canny, 1, np.pi / 180,
                                30, minLineLength=30, maxLineGap=20)
        lanes = []
        if lines is not None:
            for i in range(lines.shape[0]):
                pt1 = (lines[i][0][0], lines[i][0][1])
                pt2 = (lines[i][0][2], lines[i][0][3])
                lanes.append(lane(pt1, pt2))
                cv2.line(perspective, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

        # 선분 중앙점을 통한 좌우 나누기
        #   | 
        # L | R
        #   | 
        q_L =[]
        q_R =[]
        for l in lanes:     #l은 매개변수, lanes는 [묶음1, 묶음2,....]와 같이 각각의 클래스를 저장한 리스트이므로 l에 묶음이 번갈아 대입된다.
            if l.center[0] < (224/2):
                q_L.append(l)
            elif l.center[0] > (224/2):       #모든 점은 튜플의 좌표로 저장이 되므로 ~[0]는 x좌표를 ~[1]은 y좌표를 
                q_R.append(l)

        length_R =[]
        length_R_step =[]
        angle_R = []            
        length_L =[]
        length_L_step =[]
        angle_L = []
        count_L = 0
        count_R = 0

    
        if q_R is not None:
            for i in q_R:
                angle_R.append(i.angle)
                if i.angle <= 70:
                    length_R_step.append(i.length)
                if 80 <= i.angle:
                    length_R.append(i.length)
                    if i.length < 50:
                        count_R +=1
                    
    
        if q_L is not None:
            for i in q_L:
                angle_L.append(i.angle)
                if i.angle <= 60:
                    length_L_step.append(i.length)
                if 80 <= i.angle:
                    length_L.append(i.length)
                    if i.length < 50:
                        count_L +=1

        # ----------------딥러닝 상황판단--------------------- #
        tinput = transforms.ToTensor()(canny)
        tinput = tinput.unsqueeze_(0)
        tinput = tinput.to("cpu")
        out = torch.exp(self.model(tinput))
        _, outidx = out.max(dim=1)

        classes = ['T', 'other', 'perpendicular', 'three_left']
        situation_idx = outidx.item()
        cv2.putText(perspective, "{0} {1:0.2f}%".format(
            classes[situation_idx], out[0][outidx].item()*100), (10, 170), cv2.FONT_ITALIC, 0.6, (255, 255, 0), 2)
        
        # --------------- 딥러닝 판정 보완 ------------------- #
        situation = ''
        percent = out[0][outidx].item()*100
        if classes[situation_idx] == 'other':   situation='other'

        #삼거리
        if len(angle_R) > 0:
            if classes[situation_idx] == 'three_left' and percent>=90 and min(angle_R)>=85: #오른쪽 직선 잡힘 + 각이 80도 이상일 때
                situation = 'three_left'
        #점선
        if len(length_L) > 0 and len(length_R) > 0:
            if count_L >= 1 and max(length_R)>100:
                situation = 'dotted line'
                
            elif count_R >= 1 and max(length_L)>100:
                situation = 'dotted line'

        #직각
        if classes[situation_idx] == 'perpendicular' and percent>=90 and V[0]>=V[1]>=V[2]:
            situation = 'perpendicular'        

        #T자
        if classes[situation_idx] == 'T' and percent>=80 and min(V) >=200 :  situation = 'T'

        if situation == '' :   situation='other'        

        cv2.putText(perspective, "result = {0}".format(situation), (10, 210), cv2.FONT_ITALIC, 0.8, (255, 0, 0), 2)
        cv2.imshow("perspective", perspective)
        # ___________________________________________________________주행_________________________________________________________#

        standard_steer = 2
        standard_time = 4  #코너 하나를 돌기 위한 기준시 / 측정값
        steer = standard_steer  #기본 조향      
        velocity = 80
        state = ''
        #--------------------------빈칸인식---------------------------#
        for i in range (0,2+1) :
            if R[i]==321: R[i] = "없음"
            if L[i] ==320: L[i] = "없음"

        #------------------------중앙 보정----------------------------#
        if L[1] != '없음' and R[1] != '없음' :
            state = '중앙보정'
            if R[1]-L[1] < -20 :
                steer = (R[1] - L[1]) // 6 + standard_steer
        
            if R[1]-L[1] > 20 :
                steer = (R[1] - L[1]) // 6 + standard_steer #나누기 6은 민감도
        
        #----------------------삼거리-----------------------------#
        # 몇퍼센트로 감지 됐는지 측정 후 넣기
        # 다른 방법으로는 라이더 센서 측정값 이용하기
        # count - n번째 코너
        # intro - 첫번째 삼거리가 감지되었을 시 True, 종료될 때 False
        # start_time - 처음 감지되었을 시 시간, 7초 뒤에 종료됨.
        #if s_name in ['three_left'] and percentage >= 5:
        if situation =='three_left' and 400<frontLidar<1000: #450은 측정값
            if self.intro == False:
                self.start_time_2 = t
                self.intro = True

        if self.start_time_2 + standard_time + self.delay_1 >= t:
            steer = -70 +standard_steer
            state = '삼거리'
        else:
            self.count_1 = False
            self.delay_1 = 0
            self.intro = False

        if self.intro == True and self.count_1 == False and frontLidar>=350:
            steer = standard_steer
            self.delay_1 = t - self.start_time_2
            state = "delaying...2"
        elif self.intro == True and frontLidar<350:
            self.count_1 = True



        # if self.start_time_2 + 10000 >= t:
        #         if len(angle_R)>0:
        #             if min(angle_R) >=85:
        #                 self.start_time_2 = -10000
        #         steer = -70 +standard_steer
        #         state = '삼거리'
        
        # else:
        #     self.intro = False
        #----------------------커브 코너--------------------------# 
        # V값을 없애도 되지 않을까?
        # if V[4] < 55:
        #     steer = - (100 - V[4]) +standard_steer
        #     state = '좌회전'

        # elif V[5] < 35:
        #     steer = - (120 - V[5]) +standard_steer
        #     state = '좌회전'

        # if V[2] < 55:
        #     steer = 100 - V[2] +standard_steer
        #     state = '우회전'

        # elif V[1] < 35:
        #     steer = 120 - V[1] +standard_steer
        #     state = '우회전'

        if V[4] < 55:
            steer = - 100 +standard_steer
            state = '좌회전'

        elif V[5] < 35:
            steer = - 100 +standard_steer
            state = '좌회전'

        if V[2] < 55:
            steer = 100 +standard_steer
            state = '우회전'

        elif V[1] < 35:
            steer = 100 +standard_steer
            state = '우회전'

        #----------------------직각 코너--------------------------#
        if situation == 'perpendicular' and self.right_angle == False:
            self.right_angle =True
            self.start_time_3 = t

        elif situation == 'T' and self.right_angle == False:
            self.right_angle =True
            self.start_time_3 = t
        
        
        if self.start_time_3 + standard_time + self.delay >= t:
            steer = -70 + standard_steer
            state = "직각/T자"
        else:
            self.right_angle = False
            self.count = False
            self.delay = 0
        
        if self.right_angle == True and V[3] >= 190 and self.count == False:
            steer = standard_steer
            self.delay = t - self.start_time_3
            state = "delaying..."
        elif self.right_angle == True and V[3] < 190:
            self.count = True
        
        #----------------------장애물 피하기-----------------------#
        total_length_step = length_L_step + length_R_step
        if frontLidar <200:
            if self.obstacle == False:
                self.start_time_4 = t
                self.obstacle = True
        if self.start_time_4 + 3 >= t and len(length_R) > 0:
            # steer = (87-min(angle_R))     #딱 직진하고 있을때 기울기가 86임
            # print("후진각도=", steer)
            state = "후진중... 빵빵"
            velocity = -50
        # elif self.start_time_4 + 4 >= t:
        #     steer = standard_steer      # 만약 후진하면서 좌측이동이 너무 심하다면 후진각도를 리스트에 저장하고 평균내서 1초 우회전-> 1초 좌회전 방법으로 위치 재정비하는것으로 바꿈
        #     velocity = 50
        #     state = "다시 직진"
        elif self.obstacle == True and self.step == 0:
            steer = -60 +standard_steer
            state = "step = 0"
            if len(total_length_step)>0:
                print(sum(total_length_step))
                if sum(total_length_step)>=800:
                    self.step = 5
        elif self.step == 5:
            steer = standard_steer
            if V[2] <= 70 :
                self.step = 1
        elif self.step == 1:
            state = "step = 1"
            velocity = 30
            if len(angle_L)>0:
                steer = (87-min(angle_L))*5
                if 86 <= min(angle_L) <=88:
                    self.step = 2
        elif self.step == 2:
            steer = 0 +standard_steer
            state = "step = 2"
            if V[3]<=200:
                self.step = 3
                self.stride = t
                
        elif self.step == 3 and self.stride + 3 >= t:
            steer = 30 +standard_steer
            state = "step = 3"
            self.obstacle = False
        
        # if self.obstacle == True:
        #     state = '장애물 피하기'
            
        #---------------------------------------------#
        # 삼거리, 장애물 중 아무조건에도 들어가지 않고 라이더를 만났을 때, 대책이 없다는 것을 발견함
        # 물론 트랙구성이나 상황을 고려해보았을때 그러기는 정말 쉽지 않으나 그냥 고려해볼한 해서 기록함
        # 모든 특이점 구간에서 도입부분 기울기를 고려해봐야 할듯
        # 또한 속도가 점점 느려져 대응책도 마련해봐야 할듯

        print(state)
        cv2.waitKey(1)      #필수!
        self.vars.steer = steer
        self.vars.velocity = velocity
        return self.vars.steer, self.vars.velocity
    
    

if __name__ == "__main__":
    g = Graphics(Planning)  # 자주차 컨트롤러 실행
    g.root.mainloop()  # 클릭 이벤트 처리
    g.exit()  # 자주차 컨트롤러 종료