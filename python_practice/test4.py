#369
import time

i = 0

while True:
    time.sleep(0.1)
    i += 1
    i = str(i)

    if "3" in i or "6" in i or "9" in i:
        print("짝")
    else:
        print(i)
        
    i = int(i)