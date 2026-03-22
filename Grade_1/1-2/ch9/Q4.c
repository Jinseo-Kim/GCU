#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main () {
    srand(time(NULL));

    int cnt = 0, state;
    int value;

    char arr[10] = {0};

    while (cnt < 10) {
        state = 0;
        value = rand() % 20 + 1;

        for (int i = 0; i < cnt; i++)
            if (value == arr[i]){
                state = 1;
                break;
            }
                
        if (state == 1)
            continue;

        printf("%d ", value);
        arr[cnt] = value;
        cnt++;
    }
    printf("\n");
}