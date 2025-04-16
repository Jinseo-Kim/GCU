# 컴퓨터공학과 / 202533713 / 김진서

def error_chk(item, currect_length):
    number_chk = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for char in item:
        if char not in number_chk:
            print("\n"+"caution: 잘못된 날짜 정보가 입력되었습니다.")
            print(">>> 문자가 아닌 알맞는 숫자를 입력해주세요.")
            print(f'>>> 잘못 입력된 값: {item}\n')
            return False
        if len(item) > currect_length:
            print("\n"+"caution: 잘못된 날짜 정보가 입력되었습니다.")
            print(">>> 알맞는 길이의 숫자를 입력해주세요.")
            print(f'>>> 잘못 입력된 값: {item}\n')
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
    print("==================================================")
    print(f'>> 오늘({year}{month}{day})의 유가 정보를 입력해주세요.')
    while True:
        high = input("> 고급 휘발유(1L): ")
        regular = input("> 보통 휘발유(1L): ")
        diesel = input("> 경유(1L): ")
        print()

        print(">> 입력된 정보는 아래와 같습니다.")
        print(f'> 고급 휘발유(1L): {high}')
        print(f'> 보통 휘발유(1L): {regular}')
        print(f'> 경유(1L): {diesel}')
        recheck = input(">> 입력하신 정보가 맞습니까?(y or n): ")

        while True:
            if recheck == 'y':
                print()
                return int(high), int(regular), int(diesel)
            if recheck == 'n':
                print("\n"+"유가 정보를 다시 입력해주세요.")
                break
            recheck = input(">> 입력하신 정보가 맞다면 y를, 틀리다면 n을 입력해주세요: ")



def main_screen(yy, mm, dd):
    print("==================================================")
    print(f'날짜: {yy}.{mm}.{dd}')
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
    print('{:=^40}'.format(" 주유 전 정전기 패드 터치!!! "))
    
    


# 프로그램 실행
start_date = init_date_setting()
year, month, day = start_date[0:2], start_date[2:4], start_date[4:]
high_gsl, regular_gsl, diesel = oil_cost_update()

while True:
    select_menu = main_screen(year, month, day)
    if select_menu == '1':
        print()
        fuel_up()
    elif select_menu == '2':
        pass
    elif select_menu == '3':
        pass
    else:
        print("프로그램을 종료합니다.")
        exit()
    
        
    





