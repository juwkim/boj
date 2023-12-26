#include <stdio.h>
#include <string.h>

#define MOD 1000000007

int dp[2][252][252][4];
int main() {
    int T; scanf("%d\n", &T);
    for (int tc = 1; tc <= T; tc++) {
        char s[501]; scanf("%s", s);
        int n = strlen(s);
        memset(dp, 0, sizeof(dp));
        dp[0][0][0][0] = 1;
        for (int i = 0; i < n; ++i) {
            int cur = i & 1;
            int nxt = cur ^ 1;
            memset(dp[nxt], 0, sizeof(dp[nxt]));
            for (int j = 0; j <= n / 2; ++j) {
                for (int k = 0; k <= n / 2; ++k) {
                    if (dp[cur][j][k][0] == 0 && dp[cur][j][k][1] == 0 && dp[cur][j][k][2] == 0 && dp[cur][j][k][3] == 0) {
                        continue;
                    }
                    dp[nxt][j][k][0] = (dp[nxt][j][k][0] + dp[cur][j][k][0]) % MOD;
                    dp[nxt][j][k][1] = (dp[nxt][j][k][1] + dp[cur][j][k][1]) % MOD;
                    dp[nxt][j][k][2] = (dp[nxt][j][k][2] + dp[cur][j][k][2]) % MOD;
                    dp[nxt][j][k][3] = (dp[nxt][j][k][3] + dp[cur][j][k][3]) % MOD;
                    switch (s[i]) {
                        case 'a':
                            dp[nxt][j + 1][k][0] = (dp[nxt][j + 1][k][0] + dp[cur][j][k][0]) % MOD;
                            break;
                        case 'b':
                            dp[nxt][j][k + 1][1] = (dp[nxt][j][k + 1][1] + dp[cur][j][k][1] + (j > 0 ? dp[cur][j][k][0]: 0)) % MOD;
                            break;
                        case 'c':
                            if (j == 1)
                                dp[nxt][0][k][3] = (dp[nxt][0][k][3] + dp[cur][j][k][1] + dp[cur][j][k][2]) % MOD;
                            else if (j > 0)
                                dp[nxt][j - 1][k][2] = (dp[nxt][j - 1][k][2] + dp[cur][j][k][1] + dp[cur][j][k][2]) % MOD;
                            break;
                        case 'd':
                            if (k == 1)
                                dp[nxt][0][0][0] = (dp[nxt][0][0][0] + dp[cur][j][k][3]) % MOD;
                            else if (k > 0)
                                dp[nxt][0][k - 1][3] = (dp[nxt][0][k - 1][3] + dp[cur][j][k][3]) % MOD;
                            break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", tc, (dp[n&1][0][0][0] - 1 + MOD) % MOD);
    }
    return 0;
}