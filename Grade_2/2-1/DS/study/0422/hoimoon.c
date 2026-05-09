#include <stdio.h>
#include <string.h>

int main (){
    char arr[100];
    char stack[100];
    int top = -1;
    scanf("%s", arr);

    int length = strlen(arr);
    int mid = length / 2;

    for (int i = 0; i < length; i++){
        if (i < mid){
            top += 1;
            stack[top] = arr[i];
        }
        else if (i == mid && length % 2 == 1) {
            continue;
        }
        else {
            if (stack[top] == arr[i])
                top -= 1;
            else
                printf("두 문자가 다릅니다. %c %c", stack[top], arr[i]);
                break;
        }
    }
}

