# [Silver III] Global Warming - 6797 

[문제 링크](https://www.acmicpc.net/problem/6797) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 2월 16일 07:06:43

### 문제 설명

<p>Your task is to help scientists predict the trend of the global warming. One of the hypotheses they are considering is that over long periods of time, the average temperature follows certain cycles, but each time the cycle starts from a higher temperature level. The temperatures are measured over five-year averages, and expressed in tenths of a degree.</p>

<p>For example, if the following five-year averages are observed:</p>

<p style="text-align: center;">3, 4, 6, 4, 5, 7, 5</p>

<p>then we can calculate that the temperature changes first 1 tenth up, then 2 up, then 2 down, 1 up, 2 up, and 2 down. There is a cycle of changes of length three which covers all of the temperature differences: (+1, +2, −2). In other words, if we look at the differences starting at the first position, there is a cycle of length three of the form (+1, +2, −2) followed by another cycle of length three of exactly the same form.</p>

<p>By way of another example, suppose the following average temperatures are observed:</p>

<p style="text-align: center;">3, 4, 6, 7.</p>

<p>In this case, there is a difference of one up, two up, then one up. We would consider the shortest cycle to be length two in this case: the cycle (+1, +2). Notice that this cycle occurs once, followed by one truncated occurrence of exactly the same cycle.</p>

<p>Your task is to find the shortest such cycle from a given sequence of temperatures.</p>

### 입력 

 <p>The input consists of a number of test cases. Each test case starts with the number n (1 ≤ n ≤ 20), representing the number of temperatures in a sequence, followed by the sequence of n temperatures. You may assume that each temperature input is an integer in the range −1000...1000 inclusive. The numbers are separated by a single space. The last test case is indicated by a zero and should produce no output.</p>

### 출력 

 <p>For each test case, produce the length of the shortest temperature cycle. The cycle always exists, since the whole sequence could be treated as one long cycle.</p>

