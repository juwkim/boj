# [Silver V] Crtanje - 20200 

[문제 링크](https://www.acmicpc.net/problem/20200) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

구현(implementation)

### 문제 설명

<p>Josip used to code in Logo. He loved to draw pictures, but those days are sadly over. Nostalgic, he decided to draw a line that represents the net worth of his company over a period of n days.</p>

<p>For each of the n days, he knows if the net worth of his company increased by one unit (represented by '+'), decreased by one unit (represented by '-'), or remained the same (represented by '=') during that day. Before the first day, the net worth was equal to zero.</p>

<p>Josip will draw the line in a big infinite matrix of characters. Indices of matrix rows grow upwards, and indices of columns grow to the right. For the i-th day he will draw some character in the i-th column. The character and the index of the row are decided by the following rules:</p>

<ul>
	<li>If the net worth increased during the i-th day, he will draw '/' in the row with index equal to the net worth at the beginning of the day.</li>
	<li>If the net worth decreased during the i-th day, he will draw '\' in the row with index equal to the net worth at the end of the day.</li>
	<li>If the net worth didn’t change during the i-th day, he will draw '_' in the row with index equal to the net worth during the day.</li>
</ul>

<p>All other cells are filled with '.'.</p>

<p>Your task is to output the minimal matrix that contains the whole line, i.e. contains all characters '/', '\' and '_' that Josip drew.</p>

### 입력 

 <p>The first line contains an integer n (1 ≤ n ≤ 100), the number of days.</p>

<p>The second line contains a string of n characters '+', '-' and '=' that represents how the company’s net worth changed over the given period.</p>

### 출력 

 <p>Output the described matrix.</p>

