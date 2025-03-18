#include <stdio.h>
#include <string.h>

#define MAX_N 1000
#define MAX_W 100
#define MAX_H 100

char rocks[MAX_N][MAX_H][MAX_W + 1];
char key[MAX_H][MAX_W + 1];

int main() {
    int n, w, h;
    scanf("%d %d %d", &n, &w, &h);
    
    for (int r = 0; r < n; r++) {
        for (int i = 0; i < h; i++) {
            scanf("%s", rocks[r][i]);
        }
    }
    
    for (int i = 0; i < h; i++) {
        scanf("%s", key[i]);
    }
    
    int ans = 0;
    
    for (int r = 0; r < n; r++) {
        int valid = 1;
        for (int l = 1; l <= w; l++) {
            for (int i = 0; i < h && valid; i++) {
                for (int j = 0; j < l; j++) {
                    if (rocks[r][i][j] == '#' && key[i][w + j - l] == '#') {
                        valid = 0;
                        break;
                    }
                }
            }
            if (!valid) break;
        }
        if (valid) ans++;
    }
    
    printf("%d\n", ans);
    return 0;
}