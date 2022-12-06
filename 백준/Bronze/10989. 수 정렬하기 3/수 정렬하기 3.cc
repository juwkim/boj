#include <stdio.h>

int main()
{
    int N, num;
    int array[10001] = {0, };
    scanf("%d", &N);

    for (int i=0; i < N; i++) {
        scanf("%d", &num);
        array[num]++;
    }
    for (int i=1; i <= 10000; i++) {
        int count = array[i];
        for (int j=0; j < count; j++)
            printf("%d\n", i);
    }
    return 0;
}