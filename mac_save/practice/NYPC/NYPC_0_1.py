def check():
    for i in range(n):
        # 로그 기록 유무 확인
        try:
            log_dict[i+1][0] = log_dict[i+1][0]
        except:
            continue
        
        # 로그 1개 오류
        try:
            log_dict[i+1][1] = log_dict[i+1][1]
        except:
            print("NO")
            return 0

        # 로그 홀수 오류
        if len(log_dict[i+1]) % 2 == 1:
            print("NO")
            return 0

        # 로그 오류
        for j in range(len(log_dict[i+1])):
            if j % 2 == 0:
                if log_dict[i+1][j][1] != 0:
                    print("NO")
                    return 0
                elif log_dict[i+1][j+1][0] - log_dict[i+1][j][0] < 60:
                    print("NO")
                    return 0
            else:
                if log_dict[i+1][j][1] != 1:
                    print("NO")
                    return 0
                try:
                    if log_dict[i+1][j][0] - log_dict[i+1][j+1][0] == 0:
                        print("NO")
                        return 0
                except:
                    pass

    print("YES")


n, m = map(int, input().split())
log_dict = {}

for i in range(n):
    log_dict[i + 1] = []

for i in range(m):
    temp = list(map(int, input().split()))
    log_dict[temp[1]].append([temp[0], temp[2]])
#print(log_dict)

check()