# [Silver III] Square - 13385 

[문제 링크](https://www.acmicpc.net/problem/13385) 

### 성능 요약

메모리: 109240 KB, 시간: 112 ms

### 분류

임의 정밀도 / 큰 수 연산, 다이나믹 프로그래밍, 수학

### 제출 일자

2024년 2월 14일 06:45:59

### 문제 설명

<p>It was the first time that our government organized the 2015 ACM PCPC (Paper Cutting Programming Contest) in Bangkok last week. The objective of this event is to create a relationship between computer students in ASEAN. More than thousands of students applied to this PCPC. Eventually, there were M matches running on the final round. This is the regulation of the contest:</p>

<ul>
	<li>Match between Two Teams</li>
	<li>Material: One piece of rectangle paper with dimension L” × W”. </li>
	<li>Mission of each player:
	<ul>
		<li>Cut the paper into possible largest squares and pass the remainder to the next player. For each of the rounds, player must cut 1 or more squares, all squares must have the same size. The condition for the remainder is to be a single piece of rectangle.</li>
	</ul>
	</li>
	<li>The winner: the player who cuts the paper without the remainder. </li>
	<li>The record of the game is W L r a<sub>1</sub> a<sub>2</sub> ... a<sub>r</sub></li>
	<li>Where L : length of the original rectangle paper
	<ul>
		<li>W : width of the original rectangle paper </li>
		<li>a<sub>i</sub> : the number of squares in ith-turn.</li>
		<li>r : the number of turns for this game</li>
	</ul>
	</li>
</ul>

<p>Example:</p>

<ul>
	<li>A square paper size 5” × 2”.</li>
	<li>The first player can cut 2 squares of 2” × 2”. The remainder is therefore a rectangle 2” × 1”. </li>
	<li>The second player can cut 2 squares with 1” × 1” without the remainder.</li>
	<li>The record of this game is 5 2 2 2 2</li>
</ul>

<p>Because of the error of the computer system, the memory is magically disappeared. Only two first numbers of each record cannot be read. Our mission is to find only the first number. In the case that there are more than one possible value, we take only the smallest length.</p>

### 입력 

 <p>The input contains M + 1 lines</p>

<ul>
	<li>The first line contains one integer M </li>
	<li>The M next lines contain r+1 integers
	<ul>
		<li>The first integer is r</li>
		<li>The next r integers are ai where 1 ≤ I ≤ r</li>
	</ul>
	</li>
</ul>

<p>Limitation:</p>

<ul>
	<li>1 <= M <= 20</li>
	<li>1 <= W, L <= 10<sup>100</sup> 1 <= r <= 50</li>
	<li>1 <= a<sub>i</sub> <= 100</li>
</ul>

### 출력 

 <p>The output contains M lines where each line contains one integer L (the longer size of the rectangle).</p>

