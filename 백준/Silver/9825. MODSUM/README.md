# [Silver I] MODSUM - 9825 

[문제 링크](https://www.acmicpc.net/problem/9825) 

### 성능 요약

메모리: 209520 KB, 시간: 620 ms

### 분류

백트래킹, 브루트포스 알고리즘, 다이나믹 프로그래밍, 수학

### 제출 일자

2025년 5월 6일 13:43:45

### 문제 설명

<p>In this task, you are given the following function \(f\) with \(n\) parameters:</p>

<p>\[f(x_1, \dots, x_n) = \left(\left(\left(x_1 + x_2 + \dots + x_n\right)^4 + 2 \times \left(x_1 + x_2 + \dots + x_n \right)^2 \right) \mod {5} \right) + 1\]</p>

<p>As arguments, \(f\) accepts only integer values. Your task is to compute the sum of all values of \(f\), where each input \(x_i\) ranges from an integer value \(v_i\) to \(w_i\). In other words, you need to compute</p>

<p>\[\sum_{x_1 = v_1}^{w_1}\sum_{x_2 = v_2}^{w_2} \cdots \sum_{x_n = v_n}^{w_1} f(x_1, \dots, x_n)\]</p>

<p>For example, if \(n = 3, v_1 = 2, w_1 = 3, v_2 = 10, w_2 = 12, v_3 = 17\) and \(w_3 = 17\), then the result should be 19, since \(f(2, 10, 17) = 4, f(2, 11, 17) = 1, f(2, 12, 17) = 4, f(3, 10, 17) = 1, f(3, 11, 17) = 4\) and \(f(3, 12, 17) = 5\).</p>

<p>Important note: You can assume that the result will always be less than 1,000,000.</p>

### 입력 

 <p>Your program must read from the standard input. The input consists of \(n\), where \(1 \le n \le 1000\), followed by \(n\) pairs of numbers, \(v_i\) and \(w_i\), each of which ranges from 0 to 100. For each pair \(v_i\) and \(w_i\), you can assume that \(v_i \le w_i\).</p>

### 출력 

 <p>Your program must write to the standard output the required sum.</p>

