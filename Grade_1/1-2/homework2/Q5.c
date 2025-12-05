#include <stdio.h>

int main () 
{
    printf("202533713 김진서\n");
    
    int money;
    int ocheon = 0, cheon = 0, obaek = 0, baek = 0, osip = 0, sip = 0;

    printf("잔돈은? ");
    scanf("%d", &money);

    // 모든 if문을 타며 유효한 값을 가지는 경우, 변수에 저장
    if (money / 5000 != 0)
    {
        ocheon += (money / 5000);
        money %= 5000;
        printf("5천원권 : %d매\n", ocheon);
    }

    if (money / 1000 != 0)
    {
        cheon += (money / 1000);
        money %= 1000;
        printf("1천원권 : %d매\n", cheon);
    }

    if (money / 500 != 0)
    {
        cheon += (money / 500);
        money %= 500;
        printf("500원권 : %d매\n", obaek);
    }

    if (money / 100 != 0)
    {
        baek += (money / 100);
        money %= 100;
        printf("100원권 : %d매\n", baek);
    }

    if (money / 50 != 0)
    {
        osip += (money / 50);
        money %= 50;
        printf("50원권 : %d매\n", osip);
    }

    if (money / 10 != 0)
    {
        sip += (money / 10);
        money %= 10;
        printf("10원권 : %d매\n", sip);
    }
    
}