# [Gold III] 가장 오래 걸리는 스도쿠 - 12095 

[문제 링크](https://www.acmicpc.net/problem/12095) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

애드 혹(ad_hoc), 구성적(constructive), 런타임 전의 전처리(precomputation)

### 문제 설명

<p>백준이는 <a href="https://www.acmicpc.net/problem/2580">2580번 스도쿠 문제</a>를 풀기 위해 아래와 같은 코드를 작성했다.</p>

<pre class="brush:c++; toolbar:false;">#include <iostream>
using namespace std;
int a[10][10];
bool c[10][10];
bool c2[10][10];
bool c3[10][10];
int n=9;
int cnt=0;
int square(int x, int y) {
    return (x/3)*3+(y/3);
}
bool go(int z) {
    cnt += 1;
    if (cnt >= 10000000) {
        return true;
    }
    if (z == 81) {
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                cout << a[i][j] << ' ';
            }
            cout << '\n';
        }
        return true;
    }
    int x = z/n;
    int y = z%n;
    if (a[x][y] != 0) {
        return go(z+1);
    } else {
        for (int i=1; i<=9; i++) {
            if (c[x][i] == 0 && c2[y][i] == 0 && c3[square(x,y)][i]==0) {
                c[x][i] = c2[y][i] = c3[square(x,y)][i] = true;
                a[x][y] = i;
                if (go(z+1)) {
                    return true;
                }
                a[x][y] = 0;
                c[x][i] = c2[y][i] = c3[square(x,y)][i] = false;
            }
        }
    }
    return false;
}
int main() {
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> a[i][j];
            if (a[i][j] != 0) {
                c[i][a[i][j]] = true;
                c2[j][a[i][j]] = true;
                c3[square(i,j)][a[i][j]] = true;
            }
        }
    }
    go(0);
    return 0;
}
</pre>

<p>변수 <code>cnt</code>에 저장된 값이 가장 큰 스도쿠 퍼즐을 출력하는 프로그램을 작성하시오. 문제의 점수는 <code>cnt</code>에 저장된 값이다.</p>

### 입력 

 <p>입력은 없다.</p>

### 출력 

 <p>총 9개의 줄에 스도쿠 퍼즐을 출력한다. 빈 칸은 0으로 출력한다. (2580번 문제의 입력을 출력한다)</p>

<p>만약, 풀 수 없는 스도쿠 퍼즐을 출력한 경우에는 틀렸습니다를 받게 된다.</p>

