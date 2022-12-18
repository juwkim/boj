# [Bronze II] Decoder - 5365 

[문제 링크](https://www.acmicpc.net/problem/5365) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>All the Sith messages are sent using a complex coding scheme. You have cracked their code and must write a program to decode coded messages. Their code works as follows. Each word in the coded message represents one letter in the decoded message. Use the first letter of the first word and for each subsequent word use the nth letter where n is the length of the previous word. If the previous word is longer than the current word the current word represents a “space” (i.e., a blank space).</p>

<p>Here are two example:</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<th>Coded Message</th>
			<th>Decode Message</th>
		</tr>
		<tr>
			<td>
			<pre>A Tree
Some one too a sas
</pre>
			</td>
			<td>
			<pre>AT
S o s
</pre>
			</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>A positive integer, n, on the first line. After the first line there will be n words that represent the coded message.</p>

### 출력 

 <p>The decoded message on one line.</p>

