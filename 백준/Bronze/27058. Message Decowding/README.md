# [Bronze II] Message Decowding - 27058 

[문제 링크](https://www.acmicpc.net/problem/27058) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>The cows are thrilled because they've just learned about encrypting messages.  They think they will be able to use secret messages to plot meetings with cows on other farms.</p>

<p>Cows are not known for their intelligence.  Their encryption method is nothing like DES or BlowFish or any of those really good secret coding methods.  No, they are using a simple substitution cipher.</p>

<p>The cows have a decryption key and a secret message.  Help them decode it.  The key looks like this:</p>

<pre>        yrwhsoujgcxqbativndfezmlpk</pre>

<p>Which means that an 'a' in the secret message really means 'y'; a 'b' in the secret message really means 'r'; a 'c' decrypts to 'w'; and so on.  Blanks are not encrypted; they are simply kept in place.</p>

<p>Input text is in upper or lower case, both decrypt using the same decryption key, keeping the appropriate case, of course.</p>

### 입력 

 <ul>
	<li>Line 1: 26 lower case characters representing the decryption key</li>
	<li>Line 2: As many as 80 characters that are the message to be decoded</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single line that is the decoded message.  It should have the same length as the second line of input.</li>
</ul>

