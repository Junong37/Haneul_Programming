# 다음은 입력한 값만큼 별을 나열한 코드이다 (예제 참고). 하지만 입력값이 10 이상일 때는 "ERROR"를 출력한다. 빈칸을 알맞게 채워 넣으시오.

num = int(input())

if num >= 10:
    print("ERROR")
else:
    for i in range(num):
        print(' ' * (num - i - 1) + '*' * (i + 1))