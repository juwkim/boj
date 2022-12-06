# [Bronze II] Ballpark Estimate - 17795 

[문제 링크](https://www.acmicpc.net/problem/17795) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math), 문자열(string)

### 문제 설명

<p>Giving the right level of detail is an important skill for efficient communication. Sometimes, only the high-level message matters.</p>

<p>For example, whenever a person asks for a number, often they just want an estimate. If the value is in the millions, they do not need to know the precise number of hundreds and tens. Likewise, if the value is in the billions, they do not necessarily care about little things like millions.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 317px; height: 165px;"></p>

<p style="text-align: center;">Figure B.1: Illustration of ballpark figures versus actual figures, as a log chart.</p>

<p>Given a (possibly very large) number, print its numerically closest representation that has only one digit other than trailing zeroes.</p>

<p>The closeness of the representation r of a number n is defined by abs(r − n).</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>one line with the positive integer n (1 ≤ n ≤ 10<sup>18</sup>).</li>
</ul>

### 출력 

 <p>Output the closest number to n with exactly one significant (non-zero) figure. If there are two equally-close answers, print the larger one.</p>

