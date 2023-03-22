import random

print("랜덤 MBTI 뽑기")

fir = ["I", "E"]
sec = ["S", "N"]
thir = ["T", 'F']
fou = ["P", "J"]

random.shuffle(fir)
random.shuffle(sec)
random.shuffle(thir)
random.shuffle(fou)

print(fir[0] + sec[0] + thir[0] + fou[0])