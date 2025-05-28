import os, bisect
from datetime import datetime
import pandas as pd

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_travel_days():
    print('{:^60}'.format("< 여행지 추천>"))
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

def stay_period(start_date, end_date):
    period_day = 0
    leap = 1 if start_date.year % 4 == 0 else 0 
    fixed_day = [None, 31, 28+leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    period_year = (end_date.year - start_date.year)*365
    for i in range(start_date.month, end_date.month+1):
        period_day += fixed_day[i-1]

    stay_days = period_year + end_date.day - start_date.day

    return stay_days

def recom_travel():
    season = ''
    travel_days = input_travel_days()
    if travel_days is None:
        return None
    
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
    print(">> 추천 여행지는 아래와 같습니다.")
    choose_num = int(input("> 선호하는 여행지의 번호를 입력해주세요(1~3): "))
    
    return start_date_print, end_date_print, period_date, season, choose_num



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

def find_top3_locations_binary(file_path, date_str, season, region_map):
    # 파일 불러오기 및 정렬
    df = pd.read_excel(file_path, header=None)
    df_sorted = df.sort_values(by=0).reset_index(drop=True)
    
    # 날짜 리스트만 추출
    dates = df_sorted[0].tolist()
    target_date = pd.to_datetime(date_str)

    # 이진 탐색으로 범위 찾기
    left = bisect.bisect_left(dates, target_date)
    right = bisect.bisect_right(dates, target_date)

    if left == right:
        return f"{date_str} 에 해당하는 데이터 없음"

    daily_data = df_sorted.iloc[left:right]

    # 계절별 조건
    if season == 'summer':
        top3 = daily_data.nsmallest(3, 4) # 최고기온(열 4)
    else:
        top3 = daily_data.nlargest(3, 3) # 최저기온(열 3)

    # 지점번호 → 지역명 매핑
    if region_map:
        top3['지역명'] = top3[1].map(region_map)
    else:
        top3['지역명'] = top3[1]

    # 필요한 열 추출
    final_df = top3[['지역명', 2, 3, 4]].copy()
    final_df.columns = ['지역명', '평균기온', '최저기온', '최고기온']

    # 인덱스를 1부터 시작하는 순번으로 지정
    final_df.index = range(1, len(final_df) + 1)
    
    return final_df


def main():
    clear_screen()
    start_date_print, end_date_print, period_date, season, choose_num = recom_travel()
    region_map = load_region_code_map('Region_Code_Pairs.txt')
    df = find_top3_locations_binary('Merged_Data.xlsx', start_date_print, season, region_map)
    choose_course(start_date_print, end_date_print, period_date, df, choose_num)

def choose_course(start_date_print, end_date_print, period_date, df, choose_num):
    print('{:^60}'.format("< 여행지 추천>"))
    print(f"여행 일정: {start_date_print} ~ {end_date_print} ({period_date}박{period_date + 1}일)")
    print(f'< 선택 여행지: {df.iloc[choose_num - 1]["지역명"]}>')
    print(">> 유명 음식: ")
    



recom_travel()


