# [Silver V] Trol - 17817 

[문제 링크](https://www.acmicpc.net/problem/17817) 

### 성능 요약

메모리: 30840 KB, 시간: 84 ms

### 분류

사칙연산(arithmetic), 조합론(combinatorics), 구현(implementation), 수학(math), 정수론(number_theory)

### 문제 설명

<p>Stjepan recently received his bachelor’s degree in mathematics from the University of Zagreb. Naturally, his parents are very proud and have decided to give him all positive integers not greater than 2<sup>60</sup> as a gift. To keep them safe, he quickly stored all of those numbers in an array A, such that A<sub>i</sub> = i.</p>

<p>His jealous friend Marin decided to prank him by repeatedly replacing each element of A with the sum of its digits until all elements of A consisted of a single digit. For example, the initial value of 197th element of A was 197. Marin first changed that value to 1 + 9 + 7 = 17 and then changed its value again to 1 + 7 = 8.</p>

<p>Stjepan is devastated and begs Marin to return his array to its initial state. Unfortunately, Marin won’t do that until Stjepan correctly answers his Q queries: “What is the sum of numbers from l-th to r-th element of A?”.</p>

<p>Help Stjepan answer those queries!</p>

### 입력 

 <p>The first line contains an integer Q (1 ≤ Q ≤ 100) from the task description.</p>

<p>The next Q lines contain two integers l<sub>i</sub> and r<sub>i</sub> (1 ≤ l<sub>i</sub> ≤ r<sub>i</sub> ≤ 2<sup>60</sup>), the parameters of Marin’s i-th query.</p>

### 출력 

 <p>Output the answers to each of Marin’s Q queries. Each answer should be printed in a separate line and their order should match the order of the queries as they are given in the input.</p>

