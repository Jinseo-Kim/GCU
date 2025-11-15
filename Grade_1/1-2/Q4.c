#include <stdio.h>

int main () 
{
    printf("202533713 김진서\n");

    int divide = 1;
    double pi = 0;
    
    // 최대 10억 회의 연산 = (5천만회) * 2
    for (int i = 1; i <= 500000000; i++)
        {
            if (i == 5000)
                printf("10000회: %.10f\n", 4.0 * pi);

            if (i == 500000)
                printf("1000000회: %.10f\n", 4.0 * pi);

            if (i == 50000000)
                printf("100000000회: %.10f\n", 4.0 * pi);
                
            if (i == 500000000)
                printf("1000000000회: %.10f\n", 4.0 * pi);

            /// 아래 과정을 1회의 cycle로 진행해 5000만번의 연산만 진행
            // 홀수로 더하기
            pi += 1.0 / divide;
            divide += 2;
            
            // 홀수로 빼기
            pi -= 1.0 / divide;
            divide += 2;
        }

}

