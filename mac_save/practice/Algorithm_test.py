# 선택 정렬 알고리즘
import time
import random

a = time.time()
list_a = [i for i in range(10000)]
random.shuffle(list_a)

for i in range(len(list_a)):
    min = 9999
    for j in range(i, len(list_a)):
        if list_a[j] < min:
            min = list_a[j]
            index = j
        
    temp = list_a[i]
    list_a[i] = min
    list_a[index] = temp
    
print(list_a)
#print(time.time())
print(time.time() - a)