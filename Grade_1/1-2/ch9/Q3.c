#include <stdio.h>

int main() {
    int i;
    char seat[9] = {'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X'};
    char reserv[2];

    for (i = 0; i < 2; i++)
        scanf("%hhd", &reserv[i]);

    if (reserv[1] > 0){
        for (i = 0; i < reserv[1]; i++)
            seat[reserv[0] + i - 1] = 'O';
    }
    else
    {
        for (i = 0; i > reserv[1]; i--)
            seat[reserv[0] - i - 1] = 'X';
    }
    

    printf("[");

    for (i = 0; i < 9; i++)
        printf("%c", seat[i]);

    printf("]\n");
}