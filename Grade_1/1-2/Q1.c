#include <stdio.h>

int main()
{
    printf("202533713 김진서\n");

    int N, M;
    int i, j, result = 0;
    int cnt = 0;

    printf("N: ");
    scanf("%d", &N);

    while (N >= 1 && N <= 4)
    {
        printf("M: ");
        scanf("%d", &M);

        if (M % 2 == 0) // M = 짝수일 때
        {
            printf("M은 홀수여야합니다.\n다시 입력해주세요.");
            continue;
        }

        if (N == 1)
        {
            for (i = 0; i < M; i++)
            {
                for (j = 0; j < M - i; j++)
                {
                    printf("  ");
                }
                for (j = 0; j <= i; j++)
                {
                    result++;
                    printf("%-3d ", result);
                }
                printf("\n");
            }
            break;
        }

        if (N == 2)
        {
            for (i = 0; i < M; i++)
            {
                for (j = 0; j < i; j++)
                {
                    printf("  ");
                }
                for (j = 0; j < M - i; j++)
                {
                    result++;
                    printf("%-3d ", result);
                }
                printf("\n");
            }
            break;
        }

        if (N == 3)
        {
            for (i = 0; i < M; i++)
            {
                if ((M / 2) > i)
                {
                    for (j = 0; j < M - i; j++)
                    {
                        printf("  ");
                    }
                    for (j = 0; j <= i; j++)
                    {
                        result++;
                        printf("%-3d ", result);
                    }
                }
                else
                {
                    for (j = 0; j < i + 1; j++)
                    {
                        printf("  ");
                    }
                    for (j = 0; j < M - i; j++)
                    {
                        result++;
                        printf("%-3d ", result);
                    }
                }
                printf("\n");
            }
            break;
        }

        if (N == 4)
        {
            for (i = 0; i < M; i++)
            {
                if ((M / 2) > i)
                {
                    for (j = 0; j < i; j++)
                    {
                        printf("  ");
                    }
                    for (j = 0; j < (M / 2) + 1 - i; j++)
                    {
                        result++;
                        printf("%-3d ", result);
                    }
                }
                else
                {
                    for (j = 0; j < M - (i + 1); j++)
                    {
                        printf("  ");
                    }
                    for (j = 0; j <= i - (M / 2); j++)
                    {
                        result++;
                        printf("%-3d ", result);
                    }
                }
                printf("\n");
            }
            break;
        }
    }
}
