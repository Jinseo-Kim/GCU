#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void make_ladder(char arr[][5])
{
    char cnt = 0;
    int try = 0;
    char height; 
    char ladder_head;

    while(cnt < 20)
    {
        if (try > 1000) // 초기화
        {
            for (int i = 0; i < 15; i++)
            {
                for (int j = 0; j < 5; j++)
                arr[i][j] = 0;
            }

            try = 0;
            cnt = 0;
        }
            
        height = rand() % 15;      // 높이 15 = idx range 0 ~ 14
        ladder_head = rand() % 4; // 사다리는 user A B C D E에서 생성되며, 최종적으로 B C D에서 각각 양 옆으로 연결되는 구조로 나옴.

        if (arr[height][ladder_head] == 0)
        {
            if (arr[height][ladder_head + 1] == 0)
            {
                arr[height][ladder_head] = 1;
                arr[height][ladder_head + 1] = 2;
                cnt += 1;
            }
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