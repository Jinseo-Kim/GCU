# 컴퓨터공학과 / 202533713 / 김진서

def init_date_setting():
    print("프로그램이 정상적으로 실행되었습니다.")
    print("오늘의 날짜를 입력해주세요.")
    print("(ex. 2025년 01월 01일 -> 250101)")
    result = False

    while result == False:
        init_date = input("날짜: ")
        result = error_chk(init_date, 6)
 
    return init_date


def error_chk(item, currect_length):
    number_chk = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for char in item:
        if char not in number_chk:
            print("잘못된 날짜 정보가 입력되었습니다.")
            print("> 알맞는 숫자를 입력해주세요. <")
            print(f'잘못 입력된 문자: {char}')
            return False
        if len(item) > currect_length:
            print("잘못된 날짜 정보(숫자의 길이)가 입력되었습니다.")
            print("> 알맞는 길이의 숫자를 입력해주세요. <")
            print(f'잘못 입력된 숫자: {item}')
            return False

    return True
        
start_date = init_date_setting()
year, month, day = start_date[0:2], start_date[2:4], start_date[4:6]

print(start_date, year, month, day)

def week_receipt(end_date):
    print("주간 수입 내역서")

def day_receipt(start_date):
    print("일간 수입 내역서")

def oil_cost_update():
    print(f'오늘({year}{month}{day})의 유가 정보를 입력해주세요.')
    high = int(input("고급 휘발유: "))
    normal = int(input("일반 휘발유: "))
    other = int(input("경유"))

