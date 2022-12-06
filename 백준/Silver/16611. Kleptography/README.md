# [Silver IV] Kleptography - 16611 

[문제 링크](https://www.acmicpc.net/problem/16611) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p>John likes simple ciphers. He had been using the “Caesar” cipher to encrypt his diary until recently, when he learned a hard lesson about its strength by catching his sister Mary browsing through the diary without any problems.</p>

<p>Rapidly searching for an alternative, John found a solution: the famous “Autokey” cipher. He uses a version that takes the 26 lower-case letters ‘a’–‘z’ and internally translates them in alphabetical order to the numbers 0 to 25.</p>

<p>The encryption key k begins with a secret prefix of n letters. Each of the remaining letters of the key is copied from the letters of the plaintext a, so that k<sub>n+i</sub> = a<sub>i</sub> for i ≥ 1. Encryption of the plaintext a to the ciphertext b follows the formula b<sub>i</sub> = a<sub>i</sub> + k<sub>i</sub> mod 26.</p>

<p>Mary is not easily discouraged. She was able to get a peek at the last n letters John typed into his diary on the family computer before he noticed her, quickly encrypted the text document with a click, and left. This could be her chance.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with two integers n and m (1 ≤ n ≤ 30, n + 1 ≤ m ≤ 100), where n is the length of the keyword as well as the number of letters Mary saw, and m is the length of the text.</li>
	<li>One line with n lower-case letters, the last n letters of the plaintext.</li>
	<li>One line with m lower-case letters, the whole ciphertext.</li>
</ul>

### 출력 

 <p>Output the plaintext of John’s diary.</p>

