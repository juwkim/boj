# [Silver V] Chaos - 13047 

[문제 링크](https://www.acmicpc.net/problem/13047) 

### 성능 요약

메모리: 127376 KB, 시간: 164 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>Setting up dominoes and watching them fall toppling each other has become too boring for Doctor Brown. So he has invented the new, more mathematical, time waste.</p>

<p>The board contains n integers. Doc repeatedly performs the following moves:</p>

<ul>
	<li>He chooses three numbers a, b and c written at the board and erases them.</li>
	<li>He chooses two numbers from the triple a, b and c and calculates their average value, rounding it down if necessary, getting the number d.</li>
	<li>He writes the number d to the board two times.</li>
</ul>

<p>For example, if the board contains 1, 2 and 4, after erasing them from the board, Doc can write two 1-s (average of 1 and 2 rounded down), two 2-s (average of 1 and 4 rounded down) or two 3-s (average of 2 and 4) on the board. The process is over when there are two numbers left on the board. Clearly these two numbers are the same.</p>

<p>Once Marty was watching Doc's actions, and it really looked as some random sequence of moves. But it was not, Doc claims that he has made his moves in such way, that the numbers left on the board are maximal possible. Marty doesn't completely trust Doc. He has remembered the initial numbers on the board, and wants you to find the maximal possible value of the two numbers left on the board after performing the sequence of moves.</p>

### 입력 

 <p>The first line contains one integer n (3 ≤ n ≤ 10<sup>5</sup>) — the number of integers written on the board.</p>

<p>The second line contains n integers a<sub>i</sub> (1 ≤ a<sub>i</sub> ≤ 10<sup>9</sup>) — the numbers on the board.</p>

### 출력 

 <p>Output one integer — the maximal possible value of the two numbers left on the board in the end of Doc's actions.</p>

<p> </p>

