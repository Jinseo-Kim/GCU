#include <stdio.h>
#include <stdlib.h>

typedef struct node* listPointer;

typedef struct node {
    int data;
    listPointer link;
} node;

// 노드 생성
listPointer createNode(int data) {
    listPointer newNode = (listPointer)malloc(sizeof(node));
    if (!newNode) {
        printf("Memory allocation failed.\n");
        exit(1);
    }
    newNode->data = data;
    newNode->link = NULL;
    return newNode;
}

// 맨 앞 삽입
listPointer insertFront(listPointer head, int data) {
    listPointer newNode = createNode(data);
    newNode->link = head;
    return newNode;
}

// 특정 노드 뒤에 삽입
void insert(listPointer prev, int data) {
    if (prev == NULL) {
        printf("Previous node cannot be NULL.\n");
        return;
    }

    listPointer newNode = createNode(data);
    newNode->link = prev->link;
    prev->link = newNode;
}

// 리스트 출력
void printList(listPointer head) {
    listPointer temp = head;
    printf("List: ");
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->link;
    }
    printf("NULL\n");
}

// 노드 삭제
listPointer deleteNode(listPointer head, int key) {
    listPointer temp = head;
    listPointer prev = NULL;

    if (temp != NULL && temp->data == key) {
        head = temp->link;
        free(temp);
        return head;
    }

    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->link;
    }

    if (temp == NULL) return head;

    prev->link = temp->link;
    free(temp);
    return head;
}

// 리스트 메모리 해제
void freeList(listPointer head) {
    listPointer temp;
    while (head != NULL) {
        temp = head;
        head = head->link;
        free(temp);
    }
}

int main() {
    listPointer head = NULL;

    head = insertFront(head, 30);
    head = insertFront(head, 20);
    head = insertFront(head, 10);
    // 현재 리스트: 10 -> 20 -> 30 -> NULL

    printList(head);

    // head->link는 20을 가리킴, 그 뒤에 25 삽입
    insert(head->link, 25);  // 20 뒤에 25 삽입
    printList(head);         // 출력: 10 -> 20 -> 25 -> 30 -> NULL

    head = deleteNode(head, 25);
    printList(head);         // 출력: 10 -> 20 -> 30 -> NULL

    freeList(head);
    return 0;
}
