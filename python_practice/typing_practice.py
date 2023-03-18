import time
import random

word_list = ["hello world", "hi world", "This is the test sentence"]
random.shuffle(word_list)

difficulty = int(input("Set difficulty (1 ~ 10): "))
time_per_letter = 1 / difficulty
print("time per letter: {}".format(time_per_letter))

for i in word_list:
    print(i)
    current_time = time.time()
    val = input()

    if val == i and time.time() - current_time < len(i) * time_per_letter:
        print("성공")
        continue
    else:
        print("실패")
        break