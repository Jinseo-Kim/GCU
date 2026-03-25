#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void make_ladder(char arr[][5])
{
    /// ~ 0323
    // int try = 0;
    char cnt = 0, size = 60;
    char rand_idx, value;
    char col, row;
    char swap;
    char mapping_ladder[60];
    
    // 0: 0 -> 1 사다리, 1: 1 -> 2 사다리, 2: 2 -> 3 사다리, ... 58: 58 -> 59 사다리
    for (int i = 0; i < 60; i++)
        mapping_ladder[i] = i;
        
    // arr[value]개, 난수 = rand() % value, value = 60 - cnt, i = 0(i++)
    while(cnt < 20)
    {
        // for (int i = 0; i < 15; i++)
        // {
        //     for (int j = 0; j < 5; j++)
        //     {
        //         printf("%d ", arr[i][j]);
        //     }
        //     if (i % 5 == 4)
        //         printf("\n");
        //     printf("\n");
        // }
        rand_idx = rand() % (size);
        value = mapping_ladder[rand_idx];

        col = value / 4;
        row = value % 4;

        arr[col][row] = 1;
        arr[col][row + 1] = 2;

        size -= 1;
        cnt += 1;

        // 뽑은 random값과 맨 뒤의 값을 swap
        swap = value;
        mapping_ladder[rand_idx] = mapping_ladder[size];
        mapping_ladder[size] = swap;

        // 같은 높이에 사다리가 중복되어서 설치되지 않도록 random값+-1의 사다리도 mapping_ladder에서 제거
        for (int i = 0; i < size; i++)
        {
            if (row != 0 && value - mapping_ladder[i] == 1)
            {
                size -= 1;
                swap = mapping_ladder[i];
                mapping_ladder[i] = mapping_ladder[size];
                mapping_ladder[size] = swap;
                i -= 1;
            }

            if (mapping_ladder[i] - value == 1)
            {
                size -= 1;
                swap = mapping_ladder[i];
                mapping_ladder[i] = mapping_ladder[size];
                mapping_ladder[size] = swap;
                i -= 1;
            }
        } // 

        /// ~ 0323 = 간헐적으로 무한 루프에 빠지거나 무한 루프에 빠지며 cpu에 부하가 걸려 프로그램이 종료됨.
        // if (try > 1000) // 초기화
        // {
        //     for (int i = 0; i < 15; i++)
        //     {
        //         for (int j = 0; j < 5; j++)
        //         arr[i][j] = 0;
        //     }

        //     try = 0;
        //     cnt = 0;
        // }
            
        // height = rand() % 15;      // 높이 15 = idx range 0 ~ 14
        // ladder_head = rand() % 4; // 사다리는 user A B C D E에서 생성되며, 최종적으로 B C D에서 각각 양 옆으로 연결되는 구조로 나옴.

        // if (arr[height][ladder_head] == 0)
        // {
        //     if (arr[height][ladder_head + 1] == 0)
        //     {
        //         arr[height][ladder_head] = 1;
        //         arr[height][ladder_head + 1] = 2;
        //         cnt += 1;
        //     }
        // }
    }
}

void print_ladder(char arr[][5])
{
    for (int k = 1; k <= 5; k++)
    {
        printf("%d", k);
        
        if (k == 5)
            printf("\n");
        else
            printf("     ");
    }

    for (int i = 0; i < 15; i++)
    {
        for (int j = 0; j < 5; j++)
            {
                printf("|");
                if (arr[i][j] == 0 || arr[i][j] == 2)
                    printf("     ");
                else if (arr[i][j] == 1)
                    printf("-----");
            }
        printf("\n");
    }

    for (int k = 0; k < 5; k++)
    {
        printf("%c", 65 + k);

        if (k == 4)
            printf("\n");
        else
            printf("     ");
    }
}

void run_ladder(char arr[][5])
{
    char result[5] = {0};

    for (int i = 0; i < 15; i++)
        for (int j = 0; j < 5; j++)
            {
                if (arr[i][j] == 0)
                else if (arr[i][j] == 1)
                else if (arr[i][j] == 2)
            }
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
    print_ladder(arr);
    run_ladder(arr);
    
    return 0;
}