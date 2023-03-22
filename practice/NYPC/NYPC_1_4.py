def findNearNum(exList, values):
    answer = [0 for _ in range(2)] # answer 리스트 0으로 초기화

    minValue = min(exList, key=lambda x:abs(x-values))
    minIndex = exList.index(minValue)
    answer[0] = minIndex
    answer[1] = minValue
    
    return answer
# [출처] [Python] - 정수 리스트 중 주어진 정수, 실수값과 가장 가까운 정수 찾기(근사값 찾기)|작성자 주현
# https://blog.naver.com/zzang9ha/222010163074

n = int(input())
type = [0 for i in range(n)]
name = [0 for i in range(n)]
s = [0 for i in range(n)]
result = []
result_parts = []
parts_dict = {"Body": [],
"Handle": [],
"Wheel": [],
"Engine": [],
"Booster": []}

for i in range(n):
    type[i], name[i], s[i] = input().split()
    parts_dict[type[i]].append([name[i], s[i]])

synergy = int(input())
syn_list = [[0, 0, 0] for i in range(synergy)]

for i in range(synergy):
    syn_list[i][0], syn_list[i][1], syn_list[i][2] = input().split()
    syn_list[i][2] = int(syn_list[i][2])

result = [0 for i in range(2 ** (len(parts_dict["Handle"]) + len(parts_dict["Body"]) + len(parts_dict["Wheel"]) + len(parts_dict["Engine"]) + len(parts_dict["Booster"]) - 5))]
result_parts = [0 for i in range(2 ** (len(parts_dict["Handle"]) + len(parts_dict["Body"]) + len(parts_dict["Wheel"]) + len(parts_dict["Engine"]) + len(parts_dict["Booster"]) - 5))]
iiiii = 0
for i in range(len(parts_dict["Body"])):
    for j in range(len(parts_dict["Handle"])):
        for k in range(len(parts_dict["Wheel"])):
            for l in range(len(parts_dict["Engine"])):
                for m in range(len(parts_dict["Booster"])):
                    iii = 0
                    for n in range(synergy):
                        for o in parts_dict:
                            for p in range(len(parts_dict[o])):
                                if syn_list[n][0] in parts_dict[o][p][0]:
                                    for q in parts_dict:
                                        for r in range(len(parts_dict[q])):
                                            if syn_list[n][1] in parts_dict[q][r][0]:
                                                iii += syn_list[n][2]
                    result[iiiii] = int(parts_dict["Body"][i][1]) + int(parts_dict["Handle"][j][1]) + int(parts_dict["Wheel"][k][1]) + int(parts_dict["Engine"][l][1]) + int(parts_dict["Booster"][m][1]) + iii
                    result_parts[iiiii] = [parts_dict["Body"][i][0], parts_dict["Handle"][j][0], parts_dict["Wheel"][k][0], parts_dict["Engine"][l][0], parts_dict["Booster"][m][0]]
                    iiiii += 1
ss = int(input())
final = findNearNum(result, ss)
real_final = result_parts[final[0]]
print(result)
print(final)
print(result_parts)
for i in real_final:
    print(i)