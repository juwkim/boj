# [Silver I] Permutation Code - 4633 

[문제 링크](https://www.acmicpc.net/problem/4633) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

구현, 문자열

### 제출 일자

2025년 7월 27일 21:13:08

### 문제 설명

<p>As the owner of a computer forensics company, you have just been given the following note by a new client:</p>

<p>I, Albert Charles Montgomery, have just discovered the most amazing cypher for encrypting messages. Let me tell you about it. </p>

<p>To begin, you will need to decide on a set of symbols, call it S, perhaps with the letters RATE. The size of this set must be a power of 2 and the order of the symbols in S is important. You must note that R is at position 0, A at 1, T at 2, and E at 3. You will also need one permutation P of all those symbols, say TEAR. Finally you will need an integer, call it x. Together, these make up the key. Given a key, you are now ready to convert a plaintext message M of length n (M[0], M[1]... M[n-1]), that has some but not necessarily all of the symbols in S, into a cyphertext string C, also of length n (C[0], C[1],...C[n-1]), that has some but not necessarily all of the symbols in S. <br>
The encrypting algorithm computes C as follows:</p>

<ol>
	<li>Calculate an integer d as the remainder after dividing the integer part of (n<sup>1.5</sup> + x) by n. This can be expressed more succinctly as d = (int)(n<sup>1.5</sup> + x) % n, where "%" is the remainder operator.</li>
	<li>Set C[d] to be the symbol in S whose position is the same as the position of M[d] in P.</li>
	<li>For each j ≠ d in 0..n-1, set C[j] to be the symbol in S whose position is the value obtained by xor-ing the position of M[j] in P with the position of M[(j+1) % n] in S. Note that the bitwise xor operator is "^" in C, C++, and Java.</li>
</ol>

<p>For example, consider this scenario where S=RATE, P=TEAR, x=102, M=TEETER, and n=6. To compute d, first calculate 61.5 + 102 = 116.696938, then take the remainder after dividing by 6. So d = 116 % 6 = 2. The following table shows the steps in filling in the cyphertext C. Note that the order of the steps is not important.</p>

<table class="table table-bordered" style="width:80%">
	<tbody>
		<tr>
			<td> </td>
			<td>0</td>
			<td>1</td>
			<td>2</td>
			<td>3</td>
			<td>4</td>
			<td>5</td>
			<td> </td>
		</tr>
		<tr>
			<td><em>S</em> =</td>
			<td>R</td>
			<td>A</td>
			<td>T</td>
			<td>E</td>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<td><em>P</em> =</td>
			<td>T</td>
			<td>E</td>
			<td>A</td>
			<td>R</td>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<td><em>M</em> =</td>
			<td>T</td>
			<td>E</td>
			<td>E</td>
			<td>T</td>
			<td>E</td>
			<td>R</td>
			<td> </td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<td><em>C</em> =</td>
			<td>E</td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td><em>M</em>[0] is <span style="font-family:monospace">T</span>, <span style="font-family:monospace">T</span> is at <em>P</em>[0]. <em>M</em>[1] is <span style="font-family:monospace">E</span>, <span style="font-family:monospace">E</span> is at <em>S</em>[3]. <em>C</em>[0] = <em>S</em>[0 xor 3] = <em>S</em>[3]</td>
		</tr>
		<tr>
			<td> </td>
			<td>E</td>
			<td>T</td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td><em>M</em>[1] is <span style="font-family:monospace">E</span>, <span style="font-family:monospace">E</span> is at <em>P</em>[1]. <em>M</em>[2] is <span style="font-family:monospace">E</span>, <span style="font-family:monospace">E</span> is at <em>S</em>[3]. <em>C</em>[1] = <em>S</em>[1 xor 3] = <em>S</em>[2]</td>
		</tr>
		<tr>
			<td> </td>
			<td>E</td>
			<td>T</td>
			<td>A</td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td><em>2 is d. M</em>[2] is <span style="font-family:monospace">E</span>, <span style="font-family:monospace">E</span> is at <em>P</em>[1], so <em>C</em>[2] =  <em>S</em>[1]</td>
		</tr>
		<tr>
			<td> </td>
			<td>E</td>
			<td>T</td>
			<td>A</td>
			<td>E</td>
			<td> </td>
			<td> </td>
			<td><em>M</em>[3] is <span style="font-family:monospace">T</span>, <span style="font-family:monospace">T</span> is at <em>P</em>[0]. <em>M</em>[4] is <span style="font-family:monospace">E</span>, <span style="font-family:monospace">E</span> is at <em>S</em>[3]. <em>C</em>[3] = <em>S</em>[0 xor 3] = <em>S</em>[3]</td>
		</tr>
		<tr>
			<td> </td>
			<td>E</td>
			<td>T</td>
			<td>A</td>
			<td>E</td>
			<td>A</td>
			<td> </td>
			<td><em>M</em>[4] is <span style="font-family:monospace">E</span>, <span style="font-family:monospace">E</span> is at <em>P</em>[1]. <em>M</em>[5] is <span style="font-family:monospace">R</span>, <span style="font-family:monospace">R</span> is at <em>S</em>[0]. <em>C</em>[4] = <em>S</em>[1 xor 0] = <em>S</em>[1]</td>
		</tr>
		<tr>
			<td> </td>
			<td>E</td>
			<td>T</td>
			<td>A</td>
			<td>E</td>
			<td>A</td>
			<td>A</td>
			<td><em>M</em>[5] is <span style="font-family:monospace">R</span>, <span style="font-family:monospace">R</span> is at <em>P</em>[3]. <em>M</em>[0] is <span style="font-family:monospace">T</span>, <span style="font-family:monospace">T</span> is at <em>S</em>[2]. <em>C</em>[5] = <em>S</em>[3 xor 2] = <em>S</em>[1]</td>
		</tr>
	</tbody>
</table>

<p>I have included additional examples of encrypted messages at the end of this note for you to experiment with. However, first, I need to tell you about the decryption algorithm.</p>

<p>Unfortunately, the next page of the note, with the decrypting algorithm, is completely unreadable because it is covered with huge, overlapping, messy ink blots. Given your considerable skill in unravelling puzzles, your task is to write the decoder based on your knowledge of the encoding algorithm.</p>

### 입력 

 <p>The input for the decoder consists of one or more sets of {key, encrypted message} pairs. The key is on 3 separate lines. The first line contains the single integer x, 0 < x < 10,000; the second line contains the string S; and the third line contains the string P, which will be a permutation of S. The length of S (and therefore P) will always be one of the following powers of two: 2, 4, 8, 16, or 32. Following the key is a line containing the encrypted message string C, which will contain at least one and at most sixty characters. The strings S, P, and C will not contain whitespace, but may contain printable characters other than letters and digits. The end of the input is a line which contains the single integer 0.</p>

### 출력 

 <p>For each input set print the decrypted string on a single line, as shown in the sample output.</p>

