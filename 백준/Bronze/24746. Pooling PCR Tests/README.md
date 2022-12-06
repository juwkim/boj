# [Bronze I] Pooling PCR Tests - 24746 

[문제 링크](https://www.acmicpc.net/problem/24746) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>The Polymerase chain reaction (PCR) test is a test for COVID which repeatedly copies a DNA sample and then tests for the presence of COVID specific DNA segments. This can take time and the required reagents may be limited. One suggestion for improving throughput is pooling of samples.</p>

<p>The idea is to combine N samples and run the PCR test on the combined sample. If the test is negative then no further test is required. If the test is positive, all N people must be retested individually. If the probability of a positive test is low, this will significantly reduce the number of tests required.</p>

<p>Write a program which takes as input the probability, p, that a single person tests positive and outputs the optimum number of samples, N, to combine.</p>

<p>If P is the probability that all N people test negative then the expected number of tests, E(T), required is:</p>

<p style="text-align: center;">E(T) = 1*P + N*(1 – P)</p>

<p>Choose N to minimize E(T) / N.</p>

<p>For example, if N is 2 and p is 0.5, P is 0.25 and E(T) = 0.25 + 2*0.75 = 1.75 which is only slightly less than N.</p>

<p>In order to be sure that the sample from each person is sufficient, N must be no more than 16.</p>

### 입력 

 <p>Input consists of a single line containing a single decimal floating point value p, (0 < p < 1), the probability that a single person tests positive for Covid.</p>

### 출력 

 <p>Output is a single line containing a single decimal integer. If E(T) ≥ N for all N, output the value 1. Otherwise, the value is N, 2 ≤ N ≤ 16, which minimizes E(T) / N.</p>

