// Q1 함수
#include <stdio.h>

int is_prime(int);

int is_prime(int num)
{
    if (num == 2 || num % 2 == 1) // 2이거나 홀수이면
        return 1;
    else
        return 0;
}

int main()
{
    int num;
    printf("정수: ");
    scanf("%d", &num);

    if (is_prime(num))
        printf("%d is prime number\n", num);
}

//Q2