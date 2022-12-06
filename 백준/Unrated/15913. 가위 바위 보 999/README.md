# [Unrated] 가위 바위 보 999 - 15913 

[문제 링크](https://www.acmicpc.net/problem/15913) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

Empty

### 문제 설명

<p>채점 프로그램과 가위 바위 보를 999번 해서, 최대한 많이 이겨 보자.</p>

<p>채점 프로그램은 랜덤을 이용해 가위 바위 보 중 하나를 결정하며, 그 코드를 간단히 나타내면 다음과 같다. 아래 코드의 변수 <code>judge</code>가 채점 프로그램이 결정한 값이다.</p>

<pre class="brush:c++; toolbar:false;">#include <random>
using namespace std;
int main() {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> distribution(0, 2);
    int judge = distribution(gen);
    return 0;
} </pre>

### 입력 

 <p>이 문제는 입력이 없다.</p>

### 출력 

 <p>첫째 줄에 무엇을 낼 것인지 출력한다.</p>

<p>가위는 0, 바위는 1, 보는 2이다.</p>

