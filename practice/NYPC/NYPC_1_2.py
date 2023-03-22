n, x = map(int, input().split())

map_list = [0 for i in range(64)]
for i in [8, 17, 20, 31, 37, 39, 44, 49, 60, 63]:
    map_list[i-1] = 1
for i in [2, 6, 10, 19, 23, 25, 27, 43]:
    map_list[i-1] = 2
for i in [13, 33, 41, 52, 53, 54]:
    map_list[i-1] = 3
for i in [55, 64]:
    map_list[i-1] = 5

for i in range(n):
    for j in range(6):
        pass