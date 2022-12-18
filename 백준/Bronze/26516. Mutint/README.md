# [Bronze II] Mutint - 26516 

[문제 링크](https://www.acmicpc.net/problem/26516) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현(implementation)

### 문제 설명

<p>A “Mutint” is an integer M that is changed according to certain criteria, such as in this problem. Given a positive integer, change M according to the following rules.</p>

<ol>
	<li>Find the leftmost largest digit D of M.</li>
	<li>If D is odd, change it to a zero.</li>
	<li>If D is even, add 4 to that digit. If the sum exceeds 9, change D to the one’s place of the sum.</li>
</ol>

### 입력 

 <p>Several integers, each on one line. The end of input is signaled with a zero on the last line. All integers, except the last integer, are positive.</p>

### 출력 

 <p>M, according to the rules above. M cannot have leading zeros.</p>

