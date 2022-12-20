# [Silver IV] Falling Apples - 13732 

[문제 링크](https://www.acmicpc.net/problem/13732) 

### 성능 요약

메모리: 139812 KB, 시간: 248 ms

### 분류

구현(implementation), 두 포인터(two_pointer)

### 문제 설명

<p>You have a 2D rectangular grid. Each grid cell contains either an apple, an obstacle, or is empty. Empty cells are denoted as ’.’, apples as ’a’, and obstacles as ’#’. You are to implement a simulation of gravity, based on the following rules:</p>

<ul>
	<li>The obstacles do not move.</li>
	<li>Whenever there is an empty cell immediately below an apple, the apple moves into the empty cell.</li>
</ul>

<p>Print out the final configuration of the board after all apples reach their final locations. Merely iterating the gravity rule, a step at a time, will likely take too long on large datasets.</p>

### 입력 

 <p>The input begins with a line containing integers R and C, designating the number of rows and columns of the grid, such that 1 ≤ R ≤ 50 000 and 1 ≤ C ≤ 10. The first line is followed by R additional lines, each designating a row of the grid, from top to bottom. Each line has C characters, each of which is either ’.’, ’a’, or ’#’.</p>

### 출력 

 <p>Output R grid lines displaying the final state. </p>

