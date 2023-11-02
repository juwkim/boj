# [Silver IV] Lost Cows - 27054 

[문제 링크](https://www.acmicpc.net/problem/27054) 

### 성능 요약

메모리: 110644 KB, 시간: 132 ms

### 분류

애드 혹

### 제출 일자

2023년 11월 2일 11:18:31

### 문제 설명

<p>N (2 ≤ N ≤ 8,000) cows have unique brands in the range 1..N. In a spectacular display of poor judgment, they visited the neighborhood 'watering hole' and drank a few too many beers before dinner. When it was time to line up for their evening meal, they did not line up in the required ascending numerical order of their brands.</p>

<p>Regrettably, FJ does not have a way to sort them. Furthermore, he's not very good at observing problems. Instead of writing down each cow's brand, he determined a rather silly statistic: For each cow in line, he knows the number of cows that precede that cow in line that do, in fact, have smaller brands than that cow.</p>

<p>Given this data, tell FJ the exact ordering of the cows.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer, N</li>
	<li>Lines 2..N: These N-1 lines describe the number of cows that precede a given cow in line and have brands smaller than that cow. Of course, no cows precede the first cow in line, so she is not listed. Line 2 of the input describes the number of preceding cows whose brands are smaller than the cow in slot #2; line 3 describes the number of preceding cows whose brands are smaller than the cow in slot #3; and so on.</li>
</ul>

### 출력 

 <ul>
	<li>Lines 1..N: Each of the N lines of output tells the brand of a cow in line. Line #1 of the output tells the brand of the first cow in line; line 2 tells the brand of the second cow; and so on.</li>
</ul>

