/*
 * rhkwp3.c - 연결 리스트 사전 (이중 연결리스트)
 *
 * 노드 구성:
 *   word     - 사전 단어 (문자열)
 *   meaning  - 단어의 뜻 (문자열)
 *   intword  - 단어를 대문자 ASCII로 변환한 char 배열 (삽입 위치 비교용)
 *   num      - 알파벳 순 몇 번째 노드인지 (전체 로딩 후 부여)
 *   prev     - 이전 노드 포인터
 *   next     - 다음 노드 포인터
 *
 * 연결리스트 선택 이유:
 *   이중 연결리스트를 선택. 단어 삽입 시 이전/다음 노드에 모두 접근해야
 *   정렬된 위치에 노드를 연결할 수 있기 때문.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORD  100
#define MAX_MEAN  200

typedef struct Node {
    char  word[MAX_WORD];
    char  meaning[MAX_MEAN];
    char  intword[MAX_WORD];  /* 대문자 ASCII 변환값 배열 (char형) */
    int   num;
    struct Node *prev;
    struct Node *next;
} Node;

static Node *head  = NULL;
static Node *tail  = NULL;
static int   total = 0;

/* 단어를 대문자 ASCII 배열로 변환 */
static void chg_intword(char *src, char *dst) {
    int i;
    for (i = 0; src[i] != '\0' && i < MAX_WORD - 1; i++)
        dst[i] = (char)toupper((unsigned char)src[i]);
    dst[i] = '\0';
}

static Node *create_node(char *word, char *mean) {
    Node *node = (Node *)malloc(sizeof(Node));

    if (node == NULL) { 
        printf("메모리 할당 실패"); 
        return 0; 
    }

    strncpy(node->word, word, MAX_WORD - 1); node->word[MAX_WORD - 1] = '\0';
    strncpy(node->meaning, mean, MAX_MEAN - 1); node->meaning[MAX_MEAN - 1] = '\0';
    chg_intword(word, node->intword);

    node->num  = 0;
    node->prev = node->next = NULL;
    return node;
}

/* intword를 기준으로 알파벳 순 정렬 삽입 */
static void insert_sorted(Node *node) {
    Node *curr = head;

    /* 삽입 위치 탐색: node->intword 보다 큰 첫 번째 노드 앞에 삽입 */
    while (curr && strcmp(node->intword, curr->intword) > 0)
        curr = curr->next;

    if (curr == NULL) {
        /* 리스트가 비어있거나 맨 뒤에 삽입 */
        if (tail == NULL) {
            head = tail = node;
        } 
        else {
            node->prev  = tail;
            tail->next  = node;
            tail = node;
        }
    }
    else {
        /* curr 바로 앞에 삽입 */
        node->next  = curr;
        node->prev  = curr->prev;

        if (curr->prev) 
            curr->prev->next = node;
        else 
            head = node;

        curr->prev  = node;
    }
    total++;
}

/* 전체 로딩 후 head부터 순회하며 번호 부여 */
static void assign_numbers(void) {
    int  idx_n = 1;
    Node *curr = head;
    while (curr) {
        curr->num = idx_n++;
        curr = curr->next;
    }
}

/* intword 기준 순차 탐색 (정렬되어 있으므로 초과 시 조기 종료) */
static Node *search(char *word) {
    char iw[MAX_WORD];
    chg_intword(word, iw);

    Node *curr = head;
    while (curr) {
        int cmp = strcmp(iw, curr->intword);
        if (cmp == 0) 
            return curr;
        if (cmp <  0)
            return NULL;
        curr = curr->next;
    }
    return NULL;
}

static void free_list(void) {
    Node *curr = head;
    while (curr) {
        Node *next = curr->next;
        free(curr);
        curr = next;
    }
    head = tail = NULL;
}

int main(void) {
    FILE *fp = fopen("randdict_utf8.TXT", "r");

    if (fp == NULL) {
        fprintf(stderr, "파일 열기 실패\n");
        return 1;
    }

    char line[MAX_WORD + MAX_MEAN];
    printf("사전 로딩 중...\n");

    while (fgets(line, sizeof(line), fp)) {
        /* 줄 끝 개행 제거 */
        int len = (int)strlen(line);
        while (len > 0 && line[len-1] == '\n'){
            len -= 1;
            line[len] = '\0';
        }

        /* ':' 기준으로 단어/뜻 분리 (첫 번째 ':' 사용) */
        char *split = strchr(line, ':');
        *split = '\0';

        char *word = line;
        char *mean = split + 1; 

        /* 단어 뒤쪽 공백 제거 */
        int wlen = (int)strlen(word);
        while (wlen > 0 && word[wlen-1] == ' ')
            wlen -= 1;
            word[wlen] = '\0';

        /* 뜻 앞쪽 공백 제거 */
        while (*mean == ' ')
            mean += 1;

        insert_sorted(create_node(word, mean));
    }
    fclose(fp);

    assign_numbers();
    printf("총 %d개 단어 로딩 완료.\n\n", total);
    printf("단어를 입력하세요 (종료: quit)\n");

    char input[MAX_WORD];
    while (1) {
        printf(">> ");
        if (fgets(input, sizeof(input), stdin) == NULL)
            break;
        int ilen = (int)strlen(input);

        while (ilen > 0 && (input[ilen-1] == '\n' || input[ilen-1] == '\r'))
            input[--ilen] = '\0';

        if (!strcmp(input, "quit") || !strcmp(input, "exit")) 
            break;
        if (!*input) 
            continue;

        Node *r = search(input);

        if (r) 
            printf("(%d) %s\n", r->num, r->meaning);
        else
            printf("'%s'를 찾을 수 없습니다.\n", input);
    }

    free_list();
    return 0;
}
