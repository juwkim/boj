# [Bronze I] Flip Flow - 20906 

[문제 링크](https://www.acmicpc.net/problem/20906) 

### 성능 요약

메모리: 28776 KB, 시간: 72 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>For over 600 years, the hourglass has been a well-known timekeeping instrument. An hourglass consists of two glass flasks arranged one above the other which are connected by a narrow channel. Inside the hourglass there is sand which slowly flows from the upper to the lower flask. Hourglasses are typically symmetrical so that the sand always takes the same amount of time to run through, regardless of orientation. For the purposes of this problem, we also assume that the flow rate of the sand is a known constant and does not depend on the amount or distribution of sand in the upper half.</p>

<p>Your friend Helen was bored and has been playing around with her hourglass. At time $0$, all the sand was in the lower half. Helen flipped the hourglass over several times and recorded all the moments at which she did so. How many seconds does she need to wait from the current time until all the sand is back in the lower half?</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with three integers $t$, $s$ and $n$, where</li>
	<li>$t$ ($1 \le t \le 10^6$) is the current time;</li>
	<li>$s$ ($1 \le s \le 10^6$) is the amount of sand in the hourglass, in grams;</li>
	<li>$n$ ($1 \le n \le 1\,000$) is the number of times the hourglass was flipped.</li>
	<li>One line with $n$ integers $a_1,\dots,a_n$ ($0 < a_1 < \dots < a_n < t$), the times at which the hourglass was flipped.</li>
</ul>

<p>All times are given in seconds. You may assume that the sand flows from the top to the bottom at a constant rate of $1$ gram per second.</p>

### 출력 

 <p>Output the time in seconds needed for the hourglass to run out starting from time $t$.</p>

