# [Bronze II] Vigenère Cipher - 5222 

[문제 링크](https://www.acmicpc.net/problem/5222) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Black Widow and Hawkeye need to discuss the plans for a surprise Birthday party for Nick Fury, and decide to use an encryption technique so that Nick can’t read their messages. In particular, they decide to use the <em>Vigenère Cipher</em>. Vigenère cipher is a simple form of polyalphabetic substitution, and was described by Giovan Battista Bellaso in 1553. It was misattributed to Blaise de Vigenère in the 19th century, because of a similar but stronger cipher presented by Vigenère in 1586.</p>

<p>Vigenère cipher is similar to the Caesar cipher. In Caesar cipher, each letter of the alphabet is shifted along some number of places; for example, in a Caesar cipher of shift 3, “A” would become “D”, “B” would become “E”, “Y” would become “B” and so on. The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.</p>

<p>For example, suppose that the plaintext to be encrypted is:</p>

<pre>ATTACKATDAWN</pre>

<p>The person sending the message chooses a <em>keyword</em> and repeats it until it matches the length of the plaintext, for example, the keyword “LEMON”:</p>

<pre>LEMONLEMONLE</pre>

<p>Each letter in the plaintext is shifted according to the corresponding letter in the keyword. So the first letter “A” is shifted according to “L”, second letter “T” is shifted according to “E”, the third letter “T” is shifted according to “M”, and so on.</p>

<p>The shifting itself works as follows. If we are shifting according to, say, “L”, then: “A” becomes “L”, “B” becomes “M”, “C” becomes “N”, and so on. If we reach the end of the alphabet, then we wrap around to the beginning. So “O” becomes “Z”, and “P” becomes “A”.</p>

<p>If the keyword letter is “E”, then each letter is shifted by 4 (so “T” becomes “X” and so on).</p>

<p>The plaintext above is encrypted to ciphertext:</p>

<pre>LXFOPVEFRNHR</pre>

<p>You are to write a program that helps Black Widow and Hawkeye encrypt their messages.</p>

### 입력 

 <p>The first line in the test data file contains the number of test cases (< 100). After that, each line contains one test case with two strings: the first string is the <em>keyword</em>, and the second string is the <em>plaintext</em>. Both the keyword and plaintext only contain capital letters (from A to Z) – all numbers or punctuation marks (including white spaces) are stripped out.</p>

### 출력 

 <p>For each test case, you are to output the encrypted ciphertext. The exact form of the output is shown below.</p>

