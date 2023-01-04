# [Silver IV] Simplified Keyboard - 25882 

[문제 링크](https://www.acmicpc.net/problem/25882) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Consider a simplified keyboard consisting of the 26 lowercase letters as illustrated below:</p>

<p style="text-align: center;"><img alt="" src="" style="width: 216px; height: 68px;"></p>

<p>We define the neighbors of a key (letter) as all the letters adjacent to it. For example, the neighbors of ‘a’ are {b, k, j}, neighbors of ‘b’ are {a, c, l, k, j}, neighbors of ‘n’ are {d, e, f, o, x, w, v, m}, and neighbors of ‘z’ are {p, q, r, y}.</p>

<p>Given two words consisting of lowercase letters only, you are to determine which of the following three cases applies to them:</p>

<ol>
	<li>identical: this is when the two words are of the same length and they match letter-byletter. For example, “cool” and “cool” are identical, “cool” and “col” are not, and “cool” and “colo” are not</li>
	<li>similar: this is when the two words are of the same length, they are not identical words, and each corresponding two letters either match or are neighbors. For example, “aaaaa” and “abkja” are similar, “moon” and “done” are similar, “knq” and “bxz” are similar, but “ab” and “cb” are not (because of ‘a’ in the first word and the corresponding ‘c’ in the second word).</li>
	<li>different: this is when neither of the above two cases applies to the two words, i.e., they are not identical and they are not similar. For example, “ab” and “abc” are different, “ab” and “az” are different, and “az” and “za” are different.</li>
</ol>

### 입력 

 <p>The first input line contains a positive integer, n, indicating the number of test cases to process. Each of the following n input lines represents a test case, consisting of two words separated by one space. Each word consists of lowercase letters only and will be between 1 and 20 letters, inclusive.</p>

### 출력 

 <p>For each test case, output one line. That line should contain the digit (number) 1, 2, or 3, to indicate which of the above three cases applies to the two input words.</p>

