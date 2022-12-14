# [Silver IV] Rearranging a Sequence - 13399 

[문제 링크](https://www.acmicpc.net/problem/13399) 

### 성능 요약

메모리: 151848 KB, 시간: 220 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>You are given an ordered sequence of integers, (1, 2, 3, . . . , n). Then, a number of requests will be given. Each request specifies an integer in the sequence. You need to move the specified integer to the head of the sequence, leaving the order of the rest untouched. Your task is to find the order of the elements in the sequence after following all the requests successively.</p>

### 입력 

 <p>The input consists of a single test case of the following form.</p>

<pre>n m
e<sub>1</sub>
.
.
.
e<sub>m</sub></pre>

<p>The integer n is the length of the sequence (1 ≤ n ≤ 200000). The integer m is the number of requests (1 ≤ m ≤ 100000). The following m lines are the requests, namely e<sub>1</sub>, . . . , e<sub>m</sub>, one per line. Each request e<sub>i</sub> (1 ≤ i ≤ m) is an integer between 1 and n, inclusive, designating the element to move. Note that, the integers designate the integers themselves to move, not their positions in the sequence.</p>

### 출력 

 <p>Output the sequence after processing all the requests. Its elements are to be output, one per line, in the order in the sequence.</p>

