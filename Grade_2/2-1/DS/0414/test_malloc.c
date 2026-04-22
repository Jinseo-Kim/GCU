#include <stdio.h>
char max_size = 10;

int main() {
    char a[10] = {0};
    char cnt = 0;

    char *real_mem = (char*)malloc(max_size);
    char flag = 0;

    while (flag != 0){
        fgets(a, 10, stdin);
        if (strchr(a, '\0') != NULL)
            break;
        for (int i = 0; i < 10; i++)
            real_mem[(cnt * max_size) + i] = a[i];
            
        cnt += 1;
        real_mem = realloc(real_mem, (cnt * max_size) + max_size);
    }

    // for (int i = 0; i < cnt * max_size; i++)
    //     printf("%d ", );
}