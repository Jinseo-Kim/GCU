#include <stdio.h>

int main() {
    int i = 0, *p = 0;

    for (p = &i; *p < 10; (*p)++)
        printf("%d\n", *p);
}