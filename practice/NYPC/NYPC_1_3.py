# 달팽이
import sys
import math
from collections import deque

t = int(sys.stdin.readline())
result = []
map_list = deque()

for i in range(t):
    n, a, b = map(int, sys.stdin.readline().split())

    map_list = [0] * n
    
    for j in range(n):
        map_list[j] = [0] * n
    num = 0
    
    for j in range(n * 2 - 1):
        try:
            if j % 4 == 0: # right
                for k in range(math.floor(n - j / 2)):
                    if map_list[j // 4][k + (j // 4)] == 0:
                        num += 1
                        map_list[j // 4][k + (j // 4)] = num
            elif j % 4 == 1: # down
                for k in range(math.floor(n - j / 2)):
                    if map_list[k + 1 + (j // 4)][-(j // 4 + 1)] == 0:
                        num += 1
                        map_list[k + 1 + (j // 4)][-(j // 4 + 1)] = num
            elif j % 4 == 2: # left
                for k in range(math.floor(n - j / 2)):
                    if map_list[-(j // 4 + 1)][-k -1 - (j // 4 + 1)] == 0:
                        num += 1
                        map_list[-(j // 4 + 1)][-k -1 - (j // 4 + 1)] = num
            else: # up
                for k in range(math.floor(n - j / 2)):
                    if map_list[-(j // 4 + 2 + k)][j // 4] == 0:
                        num += 1
                        map_list[-(j // 4 + 2 + k)][j // 4] = num
        except:
            pass
        #print(map_list)
    for ii in range(len(map_list)):
        try:
            temp = map_list[ii].index(a)
        except:
            pass
        else:
            a_x = ii
            a_y = temp
        
        try:
            temp = map_list[ii].index(b)
        except:
            pass
        else:
            b_x = ii
            b_y = temp

    row = abs(a_x - b_x)
    col = abs(a_y - b_y)

    if row == col:
        print("YES")
    else:
        print("NO")