# [Bronze I] On-Screen Keyboard - 17578 

[문제 링크](https://www.acmicpc.net/problem/17578) 

### 성능 요약

메모리: 28776 KB, 시간: 232 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p>You are to input a string with an OSK (on-screen keyboard). A remote control with five buttons, four arrows and an OK (Fig. B-1), is used for the OSK. Find the minimum number of button presses required to input a given string with the given OSK.</p>

<p style="text-align: center;"><img alt="" src=""></p>

<p style="text-align: center;">Fig. B-1 Remote control</p>

<p style="text-align: center;"><img alt="" src=""></p>

<p style="text-align: center;">Fig. B-2 An on-screen keyboard</p>

<table class="table table-bordered table-center-70">
	<thead>
		<tr>
			<th>Character to input</th>
			<th>Move of highlighted cells</th>
			<th>Button presses</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center"><code>I</code></td>
			<td><img alt="" src=""></td>
			<td>→,→,→,→,→,→,→,→,OK (9 presses)</td>
		</tr>
		<tr>
			<td align="center"><code>C</code></td>
			<td><img alt="" src=""></td>
			<td>←,←,←,←,←,←,OK (7 presses)</td>
		</tr>
		<tr>
			<td align="center"><code>P</code></td>
			<td><img alt="" src=""></td>
			<td>↓,→,→,→,→,OK (6 presses)</td>
		</tr>
		<tr>
			<td align="center"><code>C</code></td>
			<td><img alt="" src=""></td>
			<td>↑,←,←,←,←,OK (6 presses)</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;">Fig. B-3 The minimum steps to input “<code>ICPC</code>” with the OSK in Fig. B-2</p>

<p>The OSK has cells arranged in a grid, each of which has a character in it or is empty. No two of the cells have the same character.</p>

<p>One of the cells of the OSK is highlighted, and pressing the OK button will input the character in that cell, if the cell is not empty.</p>

<p>Initially, the cell at the top-left corner is highlighted. Pressing one of the arrow buttons will change the highlighted cell to one of the adjacent cells in the direction of the arrow. When the highlighted cell is on an edge of the OSK, pushing the arrow button with the direction to go out of the edge will have no effect.</p>

<p>For example, using the OSK with its arrangement shown in Fig. B-2, a string “<code>ICPC</code>” can be input with 28 button presses as shown in Fig. B-3, which is the minimum number of presses.</p>

<p>Characters in cells of the OSKs are any of a lowercase letter (‘<code>a</code>’, ‘<code>b</code>’, ..., ‘<code>z</code>’), an uppercase letter (‘<code>A</code>’, ‘<code>B</code>’, ..., ‘<code>Z</code>’), a digit (‘<code>0</code>’, ‘<code>1</code>’, ..., ‘<code>9</code>’), a comma (‘<code>,</code>’), a hyphen (‘<code>-</code>’), a dot (‘<code>.</code>’), a slash (‘<code>/</code>’), a colon (‘<code>:</code>’), a semicolon (‘<code>;</code>’), or an at sign (‘<code>@</code>’).</p>

### 입력 

 <p>The input consists of at most 100 datasets, each in the following format.</p>

<pre><i>h w</i>
<i>r</i><sub>1</sub>
...
<i>r</i><sub>h</sub>
<i>s</i>
</pre>

<p>The two integers <i>h</i> and <i>w</i> in the first line are the height and the width of the OSK, respectively. They are separated by a space, and satisfy 1 ≤ <i>h</i> ≤ 50 and 1 ≤ <i>w</i> ≤ 50.</p>

<p>Each of the next <i>h</i> lines gives a row of the OSK. The <i>i</i>-th row, <i>r</i><sub>i</sub> is a string of length <i>w</i>. The characters in the string corresponds to the characters in the cells of the <i>i</i>-th row of the OSK or an underscore (‘<code>_</code>’) indicating an empty cell, from left to right.</p>

<p>The given OSK satisfies the conditions stated above.</p>

<p>The next line is a string <i>s</i> to be input. Its length is between 1 and 1000, inclusive. All the characters in <i>s</i> appear in the given OSK. Note that <i>s</i> does not contain underscores.</p>

<p>The end of the input is indicated by a line containing two zeros.</p>

### 출력 

 <p>For each dataset, output a single line containing an integer indicating the minimum number of button presses required to input the given string with the given OSK.</p>

