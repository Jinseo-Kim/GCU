// Q2 유효 년도
# include <stdio.h>

int is_valid(int, int, int);

int is_valid(int year, int month, int day) {
    char days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    if (year == 0)
        return 0;
    if (month < 1 && month > 12)
        return 0;
    if (day < 1 || day > days[month - 1])
        return 0;
    else
        return 1;
}

int main() {
    int year, month, day;

    // printf("년, 월, 일: ");
    // scanf("%d %d %d", &year, &month, &day);

    if(is_valid(2023, 2, 29))
        printf("valid\n");
    else
        printf("invalid\n");
}