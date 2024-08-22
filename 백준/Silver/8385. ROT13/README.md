# [Silver III] ROT13 - 8385 

[문제 링크](https://www.acmicpc.net/problem/8385) 

### 성능 요약

메모리: 170800 KB, 시간: 300 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 문자열

### 제출 일자

2024년 8월 23일 06:51:45

### 문제 설명

<p>The Byteland Aircraft Factory has recently developed a new type of jet plane. Naming the planes with numbers is not fashionable anymore, so the management decided to form a two-word name. To draw potential clients' attention, the name should have an additional property: when encoded with the ROT13 cipher it should still be legible - the encoded form should differ only by the order of the words.</p>

<p>Recall that the ROT13 cipher changes each letter to the one that lies 13 characters away in the alphabet. To be more precise, the encoding follows the table below.</p>

<table class="table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td>original letter</td>
			<td><code>abcdefghijklmnopqrstuvwxyz</code></td>
		</tr>
		<tr>
			<td>encoded letter</td>
			<td><code>nopqrstuvwxyzabcdefghijklm</code></td>
		</tr>
	</tbody>
</table>

<p>Write a program which:</p>

<ul>
	<li>reads from the standard input the list of available words,</li>
	<li>calculates the number of different possible plane names,</li>
	<li>writes the result to the standard output.</li>
</ul>

### 입력 

 <p>The first line of the input consists of a single integer <em>n</em> (1 ≤ <em>n</em> ≤ 1 000 000). In each of the next <em>n</em> lines there is one word consisting of small letters of the English alphabet. Each word contains at least one character. The cummulative length of all the words does not exceed 1 000 000 letters.</p>

### 출력 

 <p>The first and only line of the output should contain one integer - the total number of different possible plane names.</p>

