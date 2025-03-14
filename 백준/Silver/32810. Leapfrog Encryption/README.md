# [Silver II] Leapfrog Encryption - 32810 

[문제 링크](https://www.acmicpc.net/problem/32810) 

### 성능 요약

메모리: 109544 KB, 시간: 100 ms

### 분류

구현

### 제출 일자

2025년 3월 15일 07:21:51

### 문제 설명

<p>We've come up with a new encryption method we call Leapfrog Encryption. It is a key-based encryption scheme where an alphabetic key specifies how letters in the <em>plaintext</em> (the text to be encrypted) are placed in the <em>ciphertext</em> (the resulting encrypted string). Here's how Leapfrog Encryption works:</p>

<ol>
	<li>Remove all non-alphabetic characters from the plaintext and convert all remaining letters to lowercase.</li>
	<li>Convert the letters of the key to their location in the alphabet $+ 1$ (so that '<code>a</code>' converts to $2$, '<code>b</code>' converts to $3$ and so on). This gives us a sequence of numbers $d_1, d_2, \ldots, d_n$ where $n$ is the length of the key.</li>
	<li>Going left-to-right, place the first letters in the plaintext in every $d_1$-th location of the ciphertext until you run out of positions in the ciphertext (where the length of the ciphertext is equal to the number of letters in the plaintext). So for example, if $d_1=5$ the first letter in the plaintext goes in position $5$ of the ciphertext (numbering the first location in the ciphertext as position $1$), the second letter in the plaintext goes in position $10$ in the ciphertext, and so on.</li>
	<li>Repeat this with $d_2$ but this time going right-to-left through the ciphertext, only counting the empty positions (leapfrogging over the letters already in the ciphertext).</li>
	<li>Continue with $d_3$, $d_4$, etc., alternating the direction you go through the ciphertext each time.</li>
	<li>If there are still letters left in the plaintext after using $d_n$, fill in the remaining empty locations in the ciphertext with these remaining letters, again going in the opposite direction of the previous pass (this is equivalent to having $d_{n+1} = 1$).</li>
</ol>

<p>For example, if our plaintext is "Send more monkeys!" and our key is "bea", the encryption proceeds as follows:</p>

<table class="table table-bordered td-center table-center-40">
	<tbody>
		<tr>
			<td>b $\rightarrow$ 3, left-to-right:</td>
			<td><code>_ _ s _ _ e _ _ n _ _ d _ _ m</code></td>
		</tr>
		<tr>
			<td>e $\rightarrow$ 6, right-to-left:</td>
			<td><code>_ _ s _ _ e o _ n _ _ d _ _ m</code></td>
		</tr>
		<tr>
			<td>a $\rightarrow$ 2, left-to-right:</td>
			<td><code>_ r s _ e e o _ n m _ d o _ m</code></td>
		</tr>
		<tr>
			<td>last pass, right-to-left:</td>
			<td><code>s r s y e e o e n m k d o n m</code></td>
		</tr>
	</tbody>
</table>

<p>Decryption is done by $\ldots$ hey, you know what? We're going to let you figure that out.</p>

### 입력 

 <p>The first line of input contains two strings $t$ $k$ where $t$ is either <code>E</code> or <code>D</code> indicating whether to perform encryption or decryption and $k$ is the lowercase alphabetic key. The length of $k$ will be between $1$ and $100$, inclusive. The second and final line of input contains the plaintext to encrypt (if $t$ is <code>E</code>) or the ciphertext to decrypt (if $t$ is <code>D</code>). This string is non-empty and has a maximum length of $2\,000$. A ciphertext string consists of lowercase letters only, while a plaintext string may contain uppercase letters, numbers, punctuation and spaces as well (all counted as part of the length of the string) and is guaranteed to contain at least one letter.</p>

### 출력 

 <p>Output the encrypted or decrypted text. Your output should only contain lowercase letters.</p>

