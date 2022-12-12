# [Silver IV] 소진법 - 4839 

[문제 링크](https://www.acmicpc.net/problem/4839) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

구현(implementation), 수학(math), 정수론(number_theory), 소수 판정(primality_test)

### 문제 설명

<p>2보다 크거나 같은 자연수 b가 주어졌을 때, 모든 양의 정수 n을 b진법으로 표현하는 방법은 유일하다.</p>

<p>n = a<sub>0</sub> + a<sub>1</sub>*b + a<sub>2</sub>*b*b + a<sub>3</sub>*b*b*b + ...</p>

<p>여기서 a<sub>0</sub>, a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ...은 0보다 크거나 같고, b-1보다 작거나 같은 값을 가진다.</p>

<p>p<sub>0</sub>=2, p<sub>1</sub>=3, p<sub>2</sub>=5, ... 과 같이 p<sub>i</sub>를 i번째 소수라고 했을 때, 모든 양의 정수 n도 소수를 이용한 진법으로 유일하게 표현할 수 있다. 이를 소진법이라고 한다.</p>

<p>n = a<sub>0</sub> + a<sub>1</sub>*p<sub>0</sub> + a<sub>2</sub>*p<sub>0*</sub>p<sub>1</sub> + a<sub>3</sub>*p<sub>0</sub>*p<sub>1</sub>*p<sub>2</sub> + ...</p>

<p>여기서 a<sub>0</sub>, a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ...은 0보다 크거나 같고, p<sub>i</sub>-1보다 작거나 같은 값을 가진다. 예를 들면, a<sub>3</sub>은 0보다 크거나 같고, p<sub>3</sub>-1보다 작거나 같다.</p>

<p>양의 정수 n이 주어졌을 때, 이를 소진법으로 나타내는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, n을 포함하고 있다. n은 양의 정수로 2<sup>31</sup>-1보다 작거나 같다. 마지막 줄에는 0이 주어진다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서, 입력으로 주어진 수, 공백, 등호, 공백을 출력하고 문제 설명에 나온 것 같이 소진법으로 나타내 출력한다.</p>

