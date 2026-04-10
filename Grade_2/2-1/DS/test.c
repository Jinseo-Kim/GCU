#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

short* combine_str(char* c_mem1, char* c_mem2, short* start1, short* end1, short* start2, short* end2) {
    
}

int assign_mem(char* amem) {
    int cnt = 0;
    char input_max_size = 50;
    char *end;
    char *arr = (char *)malloc(input_max_size * sizeof(char));
    char* token;

    // 입력받고 동적할당 size를 계속 변경
    while (fgets(arr + (cnt * input_max_size), input_max_size, stdin) != NULL) {
        end = strchr(arr, '\n');
        if (end != NULL) {
            *end = '\0';
            break;
        }

        arr = (char *)realloc(arr, input_max_size + (input_max_size * cnt));
        cnt += 1;
    }

    arr = (char *)realloc(arr, strlen(arr)); // 문자열 길이 + 2(\n\0)
    int* slice_arr = (int*)malloc(strlen(arr) * 4);
    int slice_cnt = 0;

    token = strtok(arr, " ");
    while(token != NULL){
        slice_arr[slice_cnt] = atoi(token);
        token = strtok(NULL, " ");
        slice_cnt += 1;
    }

    slice_arr = (int*)realloc(slice_arr, sizeof(int) * cnt);
    amem = slice_arr;
    return slice_cnt;

}

short* slice_str(char* s_mem) {
    char* token;

    token = strtok(s_mem, ' ');

    while(token != NULL) {

    }
}

int main () {
    char* mem1;
    char* mem2;
    short start1, end1;
    short start2, end2;

    printf("수식 1을 입력하세요 : ");
    start1 = 0;
    end1 = assign_mem(mem1);

    printf("수식 2를 입력하세요 : ");
    start2 = end1 + 1;
    end2 = start2 + assign_mem(mem2);

    combine_str(mem1, mem2, start_mem1, end_mem1, start_mem2, end_mem2);

}
