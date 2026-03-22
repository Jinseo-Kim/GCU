#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void make_ladder(char arr[][5])
{
    char cnt = 0;
    int attempts = 0;  // 최대 시도 횟수 변수 추가
    char height; 
    char ladder_head, ladder_tail;

    while(cnt < 20)
    { 
        attempts += 1;
        height = rand() % 14;      // 높이 15 = idx range 0 ~ 14
        ladder_head = rand() % 3 + 1; // 사다리는 user A B C D E에서 생성되며, 최종적으로 B C D에서 각각 양 옆으로 연결되는 구조로 나옴.
        ladder_tail = rand() % 2;  // 0 또는 1 출력

        if (arr[height][ladder_head] >= 1)
        {
            continue;
            printf("%d번째 시도 / cnt = %d\n", attempts, cnt);

        }
        else if (arr[height][ladder_head + 1] >= 1 || arr[height][ladder_head - 1] >= 1)
        {
            continue;
            printf("%d번째 시도 / cnt = %d\n", attempts, cnt);

        }

        if (ladder_tail == 0)
        {
            arr[height][ladder_head] = 1;
            arr[height][ladder_head - 1] = 2;
            cnt += 1;
        }
        else
        {
            arr[height][ladder_head] = 1;
            arr[height][ladder_head + 1] = 2;
            cnt += 1;
        }
    }
}

void print_ladder()
{
    
}

int run_ladder()
{
    
}

int main()
{
    srand(time(NULL));
    char arr[15][5] = {0};

    make_ladder(arr);
    
    for (int i = 0; i < 15; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            printf("%d ", arr[i][j]);
        }
        if (i % 5 == 4)
            printf("\n");
        printf("\n");
    }
    
    return 0;
}