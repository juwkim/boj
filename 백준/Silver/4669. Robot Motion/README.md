# [Silver I] Robot Motion - 4669 

[문제 링크](https://www.acmicpc.net/problem/4669) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 5월 12일 02:39:29

### 문제 설명

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/4669/fig1trans-2.gif"></p>

<p>A robot has been programmed to follow the instructions in its path. Instructions for the next direction the robot is to move are laid down in a grid. The possible instructions are</p>

<ul>
	<li>N north (up the page)</li>
	<li>S south (down the page)</li>
	<li>E east (to the right on the page)</li>
	<li>W west (to the left on the page)</li>
</ul>

<p>For example, suppose the robot starts on the north (top) side of Grid 1 and starts south (down). The path the robot follows is shown. The robot goes through 10 instructions in the grid before leaving the grid.</p>

<p>Compare what happens in Grid 2: the robot goes through 3 instructions only once, and then starts a loop through 8 instructions, and never exits.</p>

<p>You are to write a program that determines how long it takes a robot to get out of the grid or how the robot loops around.</p>

### 입력 

 <p>There will be one or more grids for robots to navigate. The data for each is in the following form. On the first line are three integers separated by blanks: the number of rows in the grid, the number of columns in the grid, and the number of the column in which the robot enters from the north. The possible entry columns are numbered starting with one at the left. Then come the rows of the direction instructions. Each grid will have at least one and at most 10 rows and columns of instructions. The lines of instructions contain only the characters N, S, E, or W with no blanks. The end of input is indicated by a row containing 0 0 0.</p>

### 출력 

 <p>For each grid in the input there is one line of output. Either the robot follows a certain number of instructions and exits the grid on any one the four sides or else the robot follows the instructions on a certain number of locations once, and then the instructions on some number of locations repeatedly. The sample input below corresponds to the two grids above and illustrates the two forms of output. The word "step" is always immediately followed by "(s)" whether or not the number before it is 1.</p>

