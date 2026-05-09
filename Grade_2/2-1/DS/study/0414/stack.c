#define MAX_SIZE_STACK 100
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int stackArr[MAX_SIZE_STACK];
    int top;
} stack;

stack *create(void) {
    stack *tempstack;

    tempstack = malloc(sizeof(stack));
    tempstack->top = -1;
    return tempstack;
}

bool isEmpty(stack *pstack){
    if (pstack->top == -1)
        return true;
}

bool isFull(stack *pstack){
    if (pstack->top == MAX_SIZE_STACK-1)
        return true;
    else
        return false;
}

void push(stack *pstack, int data){
    pstack->stackArr[++pstack->top] = data;
}

int pop(stack *pstack){
    if (isEmpty(pstack) == true){
        printf("stack is Empty\n");
        return false;
    }
    return pstack->stackArr[pstack->top--];
}

int main() {
    stack *pstack;
    int a;

    pstack = create();
    push(pstack, 1);
    a = pop(pstack);
    printf("%d\n", a);
    return 0;
}

//19:26