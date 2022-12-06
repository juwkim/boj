# [Silver V] FBI Universal Control Numbers - 13878 

[문제 링크](https://www.acmicpc.net/problem/13878) 

### 성능 요약

메모리: 117284 KB, 시간: 780 ms

### 분류

문자열(string)

### 문제 설명

<p>The FBI has recently changed its Universal Control Numbers (UCN) for identifying individuals who are in the FBI’s fingerprint database to an eight digit base 27 value with a ninth check digit. The digits used are:</p>

<p style="text-align: center;"><code>0123456789ACDEFHJKLMNPRTVWX</code></p>

<p>Some letters are not used because of possible confusion with other digits:</p>

<p style="text-align: center;"><code>B->8, G->C, I->1, O->0, Q->0, S->5, U->V, Y->V, Z->2</code></p>

<p>The check digit is computed as:</p>

<p style="text-align: center;"><code>(2*D1 + 4*D2 + 5*D3 + 7*D4 + 8*D5 + 10*D6 + 11*D7 + 13*D8) mod 27 </code></p>

<p>Where Dn is the nth digit from the left.</p>

<p>This choice of check digit detects any single digit error and any error transposing an adjacent pair of the original eight digits.</p>

<p>For this problem, you will write a program to parse a UCN input by a user. Your program should accept decimal digits and any capital letter as digits. If any of the confusing letters appear in the input, you should replace them with the corresponding valid digit as listed above. Your program should compute the correct check digit and compare it to the entered check digit. The input is rejected if they do not match otherwise the decimal (base 10) value corresponding to the first eight digits is returned.</p>

### 입력 

 <p>The first line of input contains a single decimal integer P, (1 ≤ P ≤ 10000), which is the number of data sets that follow. Each data set should be processed identically and independently.</p>

<p>Each data set consists of a single line of input. It contains the data set number, K, followed by a single space, followed by 9 decimal digits or capital (alphabetic) characters.</p>

### 출력 

 <p>For each data set there is one line of output. The single output line consists of the data set number, K, followed by a single space followed by the string “Invalid” (without the quotes) or the decimal value corresponding to the first eight digits.</p>

