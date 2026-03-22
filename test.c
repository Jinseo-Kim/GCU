#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// int main () {
//     // char name[] = {"jskim"};
//     // char number[] = {"202533713"};
//     // char phone[] = {"010-1234-5678"};

//     // printf("%s\n%s\n%s\n", name, number, phone);

//     // char name[];과 같은 형태로는 선언 및 사용할 수 없음. (error: 잘못된 형식, 컴파일 전 에러임)
//     char name[11]; 
//     char number[20];
//     char phone[20];

//     // strcpy를 사용하려면 헤더파일 <string.h>를 선언해줘야 정상 작동함.
//     strcpy(name, "jskim");
//     strcpy(number, "202533713");
//     strcpy(phone, "010-1234-5678");

//     printf("%s\n%s\n%s\n", name, number, phone);
// }
   
// int main() {
//     char word[20];
//     char startword[20] = "apple";

//     while (1) {
//         printf("My word is %s\n", startword);
//         printf("your word?: ");
//         gets_s(word, sizeof(word));
//         // fgets(word, 20, stdin);
        
//         if (strlen(word) != 5) {
//             printf("wrong length\n");
//             continue;
//         }

//         if (startword[4] == word[0]) {
//             printf("성공\n");
//             strcpy(startword, word);
//         }
//         else{
//             printf("끝말 잇기가 안돼요\n");
//         }
//     }
// }
// void print_dan(int dan) {
//     printf("%d단\n", dan);

//     for (int i = 1; i < 10; i++) {
//         printf("%d x %d = %2d\n", dan, i, dan * i);
//     }

//     printf("\n");
// }



// int main() {
//     int dan;
//     for (dan = 2; dan < 10; dan++)
//         print_dan(dan);
// }

// static int global; // 정적 전역 변수, 0으로 초기화 됨
// int call(void);

// int call(void)
// {
//     static int in_global; // 정적 지역 변수, 0으로 초기화 됨
//     in_global += 1;

//     return in_global;
// }
// int main()
// {
//     printf("%d\n", call()); // in_global = 1
//     printf("%d\n", call()); // in_global = 2
//     printf("%d\n", call()); // in_global = 3
// }

// int i = 10;
// int main(void)
// {
//     int i = 20;
//     for (int i = 30; i < 40; i++)
//         printf("%d\n", i);
// }

// int dan;
// void print_dan(void);

// int main() {
//     for(dan = 2; dan < 10; dan++)
//         print_dan();
        
//     return 0;
// }

// void print_dan(void) {
//     for (int i = 1; i < 10; i++)
//         printf("%d x %d = %d\n", dan, i, dan * i);

//     printf("\n");
// }

// #define DIFF(x, y) (x - y)

// int main () {
//     printf("%d", DIFF(5, 3));
// }
// void change(int [][3]);

// int main() {
//     int i;
//     int value[5][3] = {0};

//     change(value);

// }

// void change(int value[][3])
// {
//     value[0][0] = 1;
// }

// int main() {
//     char start[10] = "apple";
//     char input[10];
//     int cnt = 0, state = 1;
//     int len;

//     while(cnt < 10){
//         if (state == 1){
//             cnt += 1;
//             printf("(%d) %s\n", cnt, start);
//         }

//         printf("끝말잇기 단어는? ");
//         fgets(input, 7, stdin);

//         len = strlen(input);

//         // 1. 버퍼 비우기 (핵심 해결책)
//         // 입력된 문자열 끝에 \n이 없다는 건, 글자가 짤려서 버퍼에 남았다는 뜻!
//         if (input[len - 1] != '\n') {
//             // 버퍼에 남은 걸 싹 다 꺼내서 버림(청소)
//             while (getchar() != '\n'); 
// }
//         if (len > 0 && input[len - 1] == '\n')
//             input[len - 1] = '\0';

//         if ((len - 1 != 5) || (start[4] != input[0])){
//             printf("옳지 않은 끝말잇기 단어입니다. 다시 입력하세요.\n");
//             state = 0;
//             continue;
//         }
//         else
//             state = 1;
//             strcpy(start, input);
//     }
// }

int main () {
    int N;
    int *num;
    int input, sum = 0;

    scanf("%d", &N);
    num = malloc(N * sizeof(int));

    for (int i = 0; i < N; i++){
        scanf("%d", &input);
        sum += input;
    }
    printf("총점: %d, 평균: %d\n", sum, sum / N);


int main() {
    char str1[10] = "Hello";
    char str2[10] = "World";

    printf("%s", strchr(str2, 'l'));
}