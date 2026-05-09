// #include <stdio.h>

// double f (int n){
//     if (n == 1)
//         return 1.0;
//     return f(n-1) + 1.0 / n;;
// }

// int main () {
//     int n;
//     scanf("%d", &n);
//     pritnf("%f\n", f(n));
//     return 0;
// }

#include <stdio.h>

int fi (int n) {
    if (n <= 1)
        return n;
    return fi(n-1) + fi(n-2);
}

int main() {
    int n;
    int sum = 0;
    scanf("%d", &n);
    printf("fi: %d\n", fi(n));

    if (n <= 1)
        sum = n;

    for (int i = 2; i <= n; i++){
        
    }
    printf("%d", sum);
}