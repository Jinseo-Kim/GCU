#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main ()
{
    char max, min;
    char arr[10] = {0};

    srand(time(NULL));

    for (int i = 0; i < 10; i++)
    {

        arr[i] = rand() % 100;
        printf("%d ", arr[i]);

        if (i == 0)
        {
            max = arr[i];
            min = arr[i];
            continue;
        }

        if (max < arr[i])
            max = arr[i];

        if (min > arr[i])
            min = arr[i];
        
    }
    printf("\n");
    printf("max %d min %d\n", max, min);
}