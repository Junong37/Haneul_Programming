def is_ja(str):
    k = str[-1]
    if "가" <= k <= "힣":
        return (ord(k) - ord("가")) % 28 > 0
    else:
        return
a = input()
if is_ja(a):
    print("나는 {}을 살렸다".format(a))
elif is_ja(a) == False:
    print("나는 {}를 살렸다".format(a))
else:
    print("None")