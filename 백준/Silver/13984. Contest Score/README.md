# [Silver II] Contest Score - 13984 

[문제 링크](https://www.acmicpc.net/problem/13984) 

### 성능 요약

메모리: 110576 KB, 시간: 100 ms

### 분류

자료 구조, 구현, 우선순위 큐, 시뮬레이션

### 제출 일자

2024년 12월 17일 04:19:45

### 문제 설명

<p>You are participating in the Association for Computing Machinery’s Intercollegiate Programming Competition (ACM ICPC). You must complete a set of n problems. Since you are an experienced problem solver, you can read a problem and accurately estimate how long it will take to solve it, in a negligible amount of time. But you can only keep the details from k problems straight at any given time.</p>

<p>Let t<sub>i</sub> be the time it will take to solve the ith problem. Your strategy for the contest is as follows:</p>

<ol>
	<li>Read the first k problems.</li>
	<li>Choose a problem that you have read that will take the shortest time to solve (if there are ties, choose any of them arbitrarily).</li>
	<li>Solve the problem, and read the next unread problem (if there is any).</li>
	<li>If there are still unsolved problems, go back to step 2.</li>
</ol>

<p>You want to calculate your total penalty time for the contest. Your penalty time for the contest is defined by the sum of submission times for all the problems. Given the ordering of problems in the contest, compute the penalty time of your strategy.</p>

### 입력 

 <p>The first line of input contains two space-separated integers n and k (1 ≤ k ≤ n ≤ 300).</p>

<p>The ith line of the next n lines contains a single integer t<sub>i</sub> (1 ≤ t<sub>i</sub> ≤ 1,000,000).</p>

### 출력 

 <p>Print, on a single line, a single integer repesenting the total penalty time.</p>

