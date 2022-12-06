# [Bronze I] Soundex - 4402 

[문제 링크](https://www.acmicpc.net/problem/4402) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Soundex coding groups together words that appear to sound alike based on their spelling. For example, "can" and "khawn", "con" and "gone" would be equivalent under Soundex coding.</p>

<p>Soundex coding involves translating each word into a series of digits in which each digit represents a letter:</p>

<pre>1 represents B, F, P, or V
2 represents C, G, J, K, Q, S, X,  or Z
3 represents D or T
4 represents L
5 represents M or N
6 represents R</pre>

<p>The letters A, E, I, O, U, H, W, and Y are not represented in Soundex coding, and repeated letters with the same code digit are represented by a single instance of that digit. Words with the same Soundex coding are considered equivalent.</p>

### 입력 

 <p>Each line of input contains a single word, all upper case, less than 20 letters long.</p>

### 출력 

 <p>For each line of input, produce a line of output giving the Soundex code.</p>

