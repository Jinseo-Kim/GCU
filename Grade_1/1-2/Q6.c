#include <stdio.h>

int main ()
{
    printf("202533713 김진서\n");
    
    int select;
    int call, message, data;
    int payments = 0;

    printf("원하는 음성통화 사용량(분)은? ");
    scanf("%d", &call);
    printf("원하는 문자메시지 사용량(건)은? ");
    scanf("%d", &message);
    printf("원하는 데이터 사용량(MB)은? ");
    scanf("%d", &data);

    printf("원하는 요금제는? ");
    scanf("%d", &select);

    if (select == 1)
    {
        payments = 3300;

        if (50 < call)
            payments += (int)((call - 50) * 60 * 1.98 + 0.5); // 반올림을 위한 0.5 덧셈 후 명시적 형변환
        
        if (50 < message)
            payments += (message - 50) * 22;

        if (1800 < data)
            payments += (int)((data - 1800) * 22.53 + 0.5); // 반올림을 위한 0.5 덧셈 후 명시적 형변환
    }

    else if (select == 2)
    {
        payments = 5500;

        if (100 < call)
            payments += (int)((call - 100) * 60 * 1.98 + 0.5); // 반올림을 위한 0.5 덧셈 후 명시적 형변환
        
        if (100 < message)
            payments += (message - 100) * 22;

        if (2000 < data)
            payments += (int)((data - 2000) * 22.53 + 0.5); // 반올림을 위한 0.5 덧셈 후 명시적 형변환
    }

    else if (select == 3)
    {
        payments = 5500;

        if (100 < call)
            payments += (int)((call - 100) * 60 * 1.98 + 0.5); // 반올림을 위한 0.5 덧셈 후 명시적 형변환
        
        if (100 < message)
            payments += (message - 100) * 22;

        if (1000 < data)
            payments += (int)((data - 1000) * 22.53 + 0.5); // 반올림을 위한 0.5 덧셈 후 명시적 형변환
    }

    printf("예상 요금은 %d원 입니다.\n", payments);

}