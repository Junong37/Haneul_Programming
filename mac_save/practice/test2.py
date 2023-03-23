# 2~7 8~19 20~37
# 6 12 18

num = int(input())
div_num = (6 * ((num - 1) // 6 + 1))

if num == 1:
    result = 1
else:
    result = (num - 1) // div_num + 1 

print(div_num)
print(result)