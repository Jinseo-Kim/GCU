print("202533713 김진서")

## 찍어낼 수를 저장할 num 변수 선언
num = 0

## N, M 입력
N = int(input("N: "))

while True:
    M = int(input("M: "))
    if M % 2 == 0:
        print("M은 홀수여야합니다. 다시 입력해주세요.")
        continue
    break

## 삼각형 출력
if N == 1:
    for i in range(1, M + 1):
        for _ in range(i, M):
            print("  ", end="")

        for _ in range(i):
            num += 1
            print("{:<3}".format(str(num)), end = " ")
        print()

## 역삼각형 출력
if N == 2:
    for i in range(M):
        for _ in range(i):
            print("  ", end="")

        for _ in range(i, M):
            num += 1
            print("{:<3}".format(str(num)), end = " ")
        print()

## 다이아몬드 출력
if N == 3:
    for i in range(M):
        if i < M // 2:
            for _ in range(i, M // 2):
                print("  ", end="")

            for _ in range(i + 1):
                num += 1
                print("{:<3}".format(str(num)), end = " ")
            print()

        else: 
            for _ in range(M // 2, i):
                print("  ", end="")

            for _ in range(i, M):
                num += 1
                print("{:<3}".format(str(num)), end = " ")
            print()

## 모래시계 출력
if N == 4:
    for i in range(M):
        if i < M // 2:
            for _ in range(i):
                print("  ", end="")

            for _ in range(i, M // 2 + 1):
                num += 1
                print("{:<3}".format(str(num)), end = " ")
            print()

        else:
            for _ in range(i + 1, M):
                print("  ", end="")

            for _ in range(M // 2, i + 1):
                num += 1
                print("{:<3}".format(str(num)), end = " ")
            print()

