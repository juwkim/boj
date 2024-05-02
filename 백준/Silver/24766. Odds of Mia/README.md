# [Silver III] Odds of Mia - 24766 

[문제 링크](https://www.acmicpc.net/problem/24766) 

### 성능 요약

메모리: 113312 KB, 시간: 484 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2024년 5월 2일 23:20:31

### 문제 설명

<p>This problem relates to the game of Mia introduced earlier. We recommend that you first solve Mia to understand how the game is scored. In this problem, you are asked to compute the odds that player 1 will win given partial knowledge of both rolls.</p>

### 입력 

 <p>The input will contain multiple test cases. Each test case contains on a single line four symbols s<sub>0</sub> s<sub>1</sub> r<sub>0</sub> r<sub>1</sub> where s<sub>0</sub> s<sub>1</sub> represent the dice rolled by players 1 and r<sub>0</sub> r<sub>1</sub> represents the dice rolled by player 2. A <code>*</code> represents that the value is not known, otherwise a digit represents the value of the dice. The input will be terminated by a line containing 4 zeros.</p>

### 출력 

 <p>For each test case output the odds that player 1 will win. If the odds are 0 or 1, output <code>0</code> or <code>1</code>. Otherwise, output the odds in the form <code>a/b</code> where <code>a</code> and <code>b</code> represent the nominator and denominator of a reduced fraction (i.e., in lowest terms).</p>

