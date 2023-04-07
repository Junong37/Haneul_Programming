buy = int(input("입력: "))

if 10000 <= buy < 50000:
    rate = 5
elif 50000 <= buy < 300000:
    rate = 7.5
elif buy >= 300000:
    rate = 10
else:
    rate = 0

print(rate)