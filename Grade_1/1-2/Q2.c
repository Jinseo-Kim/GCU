#include <stdio.h>

int main () {
    printf("202533713 김진서\n");

    int N, M, dan;
    int i, j, k;
    int minSpace, avgSpace;
    char space = 32;

    printf("N: ");
    scanf("%d", &N);
    printf("M: ");
    scanf("%d", &M);

    dan = M - N + 1;
    minSpace = 80 - (dan * 10) + dan + 1;
    avgSpace = (80 - (dan * 10)) / (dan + 1);

    for (j = 1; j <= 9; j++)
    {
        for (i = 0; N + i <= M; i++)
        {   
            for (k = 0; k < avgSpace; k++)
                printf("%c", space);

            printf("%d x %d = %d", N + i, j, (N + i) * j);
        }

        for (k = 0; k < avgSpace; k++)
            printf("%c", space);

        printf("\n");
    }
}