sub_list = ["한국사", "일본어/중국어", "사회", "과학", "한문", "국어", "영어", "수학"]
num = [3, 4, 3, 2, 2, 3, 3, 3]
score = []
result = 0

for i in sub_list:
    print(i, end="")
    score.append(int(input(": ").format(i)))

for i in range(len(sub_list)):
    result += (score[i] * num[i])

result /= sum(num)

print("{:.3}".format(result))