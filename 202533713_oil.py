# 컴퓨터공학과 / 202533713 / 김진서

def error_chk(item, currect_length = False, with_msg = True):
    number_chk = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if with_msg:
        for char in item:
            if char not in number_chk:
                print("\n"+"caution: 잘못된 정보가 입력되었습니다.")
                print(">>> 문자가 아닌 알맞는 숫자를 입력해주세요.")
                print(f'>>> 잘못 입력된 값: {item}')
                return False
            if currect_length and len(item) != currect_length:
                print("\n"+"caution: 잘못된 정보가 입력되었습니다.")
                print(">>> 알맞는 길이의 숫자를 입력해주세요.")
                print(f'>>> 잘못 입력된 값: {item}, 최대 숫자의 길이: {currect_length}')
                return False
    else:
        for char in item:
            if char not in number_chk:
                return False
            if currect_length and len(item) != currect_length:
                return False

    return True

def init_date_setting():
    print("==================================================")
    print(">> 프로그램이 정상적으로 실행되었습니다.")
    print(">> 오늘의 날짜를 입력해주세요.")
    print("(ex. 2025년 01월 01일 -> 250101)")
    init_date = input("> 날짜: ")

    while error_chk(init_date, 6) == False:
        init_date = input("> 날짜: ")
    
    print()
    return init_date

def oil_cost_update():
    oils = {}
    print("==================================================")
    print(f'>> 오늘({year}{month}{day})의 유가 정보를 입력해주세요.')

    while True:
        err_list = []
        oils['고급 휘발유'] = input("> 고급 휘발유(1L): ")
        oils['보통 휘발유'] = input("> 보통 휘발유(1L): ")
        oils['경유'] = input("> 경유(1L): ")
        
        for key, value in oils.items():
            chked_value = error_chk(value, with_msg = False)

            if value[0] == '0' or chked_value == False:
                err_list.append(key)

        if err_list:
            print()
            print("caution: 값이 잘못 입력되었습니다.")
            print(">>> 유가 정보를 재입력해주세요.")
            print(f'>>> 잘못 입력된 값: {", ".join(err_list)}')
        else:
            break

    return oils


def main_screen():
    print()
    print("==================================================")
    print(f'날짜: {year}.{month}.{day}')
    print("1. 주유")
    print("2. 금일 마감")
    print("3. 수입 내역서 확인")
    print("4. 프로그램 종료")
    print("--------------------------------------------------")
    main_num = input("원하는 메뉴를 입력해주세요: ")

    while error_chk(main_num, 1) == False:
        main_num = input("원하는 메뉴를 재입력해주세요: ")
    
    return main_num

def week_receipt():
    print("주간 수입 내역서")

def day_receipt():
    print("일간 수입 내역서")

def fuel_up():
    print()
    print('{:=^40}'.format(" 주유 전 정전기 패드 터치!!! "))
    print('{:^40}'.format("< 금일 유가 >"))

    cnt = 1
    for key, value in oils_info.items():
        print(f'{cnt}. {key}: {value}원 (1L당)')
        cnt+=1
    print("--------------------------------------------------")

    oil_type = input("> 유종에 알맞는 번호를 입력해주세요: ")
    liter = input("> 주유하려는 기름의 양을 입력해주세요(단위: L): ")
    while True:
        if error_chk(oil_type, 1) == False or oil_type not in ['1', '2', '3']:
            oil_type = input("> 유종에 알맞는 번호를 다시 입력해주세요: ")
            continue
        if liter[0] != '0' and error_chk(liter):
            liter = input("> 주유하려는 기름의 양을 다시 입력해주세요(단위: L): ")
            continue
        break

    profit = oils_info # 번호로 값을 받게되면 oils_info = {오일타입: 값}의 구조에서 oils_info = {1: [오일타입, 값], 2: [오일타입, 값], ...} 이런 형식으로 짜여야 함.
            

    success = input("> 주유 준비가 완료되었습니다. 주유 후 \'s\'를 입력해주세요: ")
    day_receipt()

    print(">> 초기화면으로 돌아갑니다.")
    


# 프로그램 실행
start_date = init_date_setting()
year, month, day = start_date[0:2], start_date[2:4], start_date[4:]
oils_info = oil_cost_update()
receipt = {}

while True:
    select_menu = main_screen()
    if select_menu == '1':
        fuel_up()
    elif select_menu == '2':
        pass
    elif select_menu == '3':
        pass
    elif select_menu == '4':
        print(">> 프로그램을 종료합니다.")
        exit()
    else:
        print("caution: 1~4 중의 메뉴를 선택하여 다시 입력해주세요.")
