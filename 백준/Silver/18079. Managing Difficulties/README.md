# [Silver I] Managing Difficulties - 18079 

[문제 링크](https://www.acmicpc.net/problem/18079) 

### 성능 요약

메모리: 2352 KB, 시간: 1300 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 집합과 맵

### 제출 일자

2025년 5월 3일 18:48:26

### 문제 설명

<p>Every day a new programming problem is published on Codehorses. Thus, n problems will be published in the following n days: the difficulty of the i-th problem is a<sub>i</sub>.</p>

<p>Polycarp wants to choose exactly three days i, j and k (i < j < k) so that the difference of difficulties on the day j and the day i is equal to the difference of difficulties on the day k and day j. In other words, Polycarp wants equality a<sub>j</sub> − a<sub>i</sub> = a<sub>k</sub> − a<sub>j</sub> to be true.</p>

<p>Determine the number of possible ways for Polycarp to choose the three days in the desired way.</p>

### 입력 

 <p>The first line contains an integer t — the number of test cases in the input (1 ≤ t ≤ 10). Then t test case descriptions follow.</p>

<p>The first line of a test case contains an integer n — the number of the days (3 ≤ n ≤ 2000). The second line of the test case contains n integers a<sub>1</sub>, a<sub>2</sub>, . . . , a<sub>n</sub>, where a<sub>i</sub> is the difficulty of the problem on the i-th day (1 ≤ a<sub>i</sub> ≤ 10<sup>9</sup>).</p>

### 출력 

 <p>Output t integers — the answers for each of the test cases in the input, in the order they are given. The answer to a test case is the number of triples of indices i, j, and k such that 1 ≤ i < j < k ≤ n and a<sub>k</sub> − a<sub>j</sub> = a<sub>j</sub> − a<sub>i</sub>.</p>

