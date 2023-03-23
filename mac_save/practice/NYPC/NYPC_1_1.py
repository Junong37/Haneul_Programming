def cross():
    for iii in range(n):
        for ii in range(n):
            for i in range(4):
                for j in range(m):
                    if i == 0: # up
                        if iii - (j+1) < 0:
                            continue
                        result_cross[iii * n + ii] += map_list[iii - (j+1)][ii]
                    elif i == 1: # left
                        if ii - (j+1) < 0:
                            continue
                        result_cross[iii * n + ii] += map_list[iii][ii - (j+1)]
                    elif i == 2: # down
                        if iii + (j+1) >= n:
                            continue
                        result_cross[iii * n + ii] += map_list[iii + (j+1)][ii]
                    else: # right
                        if ii + (j+1) >= n:
                            continue
                        result_cross[iii * n + ii] += map_list[iii][ii + (j+1)]
            result_cross[iii * n + ii] += map_list[iii][ii]

def x():
    for iii in range(n):
        for ii in range(n):
            for i in range(4):
                for j in range(m):
                    if i == 0: # 1
                        if iii - (j+1) < 0 or ii + (j+1) >= n:
                            continue
                        result_x[iii * n + ii] += map_list[iii - (j+1)][ii + (j+1)]
                    elif i == 1: # 2
                        if iii - (j+1) < 0 or ii - (j+1) < 0:
                            continue
                        result_x[iii * n + ii] += map_list[iii - (j+1)][ii - (j+1)]
                    elif i == 2: # 3
                        if iii + (j+1) >= n or ii - (j+1) < 0:
                            continue
                        result_x[iii * n + ii] += map_list[iii + (j+1)][ii - (j+1)]
                    else: # 4
                        if iii + (j+1) >= n or ii + (j+1) >= n:
                            continue
                        result_x[iii * n + ii] += map_list[iii + (j+1)][ii + (j+1)]
            result_x[iii * n + ii] += map_list[iii][ii]

n, m = map(int, input().split())

map_list = []
result_cross = [0 for i in range(n * n)]
result_x = [0 for i in range(n * n)]
for i in range(n):
    temp = list(map(int, input().split()))
    map_list.append(temp)

cross()
x()

final = max([max(result_cross), max(result_x)])
print(final)