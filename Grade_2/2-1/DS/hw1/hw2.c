#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned char* load_maze()
{
    FILE* fp;                        // 구조체 FILE의 포인터(파일 읽기 및 저장을 위함)
    unsigned char x, y;              // x = 가로, y = 세로
    unsigned short length;          // length = Full array length (x * y)
    unsigned short cnt;         // cnt = 총 반복 횟수(x * y번)
    unsigned char move_pointer;      // move_pointer = 4개씩 비트 연산 후 +1하여 다음 인덱스 이동 (max = 255(x * 255))
    unsigned char value;             // 매핑한 문자에 맞는 값을 full_array에 저장 


    char file_name[100];
    printf("input filename? ");
    scanf("%s", file_name);

    fp = fopen(file_name, "r");         // 텍스트 읽기 (소스코드랑 같이 있는 폴더에 파일이 있어야 함)

    if (fp == NULL)
    {
        printf("fail to open");
        return 0;
    }

    fscanf(fp, "%hhd %hhd ", &x, &y);

    length = (x * y) / 4 + 1;           // 미로 전체 문자를 1바이트 당 4개의 문자를 저장하여 1/4로 미로 압축                                     
    unsigned char* full_array = (unsigned char*)malloc(length * sizeof(unsigned char) + 2);         // length에 맞는 1바이트 단위 공간 + 2바이트(x: [0], y: [1]) 공간 동적 메모리 할당
    char* read_line = (char*)malloc((x + 2) * sizeof(char));            // '길이 x만큼의 문자 + \0 + \n' 크기의 1바이트 단위 동적 메모리 할당

    memset(full_array, 0, length * sizeof(unsigned char) + 2);       // 연산 결과를 저장할 full_aaray 내 모든 값을 0으로 초기화

    full_array[0] = x;
    full_array[1] = y;
    
    cnt = 0;
    move_pointer = 0;

    // (space): 32 = 1, +: 43 = 2, -: 45 = 3, |: 124 = 4
    while (fgets(read_line, x + 2, fp) != NULL)
    {   
        for (int i = 0 ; i < x; i++)
        {
            if (read_line[i] == ' ')
                value = 0;
            else if (read_line[i] == '+')
                value = 1;
            else if (read_line[i] == '-')
                value = 2;
            else if (read_line[i] == '|')
                value = 3;
            else
            {
                printf("미로 형식에 맞지 않는 문자가 존재합니다. \n");
                printf("프로그램 종료");
                fclose(fp);
                return 0;
            }

            move_pointer = (cnt / 4) + 2;
            full_array[move_pointer] |= value << (6 - (cnt % 4) * 2);

            cnt += 1;
        }
    }

    free(read_line);        // 읽기가 모두 끝난 동적 메모리 할당 해제
    // printf("end of line");
    fclose(fp);
    return full_array;
} 

void draw_maze(unsigned char* full_array)
{
    const char start_point = 2;           // 0번째 인덱스: x, 1번째 인덱스: y, 2번째 인덱스 ~ n번째 인덱스: 압축된 미로의 연산값
    unsigned char value;            // 언패킹한 값 (0 ~ 3)
    unsigned short cnt;            // 총 반복 횟수(x * y번)
    unsigned char move_point;           // move_point = 4개씩 비트 언패킹 후 +1하여 다음 인덱스 이동 (x = max = 255)
    unsigned char x = full_array[0], y = full_array[1];

    cnt = 0;

    while (x * y > cnt)
    {
        move_point = (cnt / 4);         // 4개씩 비트 언패킹 끝나면 +1하여 다음 인덱스 이동
        value = full_array[move_point + start_point] & (0b11000000 >> (cnt % 4) * 2);           // 앞에서부터 2비트씩 비트 연산(&)하여 해당 자리의 값만 살리기
        value >>= 6 - (cnt % 4) * 2;            // 살린 값을 하위비트로 내려서 0 ~ 3으로 매핑할 수 있게 만들기

        if (value == 0)
            printf(" ");
        else if (value == 1)
            printf("+");
        else if (value == 2)
            printf("-");
        else 
            printf("|");
        
        if ((cnt + 1) % x == 0)
            printf("\n");

        cnt += 1;
    }
}

int main() {
    unsigned char* array = load_maze();
    printf("dim: %d*%d\n", array[0], array[1]);
    printf("number: %d\n", (array[0] * array[1] / 4 + 1 + 2));
    draw_maze(array);
}