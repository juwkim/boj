# [Silver IV] Playfair Cipher - 5040 

[문제 링크](https://www.acmicpc.net/problem/5040) 

### 성능 요약

메모리: 114488 KB, 시간: 120 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p>The Playfair cipher is a manual symmetric encryption technique and was the first digraph substitution cipher. The scheme was invented in 1854 by Charles Wheatstone, but bears the name of Lord Playfair who promoted the use of the cipher.</p>

<p>The Playfair cipher uses a 5 by 5 table containing each letter in the English alphabet exactly once (except ’Q’ which is missing). The table constitutes the encryption key. To more easily remember the table, it is typically generated from a key phrase. First fill in the spaces in an empty table with the letters of the key phrase (dropping spaces and duplicate letters), then fill the remaining spaces with the rest of the letters of the alphabet in order. The key phrase is written in the top rows of the table, from left to right. For instance, if the key phrase is ”playfair example”, the encryption key becomes</p>

<table class="table table-bordered table-center-30">
	<tbody>
		<tr>
			<td style="text-align: center;">P</td>
			<td style="text-align: center;">L</td>
			<td style="text-align: center;">A</td>
			<td style="text-align: center;">Y</td>
			<td style="text-align: center;">F</td>
		</tr>
		<tr>
			<td style="text-align: center;">I</td>
			<td style="text-align: center;">R</td>
			<td style="text-align: center;">E</td>
			<td style="text-align: center;">X</td>
			<td style="text-align: center;">M</td>
		</tr>
		<tr>
			<td style="text-align: center;">B</td>
			<td style="text-align: center;">C</td>
			<td style="text-align: center;">D</td>
			<td style="text-align: center;">G</td>
			<td style="text-align: center;">H</td>
		</tr>
		<tr>
			<td style="text-align: center;">J</td>
			<td style="text-align: center;">K</td>
			<td style="text-align: center;">N</td>
			<td style="text-align: center;">O</td>
			<td style="text-align: center;">S</td>
		</tr>
		<tr>
			<td style="text-align: center;">T</td>
			<td style="text-align: center;">U</td>
			<td style="text-align: center;">V</td>
			<td style="text-align: center;">W</td>
			<td style="text-align: center;">Z</td>
		</tr>
	</tbody>
</table>

<p>To encrypt a message, one would remove all spaces and then break the message into digraphs (groups of 2 letters) such that, for example, ”Hello World” becomes ”HE LL OW OR LD”. Then map them out on the key table, and apply the rule below that matches the letter combination:</p>

<ul>
	<li>If both letters are the same (or only one letter is left), add an ’X’ after the first letter. Encrypt the new pair and continue (note that this changes all the remaining digraphs).</li>
	<li>If the letters appear on the same row of your table, replace them with the letters to their immediate right respectively (wrapping around to the left side of the row if a letter in the original pair was on the right side of the row). With the table above, the digraph ’CH’ would be encrypted ’DB’.</li>
	<li>If the letters appear on the same column of your table, replace them with the letters immediately below respectively (wrapping around to the top side of the column if a letter in the original pair was on the bottom side of the column). With the table above, the digraph ’VA’ would be encrypted ’AE’.</li>
	<li>If the letters are not on the same row or column, replace them with the letters on the same row respectively but at the other pair of corners of the rectangle defined by the original pair. The order is important – the first letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair. With the table above, the digraph ’KM’ would be encrypted ’SR’.</li>
</ul>

<p>Write a program that reads a key phrase and a plaintext to encrypt, and outputs the encrypted text.</p>

<p><em>The text to encrypt will not contain two ’x’s following each other, or an ’x’ as the last character, as this might cause the first rule above to repeat itself indefinitely.</em></p>

### 입력 

 <p>The input contains two lines. The first line contains the key phrase. The second line contains the text to encrypt. Each line will contain between 1 and 1000 characters, inclusive. Each character will be a lower case English letter, ’a’ - ’z’ (except ’q’), or a space character. Neither line will start or end with a space.</p>

### 출력 

 <p>The output should be a single line containing the encrypted text, in upper case. There should be no spaces in the output.</p>

