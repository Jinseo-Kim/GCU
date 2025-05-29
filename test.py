import json
import os
import datetime
import pandas as pd
from datetime import datetime as dt
# from google.colab import output

cal_filename = "calendar.json"
rev_filename = "review.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    # output.clear()

def today_str():
    today = dt.now()
    return today.strftime('%Y-%m-%d')


def input_travel_days():
    print('{:^60}'.format("< 여행지 추천 >"))
    print()
    print(f'오늘 날짜: {today_str()}')
    print()
    start_day = input("> 여행 출발일을 입력해주세요(ex. 2025년 01월 01일 -> 20250101): ")
    end_day = input("> 여행 복귀일을 입력해주세요(ex. 2025년 01월 01일 -> 20250101): ")

    # 날짜 형식 검증
    try:
        start_date = dt.strptime(start_day, '%Y%m%d')
        end_date = dt.strptime(end_day, '%Y%m%d')

        if start_date >= end_date:
            raise ValueError("출발일은 복귀일보다 이전이어야 합니다.")

    except ValueError as e:
        print(f"오류: {e}")
        return None

    clear_screen()
    return start_date, end_date


def travel_info(travel_days):
    season = ''
    if travel_days is None:
        return None

    print('{:^60}'.format("< 여행지 추천 >"))
    print(f'오늘 날짜: {today_str()}')
    print()

    start_date, end_date = travel_days

    if start_date.month in [6, 7, 8]:
        season = 'summer'
    elif start_date.month in [12, 1, 2]:
        season = 'winter'

    start_date_print = start_date.strftime('%Y-%m-%d')
    end_date_print = end_date.strftime('%Y-%m-%d')

    period_date = stay_period(start_date, end_date)
    print(f"여행 일정: {start_date_print} ~ {end_date_print} ({period_date}박{period_date + 1}일)")
    print()
    print(f">> 선택한 여행 일정은 {start_date_print} ~ {end_date_print}일로 '{period_date}박{period_date + 1}일' 입니다.")
    return start_date_print, end_date_print, period_date, season


def stay_period(start_date, end_date):
    period_day = 0
    leap = 1 if start_date.year % 4 == 0 else 0
    fixed_day = [None, 31, 28+leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    period_year = (end_date.year - start_date.year)*365
    for i in range(start_date.month, end_date.month+1):
        period_day += fixed_day[i-1]

    stay_days = period_year + end_date.day - start_date.day
    return stay_days


def load_region_code_map(txt_path):
    mapping = {}
    with open(txt_path, encoding='utf-8') as f:
        for line in f:
            name, code = line.strip().split(":")
            mapping[int(code.strip())] = name
    return mapping


def find_top3_locations(file_path, date_str, season, region_map):
    print(">> 추천 여행지는 아래와 같습니다.")

    df = pd.read_excel(file_path, header=None)
    df[0] = pd.to_datetime(df[0])
    target_date = pd.to_datetime(date_str)

    target_month = target_date.month
    target_day = target_date.day
    df['month'] = df[0].dt.month
    df['day'] = df[0].dt.day

    daily_data = df[(df['month'] == target_month) & (df['day'] == target_day)]

    if daily_data.empty:
        return f"{target_month:02d}-{target_day:02d} 에 해당하는 과거 데이터 없음"

    grouped = daily_data.groupby(1)[[2, 3, 4]].mean().round(1).reset_index()
    grouped.columns = ['지역코드', '평균기온', '최저기온', '최고기온']

    if season == 'summer':
        top3 = grouped.nsmallest(3, '최고기온')  # 최고기온이 낮은 3곳 (여름 기준)
    else:
        top3 = grouped.nlargest(3, '최저기온')  # 최저기온이 높은 3곳 (겨울 기준)

    top3['지역명'] = top3['지역코드'].map(region_map)

    final_df = top3[['지역명', '평균기온', '최저기온', '최고기온']].copy()
    final_df.index = range(1, len(final_df) + 1)

    print(final_df)
    return final_df


def choose_course(start_date_print, end_date_print, period_date, df, choose_num):
    clear_screen()
    print('{:^37}'.format("< 여행지 추천 >"))
    print(f"여행 일정: {start_date_print} ~ {end_date_print} ({period_date}박{period_date + 1}일)")
    location_name = df.iloc[choose_num - 1]['지역명']
    text = "< 선택 여행지: {} >".format(location_name)
    print("{:^37}".format(text))
    print(">> 추천 계획 및 코스")

    df_course = pd.read_csv('filtered_course.csv', encoding='utf-8')

    final_course = choose_random_course(df_course[df_course['MATCHED_CTPRVN_NM'] == location_name])
    cnt = 1
    for course in final_course.iterrows():
        poi_nm = course[1]['POI_NM']
        cl_nm = course[1]['CL_NM']
        print(f'{cnt}. {poi_nm} ({cl_nm})')
        cnt +=1
    while True:
        print()
        save_chk = input("> 이전화면으로 이동하시겠습니까? (y/n): ").upper()
        clear_screen()
        if save_chk == 'Y':
            return save_chk
        elif save_chk == 'N':
            save_chk = input("> 메인화면으로 이동하시려면 'q'를 눌러주세요: ").upper()
            return save_chk
        else:
            print(">> 잘못된 입력입니다. 'q'를 입력해주세요.")


def choose_random_course(df):
    random_course = df.sample(n=5, replace=False)
    return random_course


def recommend_course_main():
    clear_screen()
    travel_days = input_travel_days()
    start_date_print, end_date_print, period_date, season = travel_info(travel_days)
    region_map = load_region_code_map('Region_Code_Pairs.txt')
    df = find_top3_locations('Merged_Data.xlsx', start_date_print, season, region_map)
    first_time = True
    print()

    while True:
        if first_time == False:
            print('{:^37}'.format("< 여행지 추천 >"))
            print(f"여행 일정: {start_date_print} ~ {end_date_print} ({period_date}박{period_date + 1}일)")
            print(">> 추천 여행지는 아래와 같습니다.")
            print(df)
            print()
        first_time = False
        choose_num = int(input("> 추천 여행지 중 하나를 선택해주세요(1, 2, 3): "))
        save_chk = choose_course(start_date_print, end_date_print, period_date, df, choose_num)
        if save_chk == 'Q':
            clear_screen()
            print(">> 메인화면으로 이동합니다.")
            break
        else:
            print(">> 잘못입력하여 이전화면으로 돌아갑니다.")

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def cal_append():

  if os.path.exists(cal_filename):
    with open(cal_filename, "r") as f:
      calendar = json.load(f)
  else:
    calendar = {}

  date = input("날짜를 입력하세요 (ex. 2025-01-01): ")
  plan = input("일정을 입력하세요: ")

  if date in calendar:
    calendar[date].append(plan)
  else:
    calendar[date] = [plan]

  with open(cal_filename, "w") as f:
    json.dump(calendar, f)

  print("\n\n일정이 저장되었습니다!\n\n")


def cal_check():
  if os.path.exists(cal_filename):
    with open(cal_filename, "r") as f:
      calendar = json.load(f)
  else:
    calendar = {}
  date = input("확인할 날짜를 입력하세요 (예: 2025-06-01): ")

  if date in calendar:
    print(f"\n{date}의 일정:")
    for i, event in enumerate(calendar[date], start=1):
      print(f"{i}. {event}")
    return(date)
  else:
    print("\n\n해당 날짜에는 저장된 일정이 없습니다.\n\n")


def cal_remove():

  if os.path.exists(cal_filename):
    with open(cal_filename, "r") as f:
      calendar = json.load(f)
  else:
    calendar = {}

  date=input('\n삭제할 날짜를 입력하세요 (ex. 2025-01-01): ')

  if date in calendar:
    print(f"\n{date}의 일정 목록:")
    for i, event in enumerate(calendar[date], start=1):
        print(f"{i}. {event}")

    idx=int(input('\n삭제할 일정 번호를 입력하세요: '))-1

    if 0 <= idx and idx < len(calendar[date]):
        calendar[date].pop(idx)
        print("삭제 완료!")

        with open(cal_filename, "w") as f:
          json.dump(calendar, f)
    else:
      print("\n\n잘못된 번호입니다.\n\n")
  else:
    print("\n\n해당 날짜는 없습니다.\n\n")

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def review():

  if os.path.exists(rev_filename):
    with open(rev_filename, "r") as f:
      review = json.load(f)
  else:
    review = {}
  rev_check()
  date = input("날짜를 입력하세요 (ex. 2025-01-01): ")
  write = input("여행 후기를 간단하게 남겨주세요! : ")

  if date in review:
    review[date].append(write)
  else:
    review[date] = [write]

  with open(rev_filename, "w") as f:
    json.dump(review, f)

  print("\n후기가 저장되었습니다!\n\n")


def rev_remove():

  if os.path.exists(rev_filename):
    with open(rev_filename, "r") as f:
      review = json.load(f)
  else:
    review = {}

  rev_check()

  date=input('\n삭제할 날짜를 입력하세요 (ex. 2025-01-01): ')

  if date in review:
    del review[date]

    print('\n삭제가 완료되었습니다!\n')

    with open(rev_filename, "w") as f:
      json.dump(review, f)

  else:
    print("\n해당 날짜는 없습니다.\n\n")

def rev_check():

  if os.path.exists(rev_filename):
    with open(rev_filename, "r") as f:
      review = json.load(f)
  else:
    review = {}
  for date in sorted(review.keys()):
    print(date)

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def main_menu():
  today = datetime.date.today()
  print(f"\n📅 오늘 날짜: {today}")
  print("\n======== 메뉴 ========\n")
  print("1. 여행지 추천")
  print("2. 캘린더 작성")
  print("3. 여행 후기 작성")
  print("\n=====================\n")

  choice = input("원하는 메뉴 번호를 입력하세요: ")

  if choice == "1":
    return 1
  elif choice == "2":
    return 2
  elif choice == "3":
    return 3
  else:
    print("\n잘못된 입력입니다. 1~3 중에서 선택해주세요.\n")

def cal_menu():
  while True:
    print("\n1. 일정 확인")
    print("2. 일정 추가")
    print("3. 일정 삭제")
    print("4. 메인메뉴로 나가기\n")
    select=int(input("원하는 메뉴 번호를 입력하세요: "))
    if select==1:
      cal_check()
    elif select==2:
      cal_append()
    elif select==3:
      cal_remove()
    elif select==4:
      return 'main'
    else:
      print("\n잘못된 입력입니다. 1~2 중에서 선택해주세요.\n")

def rev_menu():
  while True:
    print("\n1. 후기 작성")
    print("2. 후기 삭제")
    print("3. 후기 작성된 날짜 확인")
    print("4. 메인메뉴로 나가기\n")
    select=int(input("원하는 메뉴 번호를 입력하세요: "))
    if select==1:
      review()
    elif select==2:
      rev_remove()
    elif select==3:
      rev_check()
    elif select==4:
      return 'main'
    else:
      print("\n잘못된 입력입니다. 1 ~ 4 중에서 선택해주세요.\n")

while True:
  select = main_menu()
  if select == 1:
    recommend_course_main()
  elif select == 2:
    cal_result = cal_menu()
    if cal_result == 'main':
      continue
  elif select == 3:
    rev_result = rev_menu()
    if rev_result == 'main':
      continue
  else:
    pass