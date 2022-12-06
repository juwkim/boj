# [Bronze II] DNA 해독 - 1672 

[문제 링크](https://www.acmicpc.net/problem/1672) 

### 성능 요약

메모리: 31156 KB, 시간: 336 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p>N개의 A, G, C, T로 구성되어 있는 DNA 염기서열이 있다. 그리고 우리는 이 염기서열을 아래의 표를 이용하여 해독을 해야 한다.</p>

<p style="text-align: center;"><img alt="" height="179" src="" width="307"></p>

<p>해독 방법은 염기 서열에서 제일 끝에 있는 두 개의 염기를 A<sub>n-1</sub>, A<sub>n</sub>이라 할 때, A<sub>n-1</sub>을 행으로 A<sub>n</sub>을 열로 대응시켜 그에 해당하는 하나의 염기로 바꾸는 방식을 반복하는 것이다.  예를 들어 <code>AAGTCG</code>라는 염기서열이 있다고 하자. 이 서열을 위의 규칙 때로 해독하면 <code>AAGTCG</code> → <code>AAGTT</code> → <code>AAGT</code> → <code>AAA</code> → <code>AA</code> → <code>A</code> 가 되어 최종적으로 해독한 염기는 <code>A</code>가 된다.</p>

<p>문제는 어떤 염기서열이 주어졌을 때 위의 표를 참고하여 해독된 최종 염기를 출력하는 것이다.</p>

### 입력 

 <p>첫째 줄에 염기 서열의 길이 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 염기서열을 나타내는 길이가 N인 문자열이 주어진다.</p>

### 출력 

 <p>첫째 줄에 최종 염기를 출력한다.</p>

