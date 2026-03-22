#include <stdio.h>

int main() {

    int i = 0;
    int *j = &i;
    int **k = &j;
    int ***m = &k;

    printf("%d %p %p %p\n", i, j, k, m);
}