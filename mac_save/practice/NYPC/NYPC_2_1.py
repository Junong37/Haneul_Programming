n = int(input())
col_list = list(map(int, input().split()))
result = []

for i in range(n):
    temp = []

    for j in range(n):
        try:
            if col_list[j+i] in temp:
                break
            temp.append(col_list[j+i])
        except:
            pass

    result.append(len(temp))
    if len(temp) >= n - i:
        break
print(max(result))