# [Bronze II] Cypher - 11297 

[문제 링크](https://www.acmicpc.net/problem/11297) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p>James Pond is a business man who often dreams he is a secret agent! He enjoys encrypting messages to his colleagues, who then have the task of decrypting them in order to read them. Your task is to write the decryption program for his staff to use.</p>

<p>Mr Pond uses the date as a key. He adds the day, month and year together, does a modulo 25 (remainder operator) on the answer and adds one to give him a value from 1 to 25 inclusive. This value, S, becomes the shift in his Caesar cypher.</p>

<p>In a Caesar cypher, each letter of a message is shifted S places forward through the alphabet, with z shifting to a where appropriate. For example, with a shift of 5, a becomes f, h becomes m and x becomes c. White space, punctuation and digits are not changed.</p>

### 입력 

 <p>Each message starts with the date as 3 integers on a single line, separated by spaces. A date of 0 0 0 marks the end of input.</p>

<p>The date is followed by a single line of at least 1 and no more than 250 characters; the line will not be just white space. Only lower case letters, spaces, punctuation marks and digits are used.</p>

### 출력 

 <p>For each message in the input, output a single line showing the decrypted message.</p>

