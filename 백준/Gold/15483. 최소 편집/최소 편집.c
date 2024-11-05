#include <stdio.h>
#include <string.h>
#define MAX_LEN 1001

char A[MAX_LEN], B[MAX_LEN];
int p[2][MAX_LEN];  // 두 개의 행을 가지는 배열
int current = 0;    // 현재 사용 중인 행 인덱스

// C 스타일의 min 함수 정의
int min(int x, int y, int z) {
    int m = (x < y) ? x : y;
    return (m < z) ? m : z;
}

int main() {
    scanf("%s%s", A, B);
    
    int lenA = strlen(A);
    int lenB = strlen(B);

    // Initialize the first row of p
    for (int j = 0; j <= lenB; j++) {
        p[0][j] = j;  // p[0] 초기화
    }

    for (int i = 0; i < lenA; i++) {
        // 현재 행과 다음 행을 전환
        current = (current + 1) % 2; // 행 인덱스 전환
        int next = (current + 1) % 2; // 다음 행 인덱스

        // c[0] 초기화
        p[current][0] = i + 1;

        for (int j = 0; j < lenB; j++) {
            int cost = (A[i] == B[j]) ? p[next][j] : 1 + min(p[current][j], p[next][j], p[next][j + 1]);
            p[current][j + 1] = cost;
        }
    }

    // 결과 출력
    printf("%d\n", p[current][lenB]);
    return 0;
}
