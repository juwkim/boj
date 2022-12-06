# include <stdio.h> 

int main() {
    int Q, a;
    scanf("%d", &Q);
    for (int i = 0; i < Q; i++) {
        scanf("%d", &a);
        if ((a & (-a)) == a) {
            printf("1\n");
        }
        else {
            printf("0\n");
        }
    }
}