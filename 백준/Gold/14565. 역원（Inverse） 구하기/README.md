# [Gold II] 역원(Inverse) 구하기 - 14565 

[문제 링크](https://www.acmicpc.net/problem/14565) 

### 성능 요약

메모리: 113248 KB, 시간: 108 ms

### 분류

확장 유클리드 호제법(extended_euclidean), 수학(math), 모듈로 곱셈 역원(modular_multiplicative_inverse), 정수론(number_theory)

### 문제 설명

<p>집합 Zn을 0부터 n-1까지의 정수 집합이라고 하자. Zn ∋ a, b, c 일 때, (a+b) mod n = 0이면 b는 a의 덧셈역이라고 하고 (a*c) mod n = 1이면 c는 a의 곱셈역이라고 한다.</p>

<p>정수 N, A가 주어졌을 때 Zn에서의 A의 덧셈역과 곱셈역을 구하시오.</p>

<p>단, 곱셈역을 구할 수 없으면 -1을 출력한다.</p>

### 입력 

 <p>첫 번째 줄에 N(2 ≤ N ≤ 10<sup>12</sup>)과 A(1 ≤ A < N)이 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 A의 N에 대한 덧셈역과 곱셈역을 한 줄에 공백으로 구분하여 출력한다.</p>

