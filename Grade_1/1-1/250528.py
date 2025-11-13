### origin code
'''
import os
import pandas as pd
# from google.colab import output
from datetime import datetime


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    # output.clear()


def today_str():
    today = datetime.now()
    return today.strftime('%Y-%m-%d %H:%M')
    

def input_travel_days():
    print('{:^60}'.format("< 여행지 추천 >"))
    print()
    print(f'오늘 날짜: {today_str()}')
    print()
    start_day = input("> 여행 출발일을 입력해주세요(ex. 2025년 01월 01일 -> 20250101): ")
    end_day = input("> 여행 복귀일을 입력해주세요(ex. 2025년 01월 01일 -> 20250101): ")
    
    # 날짜 형식 검증
    try:
        start_date = datetime.strptime(start_day, '%Y%m%d')
        end_date = datetime.strptime(end_day, '%Y%m%d')
        
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
    """
    '지역명: 코드' 형식의 텍스트 파일을 읽어 {코드: 지역명} 딕셔너리로 변환
    """
    mapping = {}
    with open(txt_path, encoding='utf-8') as f:
        for line in f:
            if ':' in line:
                name, code = line.strip().split(":")
                mapping[int(code.strip())] = name.strip()
    return mapping


def find_top3_locations(file_path, date_str, season, region_map):
    print(">> 추천 여행지는 아래와 같습니다.")
    
    df = pd.read_excel(file_path, header=None)
    df[0] = pd.to_datetime(df[0])
    target_date = pd.to_datetime(date_str)

    daily_data = df[df[0] == target_date]

    if daily_data.empty:
        return f"{date_str} 에 해당하는 데이터 없음"

    if season == 'summer':
        top3 = daily_data.nsmallest(3, 4)  # 최고기온이 낮은 3곳
    else:
        top3 = daily_data.nlargest(3, 3)   # 최저기온이 높은 3곳

    top3['지역명'] = top3[1].map(region_map)

    final_df = top3[['지역명', 2, 3, 4]].copy()
    final_df.columns = ['지역명', '평균기온', '최저기온', '최고기온']
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
    try:    
        final_course = choose_random_course(df_course[df_course['MATCHED_CTPRVN_NM'] == location_name]) 
        cnt = 1
        for course in final_course.iterrows():
            poi_nm = course[1]['POI_NM']
            cl_nm = course[1]['CL_NM']
            print(f'{cnt}. {poi_nm} ({cl_nm})')
            cnt +=1
        while True:
            print()
            save_chk = input("> 추천 여행지를 저장하시겠습니까? (y/n): ").upper()
            clear_screen()
            if save_chk == 'Y' or save_chk == 'N':
                return save_chk
            else:
                print(">> 잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")

    except IndentationError:
        print(">> 해당 지역에 추천 코스가 없습니다. 다른 지역을 선택해주세요.")
        return 'N'
    

def choose_random_course(df): 
    random_course = df.sample(n=5, replace=False)
    return random_course


def main():
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
        if save_chk == 'Y':
            clear_screen()
            print(">> 추천 코스가 저장되었습니다.")
            return save_chk, df, choose_num

# main()
'''

### 1st modification code
'''
import os
import datetime
import pandas as pd
from datetime import datetime as dt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    """
    '지역명: 코드' 형식의 텍스트 파일을 읽어 {코드: 지역명} 딕셔너리로 변환
    """
    mapping = {}
    with open(txt_path, encoding='utf-8') as f:
        for line in f:
            name, code = line.strip().split(":")
            mapping[int(code.strip())] = name
    return mapping


def find_top3_locations(file_path, date_str, season, region_map):
    print(">> 추천 여행지는 아래와 같습니다.")

    df = pd.read_excel(file_path, header=None)
    df[0] = pd.to_datetime(df[0])  # 기존에 object 타입으로 되어 있는 날짜 열을 datetime으로 변환, 그러면 datetime.year와 같은 속성 사용 가능
    target_date = pd.to_datetime(date_str)  #20250101과 같은 형태의 문자열을 datetime으로 변환, 이로인해 year, month, day 속성 사용 가능

    # 월-일 기준으로 과거 데이터 필터링
    target_month = target_date.month
    target_day = target_date.day
    df['month'] = df[0].dt.month
    df['day'] = df[0].dt.day

    # 월/일이 일치하는 과거 데이터만 필터링
    daily_data = df[(df['month'] == target_month) & (df['day'] == target_day)]

    if daily_data.empty:
        return f"{target_month:02d}-{target_day:02d} 에 해당하는 과거 데이터 없음"

    # 지역별 평균 기온 계산
    grouped = daily_data.groupby(1)[[2, 3, 4]].mean().round(1).reset_index()
    grouped.columns = ['지역코드', '평균기온', '최저기온', '최고기온']

    # 추천 기준 적용
    if season == 'summer':
        top3 = grouped.nsmallest(3, '최고기온')  # 최고기온이 낮은 3곳 (여름 기준준)
    else:
        top3 = grouped.nlargest(3, '최저기온')  # 최저기온이 높은 3곳 (겨울 기준)

    # 지역명 매핑
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

    try:
        final_course = choose_random_course(df_course[df_course['MATCHED_CTPRVN_NM'] == location_name])
        cnt = 1
        for course in final_course.iterrows():
            poi_nm = course[1]['POI_NM']
            cl_nm = course[1]['CL_NM']
            print(f'{cnt}. {poi_nm} ({cl_nm})')
            cnt +=1
        while True:
            print()
            save_chk = input("> 추천 여행지를 저장하시겠습니까? (y/n): ").upper()
            clear_screen()
            if save_chk == 'Y' or save_chk == 'N':
                return save_chk
            else:
                print(">> 잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")

    except IndentationError:
        print(">> 해당 지역에 추천 코스가 없습니다. 다른 지역을 선택해주세요.")
        return 'N'


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
        if save_chk == 'Y':
            clear_screen()
            print(">> 추천 코스가 저장되었습니다.")
            return save_chk, df, choose_num
        

recommend_course_main()
'''

import os
import datetime
import pandas as pd
from datetime import datetime as dt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    """
    '지역명: 코드' 형식의 텍스트 파일을 읽어 {코드: 지역명} 딕셔너리로 변환
    """
    mapping = {}
    with open(txt_path, encoding='utf-8') as f:
        for line in f:
            name, code = line.strip().split(":")
            mapping[int(code.strip())] = name
    return mapping


def find_top3_locations(file_path, date_str, season, region_map):
    print(">> 추천 여행지는 아래와 같습니다.")

    df = pd.read_excel(file_path, header=None)
    df[0] = pd.to_datetime(df[0])  # 기존에 object 타입으로 되어 있는 날짜 열을 datetime으로 변환, 그러면 datetime.year와 같은 속성 사용 가능

    target_date = pd.to_datetime(date_str)  #20250101과 같은 형태의 문자열을 datetime으로 변환, 이로인해 year, month, day 속성 사용 가능

    # 월-일 기준으로 과거 데이터 필터링
    target_month = target_date.month
    target_day = target_date.day
    df['month'] = df[0].dt.month  # series의 dt 속성을 사용하여 datetime 속성에 접근, 그리고 month열을 추가
    df['day'] = df[0].dt.day  # series의 dt 속성을 사용하여 datetime 속성에 접근, 그리고 day열을 추가

    # 월/일이 일치하는 과거 데이터만 필터링
    daily_data = df[(df['month'] == target_month) & (df['day'] == target_day)]
    print(daily_data)

    # 지역별 평균 기온 계산
    grouped = daily_data.groupby(1)[[2, 3, 4]].mean().round(1).reset_index()
    grouped.columns = ['지역코드', '평균기온', '최저기온', '최고기온']

    # 추천 기준 적용
    if season == 'summer':
        top3 = grouped.nsmallest(3, '최고기온')  # 최고기온이 낮은 3곳 (여름 기준준)
    else:
        top3 = grouped.nlargest(3, '최저기온')  # 최저기온이 높은 3곳 (겨울 기준)

    # 지역명 매핑
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
        save_chk = input("> 이전화면으로 이동하시겠습니까까? (y/n): ").upper()
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

region_map = load_region_code_map('Region_Code_Pairs.txt')
df = find_top3_locations('Merged_Data.xlsx', '20250101', 'winter', region_map)