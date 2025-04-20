# [Silver I] Histogram Sequence 4 - 25730 

[문제 링크](https://www.acmicpc.net/problem/25730) 

### 성능 요약

메모리: 130764 KB, 시간: 184 ms

### 분류

해 구성하기

### 제출 일자

2025년 4월 20일 18:17:33

### 문제 설명

<p>You had a histogram made of $N$ axis-parallel rectangles sharing a common baseline: the $i$-th rectangle from the left had a width $1$ and an integer height $H_i$.</p>

<p>Sadly, you lost your histogram! Moreover, you even forgot what your histogram looked like — the heights of the rectangles of the histogram. What you remember is the maximum area $A$ of the axis-parallel rectangle inside the histogram, and the fact that $L\le H_i\le R$ for every $H_i$.</p>

<p>Your goal is to recover the histogram by finding any histogram satisfying all the requirements that you remember. As your memory might not be perfect, there may be no histogram satisfying the requirements.</p>

### 입력 

 <p>The first and only line contains four space-separated integers, $N$, $A$, $L$, $R$.</p>

### 출력 

 <p>If there is no histogram satisfying the requirements, output <span style="color:#e74c3c;"><code>NO</code></span>.</p>

<p>Otherwise, output <span style="color:#e74c3c;"><code>YES</code></span> in the first line. In the second line, output $N$ integers in a single line, where the $i$-th value is the height $H_i$ of the $i$-th rectangle. If there are multiple answers, print any.</p>

