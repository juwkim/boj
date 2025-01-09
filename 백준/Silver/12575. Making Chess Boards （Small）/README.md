# [Silver II] Making Chess Boards (Small) - 12575 

[문제 링크](https://www.acmicpc.net/problem/12575) 

### 성능 요약

메모리: 115432 KB, 시간: 248 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 1월 10일 06:52:49

### 문제 설명

<p>The chess board industry has fallen on hard times and needs your help. It is a little-known fact that chess boards are made from the bark of the extremely rare Croatian Chess Board tree, (<em>Biggus Mobydiccus</em>). The bark of that tree is stripped and unwrapped into a huge rectangular sheet of chess board material. The rectangle is a grid of black and white squares.</p>

<p>Your task is to make as many large square chess boards as possible. A chess board is a piece of the bark that is a square, with sides parallel to the sides of the bark rectangle, with cells colored in the pattern of a chess board (no two cells of the same color can share an edge).</p>

<p>Each time you cut out a chess board, you must choose the largest possible chess board left in the sheet. If there are several such boards, pick the topmost one. If there is still a tie, pick the leftmost one. Continue cutting out chess boards until there is no bark left. You may need to go as far as cutting out 1-by-1 mini chess boards.</p>

<p>Here is an example showing the bark of a Chess Board tree and the first few chess boards that will be cut out of it.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/12575/images-28.png"></p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> test cases follow. Each one starts with a line containing the dimensions of the bark grid, <strong>M</strong> and <strong>N</strong>. <strong>N</strong> will always be a multiple of 4. The next <strong>M</strong> lines will each contain an (<strong>N</strong>/4)-character hexadecimal integer, representing a row of the bark grid. The binary representation of these integers will give you a strings of <strong>N</strong> bits, one for each row. Zeros represent black squares; ones represent white squares of the grid. The rows are given in the input from top to bottom. In each row, the most-significant bit of the hexadecimal integer corresponds to the leftmost cell in that row.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100;</li>
	<li><strong>N</strong> will be divisible by 4;</li>
	<li>Each hexadecimal integer will contain exactly <strong>N</strong>/4 characters.</li>
	<li>Only the characters 0-9 and A-F will be used.</li>
	<li>1 ≤ <strong>M</strong> ≤ 32;</li>
	<li>1 ≤ <strong>N</strong> ≤ 32.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: <strong>K</strong>", where x is the case number (starting from 1) and <strong>K</strong> is the number of different chess board sizes that you can cut out by following the procedure described above. The next <strong>K</strong> lines should contain two integers each -- the size of the chess board (from largest to smallest) and the number of chess boards of that size that you can cut out.</p>

