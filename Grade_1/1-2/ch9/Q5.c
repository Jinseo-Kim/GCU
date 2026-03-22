#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void sort(int, int[]);

int main () {
    srand(time(NULL));

    int arr[20];
    int n = 10;

    printf("before: ");
    for (int i = 0; i < 10; i++){
        arr[i] = rand() % 100;
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    sort(n, arr);
}


void sort(int n, int arr[]){
    printf("after: ");

    int start, p;
    int temp;

    for (start = 0; start < n; start++){
        for (p = start + 1; p < n; p++){
            if (arr[start] > arr[p]){
                temp = arr[start];
                arr[start] = arr[p];
                arr[p] = temp;
            }
        }
        printf("%d ", arr[start]);
    }
    printf("\n");
    
}

