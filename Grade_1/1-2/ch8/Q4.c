// Q4 날짜 카운터
#include <stdio.h>

short getDate(int, int, int);

short getDate(int year, int month, int day)
{
    char days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int result = day - 1;

    for (int i = 0; i < month - 1; i++)
        result += days[i];

    return result;
}

int main() {
    int year, month, day;
    printf("오늘의 날짜를 년, 월, 일 순으로입력하세요.");
    scanf("%d %d %d", &year, &month, &day);  
    printf("%d년 1월1일 이후로 오늘은 %d일 지났습니다.\n", year, getDate(year, month, day));
}