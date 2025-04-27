# [Silver I] Expired License - 16066 

[문제 링크](https://www.acmicpc.net/problem/16066) 

### 성능 요약

메모리: 116996 KB, 시간: 364 ms

### 분류

유클리드 호제법, 수학, 정수론, 소수 판정

### 제출 일자

2025년 4월 27일 18:21:41

### 문제 설명

<p>Paul is an extremely gifted computer scientist who just completed his master’s degree at a prestigious German university. Now he would like to culminate his academic career in a PhD. The problem is that there are so many great universities out there that it is hard for him to pick the best. Because some application deadlines are coming up soon, Paul’s only way to procrastinate his decision is by simply applying to all of them.</p>

<p>Most applications require Paul to attach a portrait photo. However, it seems like there does not exist an international standard for the aspect ratio of these kinds of photos. While most European universities ask Paul to send a photograph with aspect ratio 4.5 by 6, some Asian countries discard the applications immediately if the photo does not have an aspect ratio of 7.14 by 11.22, precisely.</p>

<p>As Paul has never been interested in photo editing, he never had a reason to spend a lot of money on proper software. He downloaded a free trial version some months ago, but that version has already expired and now only works with some funny restrictions. The cropping tool, for example, no longer accepts arbitrary numbers for setting the aspect ratio, but only primes. This makes Paul wonder whether the desired aspect ratios can even be properly expressed by two prime numbers. Of course, in case this is possible, he would also like to know the primes he has to enter.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>one line with an integer n (1 ≤ n ≤ 10<sup>5</sup>), the number of applications Paul has to file;</li>
	<li>n lines, each with two real numbers a and b (0 < a, b < 100), where a × b is the desired aspect ratio of one application.</li>
</ul>

<p>All real numbers are given with at most 5 decimal places after the decimal point.</p>

### 출력 

 <p>For each application, if it is possible to represent the desired aspect ratio by two prime numbers p and q, output one line with p and q. Otherwise, output impossible. If multiple solutions exist, output the one minimizing p + q.</p>

