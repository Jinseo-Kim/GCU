#include <stdio.h>
#include <stdbool.h>
#define MAX_QUEUE_SIZE 101

typedef struct {
    int queue[MAX_QUEUE_SIZE];
    int front;
    int rear;
    char flag;
} Queue;


char cnt;

int is_empty(Queue *q) {
    return (q->front == q->rear && q->flag == 0);
}

int is_full2(Queue *q) {
    // 방법 2번
    return ((q->rear + 1) % MAX_QUEUE_SIZE == q->front);
}

int is_full1(Queue *q) {
    if (q->front == q->rear && q->flag == 1){
        return true;
    }
    return false
}

void enqueue(Queue *q, int item) {
    if (is_full1(q) == true)
        error("큐가 포화상태입니다.");
    q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
    q->queue[q->rear] = item;
    q->flag = 1;
    cnt += 1;
}

int dequeue(Queue *q) {
    if (is_empty(q) == true)
        error("큐가 공백상태입니다.");
    q->front = (q->front + 1) % MAX_QUEUE_SIZE;

    q->flag = 0;
    cnt -= 1;
    return q->queue[q->front];
}

Queue *init (Queue *reset) {
    reset->queue[MAX_QUEUE_SIZE] = {0};
    reset->front = -1;
    reset->rear = -1;
    reset->flag = 0;

    cnt = 0;
    return reset;
}

void print_queue(Queue *q) {
    for (int i = 0; i < cnt; i++){
        printf("front[%d]: %d, rear[%d]: %d, length: %d\n", 
            q->front + i, q->queue[q->front + i], q->rear + i, q->queue[q->rear + i], cnt);
    }
}

int main () {
    Queue *q;

    init(q);
    for (int i = 1; i <= 15; i+=2)
        enqueue(q, i);
        
    print_queue(q);

}