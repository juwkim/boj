# [Bronze I] T9 - 3281 

[문제 링크](https://www.acmicpc.net/problem/3281) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>T9 is a system developed to satisfy rapidly growing needs for quick sending textual messages (SMS) using mobile phones. It is based on a dictionary stored in a memory of a mobile phone. While typing words it is sufficient to press a key for each letter once. The first word from dictionary that matches with letters corresponding to pressed keys is displayed.</p>

<p>The arrangement of letters on a mobile phone keyboard is given with the following table:</p>

<table class="table table-bordered td-center th-center">
	<thead>
		<tr>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th>6</th>
			<th>7</th>
			<th>8</th>
			<th>9</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>space</td>
			<td>A B C</td>
			<td>D E F</td>
			<td>G H I</td>
			<td>J K L</td>
			<td>M N O</td>
			<td>P Q R S</td>
			<td>T U V</td>
			<td>W X Y Z</td>
		</tr>
	</tbody>
</table>

<p>A message consists of a sequence of words separated by one space. Write a program that will simulate T9 system based on a given dictionary.</p>

### 입력 

 <p>The first line of input file contains a natural number M, 1 ≤ M ≤ 100, the number of words in a dictionary. Next M lines contain dictionary words, one word in each line. The words are sorted in ascending order. The words contain only capital letters of English alphabet (A–Z). Length of each word from dictionary will be 100 or less.</p>

<p>The next, (M+2)th line contains a natural number N, 1 ≤ N ≤ 100, the number of presses on a mobile phone keyboard.</p>

<p>The following line contains N natural numbers from set {1,2,...,9}, separated with one space, the numbers of pressed keys.</p>

### 출력 

 <p>The first and only line of output file should contain a message obtained by T9 system. Each letter of a word which is not in a dictionary should be replaced with a '*' character. If more than one word match a sequence of pressed keys, then the first one should be chosen.</p>

