#include <stdio.h>

int main () {
    int number[3] = {1, 2, 3};
    int(*arrptr)[3] = &number;

    printf("%d", (*arrptr)[1]);
}