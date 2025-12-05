ocheon, cheon, obaek, baek, osip, sip = 0, 0, 0, 0, 0, 0

print("202533713 김진서")

money = int(input("잔돈은? "))

if money // 5000 != 0:
    ocheon += money // 5000
    money %= 5000
    print(f"5천원권 : {ocheon}매")

if money // 1000 != 0:
    cheon += money // 1000
    money %= 1000
    print(f"1천원권 : {cheon}매")

if money // 500 != 0:
    obaek += money // 500
    money %= 500
    print(f"500원권 : {obaek}매")

if money // 100 != 0:
    baek += money // 100
    money %= 100
    print(f"100원권 : {baek}매")

if money // 50 != 0:
    osip += money // 50
    money %= 50
    print(f"50원권 : {osip}매")

if money // 10 != 0:
    sip += money // 10
    money %= 10
    print(f"10원권 : {sip}매")
