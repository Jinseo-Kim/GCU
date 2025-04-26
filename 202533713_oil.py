# 컴퓨터공학과 / 202533713 / 김진서

# 입력값이 알맞는 포맷으로 쓰였는지 확인 후 True/False로 반환.
# 유효하지 않은 입력값일 때, with_msg가 True이면 경고 메시지를 출력.
def error_check(item, expected_length=False, with_msg=True):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if with_msg:
        # msg를 띄우며 각 문자와 길이가 알맞는지 확인
        for char in item:
            if char not in digits:
                print("\n" + "caution: 잘못된 정보가 입력되었습니다.")
                print(">>> 문자가 아닌 알맞는 숫자를 입력해주세요.")
                print(f'>>> 잘못 입력된 값: {item}')
                return False
        if expected_length and len(item) != expected_length:
            print("\n" + "caution: 잘못된 정보가 입력되었습니다.")
            print(">>> 알맞는 길이의 숫자를 입력해주세요.")
            print(f'>>> 잘못 입력된 값: {item}, 알맞는 숫자의 길이: {expected_length}')
            return False
    else: # msg를 띄우지 않고 True, False만 판단하려는 경우
        for char in item:
            if char not in digits:
                return False
        if expected_length and len(item) != expected_length:
            return False
    return True


# 프로그램 실행 후 날짜 초기값 세팅팅
def init_date():
    """
    사용자로부터 입력값을 받아 현재 날짜를 초기화
    년, 월, 일, 윤년의 여부(윤년 = 1, 윤년이 아닌 경우 = 0)를 반환
    """
    fixed_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(">> 오늘의 날짜를 입력해주세요.")
    print("(ex. 2025년 01월 01일 -> 20250101)")
    date_input = input("> 날짜: ")
    leap = 0
    while True:
        if error_check(date_input, expected_length=8) == False:
            date_input = input("> 날짜: ")
            continue
        year, month, day = int(date_input[0:4]), int(date_input[4:6]), int(date_input[6:])

        if year % 4 == 0:
            fixed_day[1] = 29# 날짜가 변경될 때마다 당일의 유가 정보를 업데이트
            leap = 1
        if month > 12 or month < 1:
            print("caution: 잘못된 날짜입니다.")
            print(f'>>> 잘못 입력된 값: {date_input}, 1~12월 사이의 숫자를 입력해주세요.')
            date_input = input("> 날짜: ")
            print()
        elif day > fixed_day[month-1] or day < 1:
            print("caution: 잘못된 날짜입니다.")
            print(f'>>> 잘못 입력된 값: {date_input}, 1~{fixed_day[month - 1]}일 사이의 숫자를 입력해주세요.')
            date_input = input("> 날짜: ")
            print()
        else:
            break

    return year, month, day, leap


# main_screen()에서 2(금일 마감) 선택 시 자동으로 날짜 갱신
def date_update(leap):
    print()
    print(">> 금일 마감이 완료되었습니다.")
    print(">> 날짜가 자동 갱신됩니다.")

    fixed_day = [31, 28+leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    update_year = int(year)
    update_month = int(month)
    update_day = int(day) + 1

    if update_day > fixed_day[update_month - 1]:
        update_day = 1
        update_month += 1
    if update_month > 12:
        update_month = 1
        update_year += 1
    if update_year % 4 != 0:
        leap = 0
    else:
        leap = 1

    return update_year, update_month, update_day, leap


# 날짜가 변경될 때마다 당일의 유가 정보를 업데이트
def oil_cost_update():
    oils = {}
    print()
    print("=" * 50)
    print(f'>> 오늘({year}년 {month}월 {day}일)의 유가 정보를 입력해주세요.')
    while True:
        err_list = []
        oils['1'] = ["고급 휘발유", input("> 고급 휘발유(1L): "), 0]
        oils['2'] = ["보통 휘발유", input("> 보통 휘발유(1L): "), 0]
        oils['3'] = ["경유", input("> 경유(1L): "), 0]

        if input("> 다시 입력하고 싶으시면 'y'를 아니라면 아무 키를 눌러주세요: ") == 'y':
            print()
            print(">> 유가 정보를 재입력합니다.")
            continue

        for value in oils.values():
            oil_type_name, price = value[0], value[1]
            is_valid_number = error_check(price, with_msg=False)

            if price[0] == '0' or is_valid_number == False:
                err_list.append(oil_type_name)

        if err_list:
            print()
            print("caution: 값이 잘못 입력되었습니다.")
            print(">>> 유가 정보를 재입력해주세요.")
            print(f'>>> 잘못 입력된 유종: {", ".join(err_list)}')
        else:
            for chg_type_cost in oils.values():
                chg_type_cost[1] = int(chg_type_cost[1])
            break

    return oils


# 사용자가 선택 가능한 메뉴가 있는 메인 화면
def main_screen():
    print()
    print("=" * 50)
    print(f'날짜: {year}년 {month}월 {day}일')
    print("1. 주유")
    print("2. 금일 마감")
    print("3. 수입 내역서 확인")
    print("4. 프로그램 종료")
    menu_choice = input("> 원하는 메뉴를 입력해주세요: ")
    return menu_choice


# 유종 선택 및 주유량을 입력받아 주유 진행
def fuel_up(oils):
    print()
    print('{:=^40}'.format(" 주유 전 정전기 패드 터치!!! "))
    print('{:^40}'.format("< 금일 유가 >"))

    for key, value in oils.items():
        # 각 연료 타입과 리터당 금액을 표시
        print(f'{key}. {value[0]}: {value[1]:,}원/1L')
    oil_type = input("> 유종에 알맞는 번호를 입력해주세요: ")
    liter = input("> 주유하려는 기름의 양을 입력해주세요(단위: L): ")

    while True:
        # 입력받은 연료 타입이 유효한지 확인
        if error_check(oil_type, expected_length=1) == False or oil_type not in ['1', '2', '3']:
            oil_type = input("> 유종에 알맞는 번호를 다시 입력해주세요: ")
            liter = input("> 주유하려는 기름의 양을 입력해주세요(단위: L): ")
            continue
        # 입력받은 리터 수가 유효한지 확인
        if error_check(liter) == False or liter == "":
            if liter == "":
                print()
                print("caution: 잘못된 정보가 입력되었습니다.")
                print(">>> 문자가 아닌 알맞는 숫자를 입력해주세요.")
                print(f'>>> 잘못 입력된 값: {liter}')
            liter = input("> 주유하려는 기름의 양을 다시 입력해주세요(단위: L): ")
            continue
        break

    # 리터 수 및 수입 계산
    oils[oil_type][2] += int(liter) # 넣은 기름의 타입에 알맞는 기름의 양
    profit = oils[oil_type][1] * int(liter) # 넣은 기름의 가격 = 유종 * 기름의 양
    print()
    print(f">> {oils[oil_type][0]} {liter}L 주유하였습니다.")
    print(f">> 주유한 기름의 가격: {profit:,}원")
    print(">> 초기화면으로 돌아갑니다.")

    return profit


# receipt 딕셔너리에 현재 날짜의 수입을 기록
def add_profit(receipt, profit):
    day_key = str(day_idx)
    if day_key not in receipt:
        receipt[day_key] = [year, month, day, profit]
    else:
        # 기존 수입에 현재 수입을 추가
        receipt[day_key][-1] += profit
    return receipt


# 메뉴 선택에 따른 수입 내역서 화면 출력
def menu_receipt(receipt):
    no_receipt = print_receipt(receipt)
    if no_receipt:
        return
    
    while True:
        print("> 원하는 메뉴를 입력해주세요.")
        select = input("> 초기화면 이동-q, 상세 내역 확인-숫자번호(ex.1): ")

        if select == 'q':
            print(">> 초기화면으로 돌아갑니다.")
            break
        elif select not in receipt:
            print()
            print("caution: 잘못된 번호가 입력되었습니다.")
            continue
        else:
            detail_receipt(receipt, int(select))
            print_receipt(receipt)


# 수입 내역서의 메인 화면 출력
# 현재까지의 수입에 대한 내역이 모두 출력됨
def print_receipt(receipt):
    print()
    if not receipt:
        print(">>> 수입 내역서가 없습니다.")
        return True
    print("=" * 50)
    print('{:^40}'.format("<수입 내역서>"))
    print(f'현재 날짜: {year}년 {month}월 {day}일')
    for key, value in receipt.items():
        print(f'>> {key}. {value[0]}년 {value[1]}월 {value[2]}일\t수입: {value[3]:,}원')
    print("=" * 50)
    print()


# 선택된 날짜에 대한 상세 내역 출력
def detail_receipt(receipt, select_num):
    print()
    print("=" * 50)
    print('{:^40}'.format("<상세 수입 내역서>"))
    sel_year, sel_month, sel_day, _ = receipt[str(select_num)]
    print(f'선택 날짜: {sel_year}년 {sel_month}월 {sel_day}일')
    for key, value in receipt_details[select_num].items():
        print(f'>> {key}. {value[0]}: {value[1]:,}원/{value[2]:,}L') 
    print(f'>> 총 수입: {receipt[str(select_num)][-1]:,}원')
    print("=" * 50)
    input("아무 키를 눌러주시면 이전화면으로 돌아갑니다...")
    print()



# 프로그램 실행
print("=" * 50)
print(">> 프로그램이 정상적으로 실행되었습니다.")

year, month, day, leap = init_date()
oils_info = oil_cost_update()  # oils_info = {'1': [oil_type, price(int), liter(int)]}
receipt = {}         # receipt = {'1': [year, month, day, profit]}
receipt_details = {} # receipt_details = {1: {'1': [oil_type, price(int), liter(int)], ...}}
day_idx = 1

while True:
    menu_choice = main_screen()
    if menu_choice == '1':
        profit = fuel_up(oils_info)
        receipt = add_profit(receipt, profit)
        receipt_details[day_idx] = oils_info.copy()
    elif menu_choice == '2':
        year, month, day, leap = date_update(leap)
        oils_info = oil_cost_update()
        day_idx += 1
        print(">> 유가 정보가 갱신되었습니다.")
    elif menu_choice == '3':
        menu_receipt(receipt)
    elif menu_choice == '4':
        print(">> 프로그램을 종료합니다.")
        exit()
    else:
        print()
        print("caution: 1~4 중의 메뉴를 선택하여 다시 입력해주세요.")
