#include <stdio.h>
#include <stdlib.h>

#define MAXN 150

int R, C, a[MAXN][MAXN];
int px1[MAXN + 1][MAXN] = {0}, px2[MAXN][MAXN + 1] = {0};
int ans[MAXN * MAXN][4], ansCount = 0, Max = 1;

int main() {
    scanf("%d %d", &R, &C);
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    for (int i = 1; i <= R; i++) {
        int cur = 0;
        for (int j = 1; j < C; j++) {
            cur += (a[i - 1][j - 1] >= a[i - 1][j]);
            px1[i][j] = cur + px1[i - 1][j];
        }
    }
    
    for (int j = 1; j <= C; j++) {
        int cur = 0;
        for (int i = 1; i < R; i++) {
            cur += (a[i - 1][j - 1] >= a[i][j - 1]);
            px2[i][j] = cur + px2[i][j - 1];
        }
    }

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            for (int k = (Max + C - j - 1) / (C - j); k <= R - i; k++) {
                for (int l = (Max + k - 1) / k; l <= C - j; l++) {
                    if (px1[i + k][j + l - 1] - px1[i + k][j] - px1[i][j + l - 1] + px1[i][j] == 0 && 
                        px2[i + k - 1][j + l] - px2[i][j + l] - px2[i + k - 1][j] + px2[i][j] == 0) {
                        if (k * l > Max) {
                            Max = k * l;
                            ansCount = 0;
                            ans[ansCount][0] = i + 1;
                            ans[ansCount][1] = j + 1;
                            ans[ansCount][2] = k;
                            ans[ansCount][3] = l;
                            ansCount++;
                        } else if (k * l == Max) {
                            ans[ansCount][0] = i + 1;
                            ans[ansCount][1] = j + 1;
                            ans[ansCount][2] = k;
                            ans[ansCount][3] = l;
                            ansCount++;
                        }
                    }
                }
            }
        }
    }

    for (int i = 0; i < ansCount; i++) {
        printf("%d %d %d %d\n", ans[i][0], ans[i][1], ans[i][2], ans[i][3]);
    }
    
    return 0;
}