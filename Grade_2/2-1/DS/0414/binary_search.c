#include <stdio.h>
#define FAIL -1

int binary_search(int arr[], int first, int len, int find_num){
    int mid;
    int last = len - 1;

    while (first <= last) {
        mid = (first + last) / 2;
        printf("first: %d, end: %d, mid: %d\n", first, last, mid);

        if (find_num == arr[mid])
            return mid;
        else if (find_num > arr[mid])
            first = mid + 1;
        else
            last = mid - 1;
    }

    return FAIL;
}

int main () {
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int num;
    int first = 0;
    int len = sizeof(arr) / sizeof(int) ;

    printf("숫자 입력: ");
    scanf("%d", &num);

    printf("%d\n", binary_search(arr, first, len, num));
}