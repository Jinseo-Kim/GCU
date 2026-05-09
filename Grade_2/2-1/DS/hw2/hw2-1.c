#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct {
    float coef;
    int expon;
} Terms;

Terms *terms = NULL;
int avail = 0;
int max = 0;

// 두 개의 정수를 비교
char compare(int a, int b) {
    if (a > b)
        return '>';
    else if (a == b)
        return '=';
    else
        return '<';
}

// 새로운 항을 다항식에 추가한다.
void attach(float coef, int expon) {
    if (avail >= max) {
        if (max == 0) {
            max = 20;
        }
        else {
            max *= 2;
        }

        terms = (Terms*)realloc(terms, sizeof(Terms) * max);

        if (terms == NULL) {
            printf("메모리 할당 실패\n");
            exit(1);
        }
    }
    terms[avail].coef = coef;
    terms[avail].expon = expon;

    avail++;
}

void poly_add2(int As, int Ae, int Bs, int Be, int *Cs, int *Ce)
{
    float tempcoef;
    *Cs = avail;
    while (As <= Ae && Bs <= Be)
        switch (compare(terms[As].expon, terms[Bs].expon))
        {
        case '>': // A의 지수 > B의 지수
            attach(terms[As].coef, terms[As].expon);
            As++;
            break;
        case '=': // A의 지수== B의 지수
            tempcoef = terms[As].coef + terms[Bs].coef;
            if (tempcoef)
                attach(tempcoef, terms[As].expon);
            As++;
            Bs++;
            break;
        case '<': // A의 지수 < B의 지수
            attach(terms[Bs].coef, terms[Bs].expon);
            Bs++;
            break;
        }

    // A의 나머지 항들을 이동함
    for (; As <= Ae; As++)
        attach(terms[As].coef, terms[As].expon);

    // B의 나머지 항들을 이동함
    for (; Bs <= Be; Bs++)
        attach(terms[Bs].coef, terms[Bs].expon);
    *Ce = avail - 1;
}

void sort(int *Ms, int *Me) {
    Terms sort_terms;

    // 내림차순 정렬
    for (int i = *Ms; i <= *Me; i++) {
        for (int j = i+1; j <= *Me; j++) {
             if (terms[j].expon > terms[i].expon) {
                sort_terms = terms[j];
                terms[j] = terms[i];
                terms[i] = sort_terms;
            }
        }
    }

    // 값 합치기
    for (int i = *Ms; i <= *Me; i++)
        for (int j = i+1; j <= *Me; j++) {
            // if (terms[i].coef == 0 && terms[i].expon == 0)
            //     break;
            if (terms[i].expon == terms[j].expon) {
                terms[i].coef += terms[j].coef;

                terms[j].coef = 0;
                terms[j].expon = 0;
            }
            else
                break;
        }

}

void poly_multiply(int As, int Ae, int Bs, int Be, int *Ms, int *Me)
{
    float tempcoef;
    int tempexpon;
    *Ms = avail;
    
    for (int i = As; i <= Ae; i++) {
        for (int j = Bs; j <= Be; j++) {
            tempcoef = terms[i].coef * terms[j].coef;
            tempexpon = terms[i].expon + terms[j].expon;
            attach(tempcoef, tempexpon);
        }
    }

    *Me = avail - 1;

    sort(Ms, Me);

}

float eval_nums(int start, int end, float x) {
    float result = 0;

    for (int i = start; i <= end; i++) {
        if (terms[i].coef != 0) {
            result += (terms[i].coef * pow(x, terms[i].expon));
        }
    }

    return result;
}

int main() {
    char input[1000];
    int start1, end1, start2, end2;
    int Cs, Ce; // add start, add end
    int Ms, Me; // Multiply start, Multiply end
    char* enter;
    char* token;
    float coef;
    int expon;


    // 수식 1 입력
    printf("수식 1을 입력하세요: ");
    fgets(input, sizeof(input), stdin);

    enter = strchr(input, '\n');
    *enter = '\0';

    start1 = avail;

    token = strtok(input, " ");             // str(coef), 최초 한번만임
    // 1 ~ 4 반복
    while (token != NULL) {
        coef = atof(token);                 // 2. float(coef)

        token = strtok(NULL, " ");          // 3. str(expon)
        if (token == NULL){
            printf("coef (O) expon (X)\n");
            break;
        }
        expon = atoi(token);                // 4. int(expon)

        attach(coef, expon);                // 5. 구조체에 값 넣고 다음 인덱스로 이동(avail++)

        token = strtok(NULL, " ");          //1. str(coef), 최초 이후
    }

    end1 = avail-1;     // atatch() 마지막 호출에서 avail++로 인해 -1 해줘야 end임


    // 수식 2 입력
    printf("수식 2을 입력하세요: ");
    fgets(input, sizeof(input), stdin);

    enter = strchr(input, '\n');
    *enter = '\0';

    start2 = avail;

    token = strtok(input, " ");             // str(coef), 최초 한번만임
    // 1 ~ 4 반복
    while (token != NULL) {
        coef = atof(token);                 // 2. float(coef)

        token = strtok(NULL, " ");          // 3. str(expon)
        if (token == NULL)
            break;
        expon = atoi(token);                // 4. int(expon)

        attach(coef, expon);                // 5. 구조체에 값 넣고 다음 인덱스로 이동(avail++)

        token = strtok(NULL, " ");          //1. str(coef), 최초 이후
    }

    end2 = avail-1;     // atatch() 마지막 호출에서 avail++로 인해 -1 해줘야 end임
    
    poly_add2(start1, end1, start2, end2, &Cs, &Ce);
    poly_multiply(start1, end1, start2, end2, &Ms, &Me);

    // test목적 출력(poly_add2)
    // for (int i = Cs; i <= Ce; i++) {
    //     printf("terms[%d] = [%f, %d]", i, terms[i].coef, terms[i].expon);
    // }
    // printf("\n");

    // test목적 출력(poly_multiply)
    // for (int i = Ms; i <= Me; i++) {
    //     printf("terms[%d] = [%f, %d]\n", i, terms[i].coef, terms[i].expon);
    // }

    // 원본 출력
    printf("1 + 2 = ");
    for (int i = Cs; i <= Ce; i++) {
        if (i != Cs)
            printf("+");
        if (terms[i].expon == 0)
            printf("%d", (int)terms[i].coef);
        else if (terms[i].expon == 1)
            printf("%dx", (int)terms[i].coef);
        else 
            printf("%dx^%d", (int)terms[i].coef, terms[i].expon);
    }
    printf("\n");


    printf("1 * 2 = ");
    for (int i = Ms; i <= Me; i++) {
        if (terms[i].coef == 0)
            continue;

        if (i != Ms)
            printf("+");
        if (terms[i].expon == 0)
            printf("%d", (int)terms[i].coef);
        else if (terms[i].expon == 1)
            printf("%dx", (int)terms[i].coef);
        else 
            printf("%dx^%d", (int)terms[i].coef, terms[i].expon);

    }
    printf("\n");

    float x;

    printf("수식에 x의 값을 넣으세요 ");
    scanf("%f", &x);

    float x1 = eval_nums(start1, end1, x);
    float x2 = eval_nums(start2, end2, x);
    float add = eval_nums(Cs, Ce, x);
    float mul = eval_nums(Ms, Me, x);

    printf("수식1 = %g\n", x1);
    printf("수식2 = %g\n", x2);
    printf("수식1+2 = %g\n", add);
    printf("수식1*2 = %g\n", mul);

}