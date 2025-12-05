// Q3 최대공약수, 최소공배수
#include <stdio.h>

int getGCD(int, int);
int getLCM(int, int);

int getGCD(int x, int y) {

}
int main() {
    int x, y;
    
    printf("두 개의 정수 입력: ");
    scanf("%d %d", &x, &y);

    printtf("최대 공약수: %d\n", getGCD(x, y));
    printtf("최소 공배수: %d\n", getLCM(x, y));
}