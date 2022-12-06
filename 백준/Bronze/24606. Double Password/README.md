# [Bronze III] Double Password - 24606 

[문제 링크](https://www.acmicpc.net/problem/24606) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

조합론(combinatorics), 수학(math)

### 문제 설명

<p>A computer at ICPC headquarters is protected by a four-digit password---in order to log in, you normally need to guess the four digits exactly. However, the programmer who implemented the password check left a backdoor in the computer---there is a second four-digit password. If the programmer enters a four-digit sequence, and for each digit position the digit entered matches at least one of the two passwords in that same position, then that four-digit sequence will log the programmer into the computer.</p>

<p>Given the two passwords, count the number of distinct four-digit sequences that can be entered to log into the computer.</p>

### 입력 

 <p>The input consists of exactly two lines. Each of the two lines contains a string $s$ ($|s| = 4$, $s \in \{<code>0-9</code>\}^*$). These are the two passwords.</p>

### 출력 

 <p>Output a single integer, which is the number of distinct four-digit sequences that will log the programmer into the system.</p>

