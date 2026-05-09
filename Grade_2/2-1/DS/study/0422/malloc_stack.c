#include <stdio.h>
#include <stdlib.h>

typedef struct Stack {
    int *arr;
    int top;
    int size;
} stack;

stack * init(){
    stack *st = malloc(sizeof(stack));
    st->size = 0;
    st->top = -1;
    st->arr = malloc(sizeof(int) * st->size);
}

void insert (stack *st, int i){
    if (st->top == st->size - 1){
        st->size += 10;
        st->arr = realloc(st->arr, sizeof(int) * st->size);
    }
    st->arr[++st->top] = i;
}

void pop (stack *st) {
    if (st->top < 0)
        return;
    st->top -=1;

    if (st->top == -1 && st->size - 10 >= 9)
        st->size -= 10;
        st->arr = realloc(st->arr, sizeof(int) * st->size);
}

int main() {
    stack *st = init();

    for (int i = 0; i < 10; i++)
        insert(st, i);
    
    free(st->arr);
    free(st);
    return 0;
}