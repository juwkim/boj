# [Silver II] 신나는 함수 실행 - 9184 

[문제 링크](https://www.acmicpc.net/problem/9184) 

### 성능 요약

메모리: 119788 KB, 시간: 860 ms

### 분류

다이나믹 프로그래밍(dp), 재귀(recursion)

### 문제 설명

<p>재귀 호출만 생각하면 신이 난다! 아닌가요?</p>

<p>다음과 같은 재귀함수 w(a, b, c)가 있다.</p>

<pre>if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
</pre>

<p>위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)</p>

<p>a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다. 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.</p>

### 출력 

 <p>입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.</p>

