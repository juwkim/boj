# [Bronze I] He is offside! - 5738 

[문제 링크](https://www.acmicpc.net/problem/5738) 

### 성능 요약

메모리: 30840 KB, 시간: 100 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>Hemisphere Network is the largest television network in Tumbolia, a small country located east of South America (or south of East America). The most popular sport in Tumbolia, unsurprisingly, is soccer; many games are broadcast every week in Tumbolia.</p>

<p>Hemisphere Network receives many requests to replay dubious plays; usually, these happen when a player is deemed to be offside by the referee. An attacking player is offside if he is nearer to his opponents’ goal line than the second last opponent. A player is not offside if</p>

<ul>
	<li>he is level with the second last opponent or</li>
	<li>he is level with the last two opponents.</li>
</ul>

<p>Through the use of computer graphics technology, Hemisphere Network can take an image of the field and determine the distances of the players to the defending team’s goal line, but they still need a program that, given these distances, decides whether a player is offside.</p>

### 입력 

 <p>The input file contains several test cases. The first line of each test case contains two integers A and D separated by a single space indicating, respectively, the number of attacking and defending players involved in the play (2 ≤ A, D ≤ 11). The next line contains A integers B<sub>i</sub> separated by single spaces, indicating the distances of the attacking players to the goal line (1 ≤ B<sub>i</sub> ≤ 10<sup>4</sup>). The next line contains D integers C<sub>j</sub> separated by single spaces, indicating the distances of the defending players to the goal line (1 ≤ C<sub>j</sub> ≤ 10<sup>4</sup>).</p>

<p>The end of input is indicated by a line containing only two zeros, separated by a single space.</p>

<p>The input must be read from standard input.</p>

### 출력 

 <p>For each test case in the input print a line containing a single character: “Y” (uppercase) if there is an attacking player offside, and “N” (uppercase) otherwise.</p>

<p>The output must be written to standard output.</p>

