# [Silver I] Automatic Control Machine - 18148 

[문제 링크](https://www.acmicpc.net/problem/18148) 

### 성능 요약

메모리: 110904 KB, 시간: 200 ms

### 분류

비트마스킹, 브루트포스 알고리즘

### 제출 일자

2025년 5월 4일 04:19:33

### 문제 설명

<p>The company has produced an Automatic Control Machine (ACM for short) that is very popular. Due to its complete and powerful features, the company is preparing to redesign after years of sales. The new version of the ACM is still subject to a number of tests to determine the reliability of the product before it goes on the market. Because there are so many features, each test dataset can only detect several of them. Of course, the product must be available after all features have been tested. Since each test has time and material costs, they like to do the test as less as possible. Assume that running each test dataset costs the same, your job is finding the minimum number of test datasets that can cover the test of all features. For example, if there are 5 features that need to be tested, and there are 6 test datasets each can cover the features as follows:</p>

<ul>
	<li>Test dataset a: 1</li>
	<li>Test dataset b: 2, 5</li>
	<li>Test dataset c: 2, 3, 4</li>
	<li>Test dataset d: 1, 3, 5</li>
	<li>Test dataset e: 1, 3, 4</li>
	<li>Test dataset f: 3, 5</li>
</ul>

<p>Although {a, b, c} may do the job, but {c, d} will do the job better in the way of saving time<br>
and money.</p>

### 입력 

 <p>The first line of the input file contains one positive integer T representing the number of machines. For each machine, the first line consists of two integers n and m representing the features of machine that has to be tested and the number of test datasets. It follows by m lines, each line has a binary string of length n, showing whether the features can be detected by the test dataset or not (1 means yes, 0 means no).</p>

### 출력 

 <p>Output T lines. Each of them should be the minimum number of test dataset needed to test all features for that machine. If it is not possible to test all functions for the machine, output -1.</p>

