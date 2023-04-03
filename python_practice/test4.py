a = int(input())

four = False
five = False

if a % 4 == 0:
    four = True
if a % 5 == 0:
    five = True

if four and five:
    print("{}은(는) 4의 배수이면서 5의 배수이다.".format(a))
elif four:
    print("{}는 4의 배수이다.".format(a))
elif five:
    print("{}는 5의 배수이다.".format(a))
else:
    print(four, five)
    print("{}는 4의 배수도 5의 배수도 아니다.".format(a))