import random

## 각 숫자에 맞는 가위, 바위, 보를 key: value 로 매칭
SRP = {0: "가위", 1: "바위", 2: "보"}

win_com, win_human = 0, 0

print("202533713 김진서")

print("가위바위보 게임")
print("컴퓨터 : 0승 0패, 당신 : 0승 0패")

for cnt in range(1, 6):
    print(f"(라운드 {cnt})")

    while True:
        com = (random.randint(0, 2)) ## 0 ~ 2까지의 값만 받음
        print("컴퓨터가 결정했습니다.")

        human = int(input("무엇을 내시겠습니까? (가위 : 0, 바위 : 1, 보 : 2)"))

        if com == human:
            print("비겼습니다. 다시 시작합니다.")
            continue

        break
    
    ### SRP(dict)을 통해 입력받은 human, com 변수의 정수값으로 가위, 바위, 보의 문자값을 매칭
    ## 사람이 이겼을 경우 (보 - 바위, 바위 - 가위)
    if (human - com == 1):
        print(f"컴퓨터는 {SRP.get(com)}, 당신은 {SRP.get(human)}, 당신이 이겼습니다.")
        win_human += 1

    ## 컴퓨터 이겼을 경우 (보 - 바위, 바위 - 가위)
    if (com - human == 1):
        print(f"컴퓨터는 {SRP.get(com)}, 당신은 {SRP.get(human)}, 컴퓨터가 이겼습니다.")
        win_com += 1

    ## 사람이 이겼을 경우 (가위 - 보)
    if (com - human == 2):
        print(f"컴퓨터는 {SRP.get(com)}, 당신은 {SRP.get(human)}, 당신이 이겼습니다.")
        win_human += 1

    ## 컴퓨터 이겼을 경우 (가위 - 보)
    if (human - com == 2):
        print(f"컴퓨터는 {SRP.get(com)}, 당신은 {SRP.get(human)}, 컴퓨터가 이겼습니다.")
        win_com += 1
    
    print(f"컴퓨터 : {win_com}승 {cnt - win_com}패, 당신 : {win_human}승 {cnt - win_human}패\n")
    