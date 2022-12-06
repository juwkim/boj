# [Diamond V] Binomial - 18719 

[문제 링크](https://www.acmicpc.net/problem/18719) 

### 성능 요약

메모리: 406288 KB, 시간: 3528 ms

### 분류

비트마스킹(bitmask), 다이나믹 프로그래밍(dp), 비트필드를 이용한 다이나믹 프로그래밍(dp_bitfield), undefined(dp_sum_over_subsets), 뤼카 정리(lucas), 수학(math), 정수론(number_theory)

### 문제 설명

<p>There are people that wont be happy with solving a problem, unless the actual task is obscured by an elaborate and somewhat unnecessary story. If you are one of these people, then this problem is NOT for you.</p>

<p>You are given a sequence of non-negative integers \(a_1, a_2, . . . , a_n\). You need to find the number of pairs \((i, j)\) such that \(1 \le i, j \le n\) and \(\binom{a_i}{a_j}\)is odd.</p>

<p>Note that \(\binom{n}{k}\) is the number of ways, disregarding order, that \(k\) objects can be chosen from among n objects. In particular, if \(n < k\) then \(\binom{n}{k} = 0\).</p>

### 입력 

 <p>The first line of input contains the number of test cases \(z\) (\(1 \le z \le 10\)). The descriptions of the test cases follow.</p>

<p>The first line of each test case contains the number of elements in the sequence \(n\) (\(1 \le n \le 10^6\)).</p>

<p>The second line contains \(n\) integers \(a_i\) (\(1 \le a_i \le 10^6\)) – the elements of the sequence.</p>

### 출력 

 <p>For each test case, output a single line which contains a single integer – the answer for the problem.</p>

