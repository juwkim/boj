# [Silver I] The Monkey Dance - 6936 

[문제 링크](https://www.acmicpc.net/problem/6936) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

유클리드 호제법, 그래프 이론, 그래프 탐색, 수학, 정수론, 순열 사이클 분할

### 제출 일자

2025년 5월 8일 12:58:10

### 문제 설명

<p>The director of Hind Circus has decided to add a new performance, the monkey dance, to his show. The monkey dance is performed simultaneously by $N$ monkeys. There are $N$ circles drawn on the ground, labelled from $1$ to $N$. In the beginning, each monkey sits on a different circle. There are $N$ arrows drawn from circle to circle in such a way that there is exactly one arrow pointing toward each ring and exactly one arrow pointing away from each ring.</p>

<p>When the show begins, at each whistle of the ringmaster, all the monkeys simultaneously jump from their respective circles to other circles following the arrows from their respective current circles. This is one step of the dance. The dance ends when all the monkeys have returned to the circles where they initially started. How long does the dance last?</p>

### 입력 

 <p>The input may have multiple cases. Each case consists of the value of $N$ $(1 \le N \le 100)$ on a line, followed by $N$ lines, each with a pair of integers between $1$ and $N$. The pair $I_1$, $I_2$ means that there is an arrow from circle $I_1$ to circle $I_2$. The input ends with 0 for the value of $N$.</p>

### 출력 

 <p>For each case, simply output the number of steps in the dance. Each output should be on a separate line.</p>

