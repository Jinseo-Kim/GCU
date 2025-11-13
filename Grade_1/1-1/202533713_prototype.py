# 컴퓨터공학과 / 202533713 / 김진서
# 이건 좀 더 고민해보는 걸로


# 청구기호 / 도서명 / 저자 / 대출상태 / 반납예정일 
philosophie = {
    'width':['0', '0', '0'],
    "1":["199.1-에298ㅇ1", "인생의 의미", "토마스 힐란드 에릭센", ['대출가능', '대여중'], ['-'], False],
    "2":["199.1-법296ㅇ1", "인생수업", "법륜", ['대출가능', '대여중'], ['-'], False],
    "3":["199.1-리198ㄱ", "기록이라는 세계", "리니", ['대출가능', '대여중'], ['-'], False],
    "4":["186.3-클294ㅁ", "마음의 기술", "안-엘렌 클레르, 뱅상 트리부 [공]", ['대출가능', '대여중'], ['-'], False],
    "5":["104-한44ㅂ", "불안사회", "한병철스", ['대출가능', '대여중'], ['-'], False], 
    }

histories = {
    'width':['0', '0', '0'],
    "1":["909.54-이76ㅅ", "생존자들", "이준호", "O", ['-']],
    "2":["990.9-썬878ㄱ", "그날의 세계사", "썬킴", "O", ['-']],
    "3":["981.4-정57ㅂ", "(셀프트래블)베트남", "정승원", "O", ['-']],
    "4":["909-구54ㅆ", "쓸모 있는 세계사 365", "요나스 구세나에르츠 , 벤저민 고이배르츠 , 로랑 포쉐 [공]", "O", ['-']],
    "5":["990.9-장68ㅈ", "작심하고 다시, 기자", "장인수", "O", ['-']],
}

Library_books = [
    philosophie,
    histories

]

search_number = {
    'philosophie_num':[value[0] for key, value in philosophie.items() if key != 'width']
}

def calc_maxlength(section, values):
    for value in values:
        for i in range(0,3):
            if len(value[i]) > int(section['width'][i]):
                section['width'][i] = len(value[i])

        
            


def init_library_DB():
    for section in Library_books:
        calc_maxlength(section, section.values())

    pass

init_library_DB()