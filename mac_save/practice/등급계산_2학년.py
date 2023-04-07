sub_list = ["국어", "수학", "영어", "선택A", "선택B"]
num = [5, 5, 4, 5, 5]
score = []
result = 0

for i in sub_list:
    print(i, end="")
    score.append(int(input(": ").format(i)))

for i in range(len(sub_list)):
    result += (score[i] * num[i])

result /= sum(num)

print("{:.3}".format(result))