# [Silver III] Polygon - 18044 

[문제 링크](https://www.acmicpc.net/problem/18044) 

### 성능 요약

메모리: 135484 KB, 시간: 372 ms

### 분류

기하학, 그리디 알고리즘, 정렬

### 제출 일자

2024년 2월 10일 02:37:02

### 문제 설명

<p>You are given <em>n</em> segments of lengths <em>ℓ</em><sub>1</sub>, <em>ℓ</em><sub>2</sub>, . . . , <em>ℓ</em><em><sub>n</sub></em>, respectively. Determine the largest possible circumference of a convex polygon that can be constructed using these segments (in any order, and not neccessarily all of them). The polygon must be non-degenerate – in other words, its area must be positive.</p>

### 입력 

 <p>The first line of input contains the number of test cases <em>z</em> (1 ≤ <em>z</em> ≤ 100 000). The test cases follow, each one in the following format:</p>

<p>The first line of a test case contains the number of segments <em>n</em> (1 ≤ <em>n</em> ≤ 100 000). In the second line, there are <em>n</em> integers <em>ℓ</em><sub>1</sub>, <em>ℓ</em><sub>2</sub>, . . . , <em>ℓ</em><em><sub>n</sub></em> (1 ≤ <em>ℓ<sub>i</sub></em> ≤ 10<sup>9</sup> ) – the lengths of the segments.</p>

<p>The sum of <em>n</em> values over all test cases does not exceed 1 000 000.</p>

### 출력 

 <p>For each test case, output a single integer – the largest possible circumference of a convex polygon made of given segments. If no such polygon can be constructed at all, output 0.</p>

