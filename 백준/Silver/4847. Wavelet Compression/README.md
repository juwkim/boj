# [Silver III] Wavelet Compression - 4847 

[문제 링크](https://www.acmicpc.net/problem/4847) 

### 성능 요약

메모리: 113228 KB, 시간: 680 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2024년 4월 21일 14:08:09

### 문제 설명

<p>The discrete wavelet transform is a popular tool for signal compression. In this problem, your job is to write a program to decompress a one−dimensional signal (a list of integers) that has been compressed by a simple wavelet transform.</p>

<p>To understand how this simple wavelet transform works, suppose that we have a list of an even number of integers. We compute the sum and difference of each pair of consecutive samples, resulting in two lists of sums and differences each having half the original length. Formally, if the original samples are</p>

<pre>a(1),..., a(n)</pre>

<p>the i−th sum s(i) and difference d(i) are computed as:</p>

<pre>for i = 1,...,n/2:
  s(i) = a(2*i−1) + a(2*i)
  d(i) = a(2*i−1) − a(2*i)</pre>

<p>This is then rearranged to give the transformed signal by first listing the sums and then the differences. For example, if the input signal is:</p>

<pre>5, 2, 3, 2, 5, 7, 9, 6</pre>

<p>Then the sum and difference signals are:</p>

<pre>s(i) = 7, 5, 12, 15
d(i) = 3, 1, −2, 3</pre>

<p>Thus, the transformed signal is:</p>

<pre>7, 5, 12, 15, 3, 1, −2, 3</pre>

<p>The same process is applied recursively to the first half of the transformed signal, treating s(i) as the input signal, until the length of the input signal is 1. In the example above, the final transformed signal is:</p>

<pre>39, −15, 2, −3, 3, 1, −2, 3</pre>

<p>It is assumed that the length of the original input is a power of 2, and the input signal consists of integers between 0 and 255 (inclusive) only.</p>

### 입력 

 <p>The input consists of a number of cases. Each case is specified on a line, starting with an integer N (1 <= N <= 256) indicating the number of samples. The next N integers are the transformed samples. The end of input is indicated by a case in which N = 0.</p>

### 출력 

 <p>For each test case, output the original samples on a single line, separated by a single space.</p>

