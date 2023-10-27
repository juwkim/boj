# [Silver IV] Angry Teacher - 7459 

[문제 링크](https://www.acmicpc.net/problem/7459) 

### 성능 요약

메모리: 114828 KB, 시간: 1152 ms

### 분류

임의 정밀도 / 큰 수 연산

### 제출 일자

2023년 10월 28일 05:34:05

### 문제 설명

<p>Mr. O’Cruel is teaching Math to ninth grade students. Students of course are very lazy, so they do not like to do their homework. On the other side, Mr. O’Cruel doesn’t like lazy students.</p>

<p>Recently Andrew failed to do his homework again, so he was given a special task. If he doesn’t do it, he will be expelled from his school. The task seems very easy, but it is very technical, so it would take a lot of time. Andrew is given a polynomial p(x) = a<sub>n</sub>x<sup>n</sup> + a<sub>n−1</sub>x<sup>n−1</sup> + ... + a<sub>1</sub>x + a<sub>0</sub> with integer coefficients. He must calculate the value of the polynomial for k successive integer numbers starting from l. Of course writing all these numbers would require too much paper. So as a proof of completing the task, for each number x from l to l + k − 1 Andrew is asked to provide the sum of squares of m last digits in decimal notation of p(x).</p>

<p>Since Andrew is lazy, he doesn’t want to do the task by himself. So he asks you to write the program that calculates the values requested.</p>

### 입력 

 <p>The first line of the input file contains n, l, k, and m (0 ≤ n ≤ 10, 0 ≤ l ≤ 10<sup>1000</sup>, 1 ≤ k ≤ 1 000, 1 ≤ m ≤ 1 000).</p>

<p>The following n + 1 lines contain coefficients of the polynomial: an, an−1,...,a1, a0 (0 ≤ ai ≤ 10<sup>1000</sup>).</p>

### 출력 

 <p>Output k lines — for x from l to l + k − 1 output the sum of squares of last m digits of p(x).</p>

