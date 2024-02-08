# [Silver III] Subset Sum - 4132 

[문제 링크](https://www.acmicpc.net/problem/4132) 

### 성능 요약

메모리: 112168 KB, 시간: 144 ms

### 분류

백트래킹

### 제출 일자

2024년 2월 9일 02:19:06

### 문제 설명

<p>Maia would like to buy exactly 3.141592 litres of milk. But guess what? Her local grocery store does not stock a bag that size! So Maia decides to buy multiple bags. Even so, it might not be possible to buy a total of exactly 3.141592 litres. In that case, she is willing to buy a little bit more if necessary, but she wants to minimize the extra amount. In addition, Maia wants the bags to all be of distinct sizes, because it would be too boring to buy two bags of the same size. Maia painstakingly figures out which bags of milk to buy. But the next day, she wants 2.718281 litres of milk, and she has to figure it all out again. Clearly she needs to write a program to help her.</p>

### 입력 

 <p>The first line of input contains two integers 0 <= n <= 1000000000 and 0 < m <= 20, the number of microlitres of milk that Maia wants, and the number of sizes of milk that the store sells. The following m lines each contain an integer 0 <= a <= 1000000000, the size of a bag of milk that the store sells (in microlitres).</p>

### 출력 

 <p>Output a single integer, the minimum total number of microlitres of milk that Maia needs to buy in order to have at least n microlitres. If it is not possible to buy at least n microlitres, output the word IMPOSSIBLE.</p>

