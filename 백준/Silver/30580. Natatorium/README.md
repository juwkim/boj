# [Silver IV] Natatorium - 30580 

[문제 링크](https://www.acmicpc.net/problem/30580) 

### 성능 요약

메모리: 170452 KB, 시간: 192 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵

### 제출 일자

2023년 11월 10일 14:02:49

### 문제 설명

<p>Tomorrow Programming School Department of Arithmetics is going to build a new pool in the basement of their building. The pool will serve mainly for testing of innovative floating point arithmetic algorithms, especially their floating properties in different kinds of liquids. Occasionally, the members of the staff will be allowed to the pool as well. To make the pool optimally fit for human needs, the department has to decide on the pool dimensions. The pool will be rectangular, it must not be a square. Its exact surface area C is predetermined by the choice of the relevant algorithms to be tested there. The company they hired to build the pool offers the list of possible pool side lengths. They have studied the demand in detail and they guarantee that a pool with the given area can be built using the lengths in the list. However, the particular choice is up to the department.</p>

<p>As the presented list is relatively long, the department also hired a junior programmer who is going to find out which lengths from the list can be chosen. Before he started his job, the programmer had made interesting observations. First, all available pool side lengths are primes. Second, the surface area C of the pool is a product of two distinct primes. He thinks this information may be helpful to find appropriate side lengths reasonably quickly.</p>

<p>Be faster than the hired programmer and solve the problem first.</p>

### 입력 

 <p>The first input line contains integer C (1 ≤ C ≤ 10<sup>18</sup>), the area of the pool surface. The second line contains integer M (1 ≤ M ≤ 2 · 10<sup>5</sup>), the number of pool side lengths offered by the company. The third line contains a list of space-separated unique primes P<sub>1</sub>, . . . , P<sub>M</sub> (1 < P<sub>i</sub> < 10<sup>9</sup>), representing the offered pool side lengths.</p>

<p>All measurements are expressed in the same units.</p>

### 출력 

 <p>Output a single line with two space-separated pool side lengths from the offered list, which can be used to build the pool. The first side length has to be smaller than the second one.</p>

