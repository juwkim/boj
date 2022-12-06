# [Bronze II] The Seven Percent Solution - 4606 

[문제 링크](https://www.acmicpc.net/problem/4606) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Uniform Resource Identifiers (or URIs) are strings like http://icpc.baylor.edu/icpc/, mailto:foo@bar.org, ftp://127.0.0.1/pub/linux, or even just readme.txt that are used to identify a resource, usually on the Internet or a local computer. Certain characters are reserved within URIs, and if a reserved character is part of an identifier then it must be percent-encoded by replacing it with a percent sign followed by two hexadecimal digits representing the ASCII code of the character. A table of seven reserved characters and their encodings is shown below. Your job is to write a program that can percent-encode a string of characters.</p>

<table class="table table-bordered" style="width:30%">
	<thead>
		<tr>
			<th>Character</th>
			<th>Encoding</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>" " (space)</td>
			<td>%20</td>
		</tr>
		<tr>
			<td>"!" (exclamation point)</td>
			<td>%21</td>
		</tr>
		<tr>
			<td>"\$" (dollar sign)</td>
			<td>%24</td>
		</tr>
		<tr>
			<td>"%" (percent sign)</td>
			<td>%25</td>
		</tr>
		<tr>
			<td>"(" (left parenthesis)</td>
			<td>%28</td>
		</tr>
		<tr>
			<td>")" (right parenthesis)</td>
			<td>%29</td>
		</tr>
		<tr>
			<td>"*" (asterisk)</td>
			<td>%2a</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>The input consists of one or more strings, each 1–79 characters long and on a line by itself, followed by a line containing only "#" that signals the end of the input. The character "#" is used only as an end-of-input marker and will not appear anywhere else in the input. A string may contain spaces, but not at the beginning or end of the string, and there will never be two or more consecutive spaces.</p>

### 출력 

 <p>For each input string, replace every occurrence of a reserved character in the table above by its percent-encoding, exactly as shown, and output the resulting string on a line by itself. Note that the percent-encoding for an asterisk is %2a (with a lowercase "a") rather than %2A (with an uppercase "A").</p>

