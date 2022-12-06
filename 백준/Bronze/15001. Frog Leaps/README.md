# [Bronze III] Frog Leaps - 15001 

[문제 링크](https://www.acmicpc.net/problem/15001) 

### 성능 요약

메모리: 144128 KB, 시간: 620 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>It is a little known secret that frogs also like to participate in the BAPC. However, to reach Amsterdam they will need to cross lots of rivers. Fortunately, the frog is in good condition and can jump as far as he wants to go. However, jumping a distance of i meters costs the frog i<sup>2</sup> units of energy. The only way the frog can reach Amsterdam is by jumping from stop to stop.</p>

<p>The frog, who is of course lazy, would like to minimize the amount of energy he needs to spend. Can you calculate the minimum amount of energy he needs to spend to reach Amsterdam?</p>

### 입력 

 <ul>
	<li>On the first line one integer 2 ≤ n ≤ 10<sup>6</sup>, the total number of stops.</li>
	<li>Then follow n lines with one integer x<sub>i</sub>, the position of the ith stop in meters, with x<sub>i</sub> < x<sub>i+1</sub>. Here 0 ≤ x<sub>i</sub> ≤ 10<sup>6</sup>. The frog’s start location is at the first stop x<sub>0</sub>. Amsterdam is located at the last stop x<sub>n−1</sub>.</li>
</ul>

### 출력 

 <ul>
	<li>Print a single integer indicating the minimum number of units of energy the frogs needs to travel to Amsterdam.</li>
</ul>

