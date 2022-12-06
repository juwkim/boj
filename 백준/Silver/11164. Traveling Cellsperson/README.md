# [Silver V] Traveling Cellsperson - 11164 

[문제 링크](https://www.acmicpc.net/problem/11164) 

### 성능 요약

메모리: 2020 KB, 시간: 0 ms

### 분류

애드 혹(ad_hoc)

### 문제 설명

<p>You have solved every problem from Project Euler in your head. Now it is time for a problem you might have heard of, namely The Traveling Salesperson, whose decision version is NP-complete. We consider the Traveling Salesperson problem in a 2D rectangular grid where every cell can be reached from their neighboring cells (up, down, left and right) and you can visit a cell as many times as you like (though, most of the cells aren’t that interesting, so you might prefer not to visit them a lot).</p>

### 입력 

 <p>The first line of the input consists of a single integer T, the number of test cases. Then follow two integers X and Y , marking the width and height of the grid, respectively. Then follow Y lines with X characters, where the character ’C’ is a cell and the character ’S’ is the starting point.</p>

<ul>
	<li>0 < T ≤ 50</li>
	<li>0 < X ≤ 100</li>
	<li>0 < Y ≤ 100</li>
	<li>All characters in a test case are ’C’, except for exactly one, which is ’S’.</li>
</ul>

### 출력 

 <p>For each test case, output the minimum number of steps required to make a full roundtrip of the grid, starting and ending at S, and visiting each cell at least once.</p>

<p>Since you realize that this won’t lead anywhere, finish off the output with “LOL” (without quotes) on a line of its own (one per run, not per test case).</p>

