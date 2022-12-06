# [Bronze II] Moderate Pace - 20341 

[문제 링크](https://www.acmicpc.net/problem/20341) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation)

### 문제 설명

<p>An ultra-marathon is a race that takes place over an uncomfortably long distance and time, typically lasting for five hours or more. You are part of a group of three ultra-marathon runners looking to place in this year's Great South-to-North run from Plymouth to Aberdeen.</p>

<p>You have a set number of days until the next race to train. You will all train together, as training alone can be dangerous. As everyone has their own schedule in mind for how many kilometres to run per day, this will not be easy, you will have to compromise.</p>

<p>The fairest option is to look at each day individually, examine the three options for how far to run, and to take the median one. That is to say, the option taken for each day should be one that is not be greater or lesser than both of the other possibilities at the same time.</p>

### 입력 

 <ul>
	<li>A line with the integer $n$ ($1\leq n\leq1000$), the number of days of training.</li>
	<li>A line with $n$ integers $k_{1,\ldots,n}$ ($0\leq k \leq 10^6$), your ideal daily distances.</li>
	<li>A line with $n$ integers $a_{1,\ldots,n}$ ($0\leq a \leq 10^6$), your first colleague's ideal daily distances.</li>
	<li>A line with $n$ integers $b_{1,\ldots,n}$ ($0\leq b \leq 10^6$), your second colleague's ideal daily distances.</li>
</ul>

### 출력 

 <p>Output a plan for the $n$ days as $n$ integers, where the distance for every day corresponds to the median of choices for that day.</p>

