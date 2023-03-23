n = int(input())
x = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n, 1):
        if (a[i] + a[j] - abs(x[i] - x[j])) / 2 < 0:
            continue
        elif (a[i] + a[j] - abs(x[i] - x[j])) / 2 == 0:
            break