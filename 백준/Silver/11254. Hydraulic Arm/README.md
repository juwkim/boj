# [Silver IV] Hydraulic Arm - 11254 

[문제 링크](https://www.acmicpc.net/problem/11254) 

### 성능 요약

메모리: 115268 KB, 시간: 168 ms

### 분류

자료 구조(data_structures), 스택(stack)

### 문제 설명

<p>Your chicken farm would like to send eggs to the market. Each package has different sizes, so you need to take care how you pack them. You decide to pack the egg packages vertically and sort them from the shortest to tallest.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11254/1.png" style="height:405px; width:483px"></p>

<p>Your farm uses the hydraulic arm system and the arm can do one of these three actions at a time.</p>

<ol>
	<li>Move the right-most egg package from the left conveyor belt and place at the left-most position of the upper shelf</li>
	<li>Move the left-most egg package on the upper shelf to the left-most position of the right conveyor belt.</li>
	<li>Move the right-most egg package from the left conveyor belt to the left-most position of the right conveyor belt.</li>
</ol>

<p>For the speed of the process, the arm cannot move any package on the right conveyor belt.</p>

<p>Write the program to check if the given position of the package can be process to the desire position, all package on the right conveyor belt, sorted from smallest on the right and tallest on the left.</p>

### 입력 

 <p>The first lint contain integer T (1 ≤ T ≤ 20), the number of testcases. In each testcase there will be as follow.</p>

<p>The first line contains integer N (1 ≤ N ≤ 10,000), the number of egg packages.</p>

<p>Next line contains positive integer a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, …, a<sub>N</sub> (1 ≤ a<sub>i</sub> ≤ N), the height of the egg packages from left to right of the left conveyor belt. There will not be two packages that have the same height.</p>

### 출력 

 <p>For each testcase, print “yes” or “no” on the following condition.</p>

<ul>
	<li>“yes” if there is a way to process the given position to the desire position</li>
	<li>“no” if you cannot find a way to do it.
	<ul>
		<li>(please notice that “yes” and “no” is in lowercase.)</li>
	</ul>
	</li>
</ul>

