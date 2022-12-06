# [Silver V] Go Latin - 16360 

[문제 링크](https://www.acmicpc.net/problem/16360) 

### 성능 요약

메모리: 29200 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>There are English words that you want to translate them into pseudo-Latin. To change an English word into pseudo-Latin word, you simply change the end of the English word like the following table.</p>

<table class="table table table-bordered" style="width: 25%;">
	<thead>
		<tr>
			<th style="text-align:center;">English</th>
			<th style="text-align:center;">pseudo-Latin</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align:center;">-a</td>
			<td style="text-align:center;">-as</td>
		</tr>
		<tr>
			<td style="text-align:center;">-i, -y</td>
			<td style="text-align:center;">-ios</td>
		</tr>
		<tr>
			<td style="text-align:center;">-l</td>
			<td style="text-align:center;">-les</td>
		</tr>
		<tr>
			<td style="text-align:center;">-n, -ne</td>
			<td style="text-align:center;">-anes</td>
		</tr>
		<tr>
			<td style="text-align:center;">-o</td>
			<td style="text-align:center;">-os</td>
		</tr>
		<tr>
			<td style="text-align:center;">-r</td>
			<td style="text-align:center;">-res</td>
		</tr>
		<tr>
			<td style="text-align:center;">-t</td>
			<td style="text-align:center;">-tas</td>
		</tr>
		<tr>
			<td style="text-align:center;">-u</td>
			<td style="text-align:center;">-us</td>
		</tr>
		<tr>
			<td style="text-align:center;">-v</td>
			<td style="text-align:center;">-ves</td>
		</tr>
		<tr>
			<td style="text-align:center;">-w</td>
			<td style="text-align:center;">-was</td>
		</tr>
	</tbody>
</table>

<p>If a word is not ended as it stated in the table, put ‘-us’ at the end of the word. For example, a word “cup” is translated into “cupus” and a word “water” is translated into “wateres”.</p>

<p>Write a program that translates English words into pseudo-Latin words.</p>

### 입력 

 <p>Your program is to read from standard input. The input starts with a line containing an integer, <em>n</em> (1 ≤ <em>n</em> ≤ 20), where <em>n</em> is the number of English words. In the following <em>n</em> lines, each line contains an English word. Words use only lowercase alphabet letters and each word contains at least 3 and at most 30 letters.</p>

### 출력 

 <p>Your program is to write to standard output. For an English word, print exactly one pseudo-Latin word in a line.</p>

