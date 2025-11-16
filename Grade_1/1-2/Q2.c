#include <stdio.h>

int main () {
    printf("202533713 김진서\n");

    int N, M, dan;
    int i, j, k;
    int avgSpace;
    char space = 32;

    printf("N: ");
    scanf("%d", &N);
    printf("M: ");
    scanf("%d", &M);

    dan = M - N + 1; // 출력할 단 수 (ex. 2 ~ 5단 = 4개)
    avgSpace = (80 - (dan * 10)) / (dan + 1); // 공백 칸 수의 평균값 = 총 행(80) - (출력할 단 수 * 10) / ((출력할 단 수 = 각 단의 뒤에 들어갈 공백) + (맨 앞에 들어갈 공백 = 1)) 

    for (j = 1; j <= 9; j++)
    {
        for (i = 0; N + i <= M; i++)
        {   
            for (k = 0; k < avgSpace; k++)
                printf("%c", space);

            printf("%d x %d = %2d", N + i, j, (N + i) * j);
        }
        
        printf("\n");
    }
}