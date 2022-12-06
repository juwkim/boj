# [Bronze II] Cold Compress - 17011 

[문제 링크](https://www.acmicpc.net/problem/17011) 

### 성능 요약

메모리: 32020 KB, 시간: 96 ms

### 분류

구현(implementation)

### 문제 설명

<p>Your new cellphone plan charges you for every character you send from your phone. Since you tend to send sequences of symbols in your messages, you have come up with the following compression technique: for each symbol, write down the number of times it appears consecutively, followed by the symbol itself. This compression technique is called run-length encoding.</p>

<p>More formally, a block is a substring of identical symbols that is as long as possible. A block will be represented in compressed form as the length of the block followed by the symbol in that block. The encoding of a string is the representation of each block in the string in the order in which they appear in the string.</p>

<p>Given a sequence of characters, write a program to encode them in this format.</p>

### 입력 

 <p>The first line of input contains the number N, which is the number of lines that follow. The next N lines will contain at least one and at most 80 characters, none of which are spaces.</p>

### 출력 

 <p>Output will be N lines. Line i of the output will be the encoding of the line i+1 of the input. The encoding of a line will be a sequence of pairs, separated by a space, where each pair is an integer (representing the number of times the character appears consecutively) followed by a space, followed by the character.</p>

