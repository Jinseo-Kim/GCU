#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main () {
    srand(time(NULL));

    int com;

    for (int i = 0; i < 100; i++)
    {
        com = rand();
        printf("%d\n", com);
    }
}
   