#include <stdio.h>

int main () {
    int i, end;
    int arr[100];
    
    for (i = 0; i < 100; i++)
    {
        scanf("%d", &arr[i]);

        if (arr[i] == 0){
            end = i - 1;
            break;
        }
    }

    for (i = 0; i <= end; i++)
        printf("%d ", arr[end - i]);

    printf("\n");
}