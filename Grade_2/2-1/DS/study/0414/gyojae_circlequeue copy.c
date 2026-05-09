#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#define MAX_QUEUE_SIZE 101

typedef struct {
    int *queue;
    int front;
    int rear;
    int max;
    char flag;
} Queue;


char cnt;

int is_empty(Queue *q) {
    return (q->front == q->rear && q->flag == 0);
}

int is_full2(Queue *q) {
    // 방법 2번
    return ((q->rear + 1) % q->max == q->front);
}

int is_full1(Queue *q) {
    if (q->front == q->rear && q->flag == 1){
        return true;
    }
    return false;
}

void enqueue(Queue *q, int item) {
    if (is_full1(q) == true){
        printf("큐가 포화상태입니다.");
        exit(1);
    }
    q->rear = (q->rear + 1) % q->max;
    q->queue[q->rear] = item;
    q->flag = 1;
    cnt += 1;
}

int get_count (Queue *q){
    if (is_full1(q) == true){
        return q->max;
    }
    return q->rear - q->front;
}

int dequeue(Queue *q) {
    if (is_empty(q) == true){
        printf("큐가 공백상태입니다.");
        exit(1);
    }
    q->front = (q->front + 1) % q->max;
    if (q->front == q->rear)
        q->flag = 0;
    cnt -= 1;
    return q->queue[q->front];
}

Queue *init () {
    Queue *q = malloc(sizeof(Queue));
    q->max = 10;
    q->queue = malloc(sizeof(int) * q->max);
    q->front = 0;
    q->rear = 0;
    q->flag = 0;

    cnt = 0;
    return q;
}

void print_queue(Queue *q) {
    for (int i = 0; i < cnt; i++){
        int idx = (q->front + 1 + i) % q->max;
        printf("[%d]: %d\n", idx, q->queue[idx]);
    }
}

int main () {
    Queue *q = init();

    for (int i = 1; i <= 15; i+=2)
        enqueue(q, i);

    print_queue(q);
    printf("count: %d", get_count(q));

        
    // print_queue(q);

}