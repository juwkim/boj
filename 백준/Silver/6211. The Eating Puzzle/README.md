# [Silver II] The Eating Puzzle - 6211 

[문제 링크](https://www.acmicpc.net/problem/6211) 

### 성능 요약

메모리: 110760 KB, 시간: 100 ms

### 분류

백트래킹, 브루트포스 알고리즘

### 제출 일자

2024년 12월 8일 00:27:03

### 문제 설명

<p>Bessie is on a diet where she can eat no more than C (10 <= C <= 35,000) calories per day. Farmer John is teasing her by putting out B (1 <= B <= 21) buckets of feed, each with some (potentially non-unique) number of calories (range: 1..35,000). Bessie has no self-control: once she starts on a feed bucket, she consumes all of it.</p>

<p>Bessie is not so good at combinatorics. Determine the optimal combination of feed buckets that gives Bessie as many calories without exceeding the limit C.</p>

<p>As an example, consider a limit of 40 calories and 6 buckets with 7, 13, 17, 19, 29, and 31 calories. Bessie could eat 7 + 31 = 38 calories but could eat even more by consuming three buckets: 7 + 13 + 19 = 39 calories. She can find no better combination.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: C and B</li>
	<li>Line 2: B space-separated integers that respectively name the number of calories in bucket 1, 2, etc.</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single line with a single integer that is largest number of calories Bessie can consume and still stay on her diet.</li>
</ul>

