i = 0
while True:
    i += 1
    a = int(input())
    
    if a >= 10:
        print(i)
        break
    elif a == 5:
        print("hi")
        continue
    print(i)