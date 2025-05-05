# [Silver I] Error Correction - 6586 

[문제 링크](https://www.acmicpc.net/problem/6586) 

### 성능 요약

메모리: 110708 KB, 시간: 96 ms

### 분류

애드 혹, 구현, 수학

### 제출 일자

2025년 5월 6일 08:32:52

### 문제 설명

<p>A boolean matrix has the <em>parity property</em> when each row and each column has an even sum, i.e. contains an even number of bits which are set. Here's a 4 x 4 matrix which has the parity property:</p>

<pre>1 0 1 0
0 0 0 0
1 1 1 1
0 1 0 1
</pre>

<p>The sums of the rows are 2, 0, 4 and 2. The sums of the columns are 2, 2, 2 and 2.</p>

<p>Your job is to write a program that reads in a matrix and checks if it has the parity property. If not, your program should check if the parity property can be established by changing only one bit. If this is not possible either, the matrix should be classified as <em>corrupt</em>.</p>

### 입력 

 <p>The input file will contain one or more test cases. The first line of each test case contains one integer <em>n</em> (n < 100, representing the size of the matrix. On the next <em>n</em> lines, there will be <em>n</em> integers per line. No other integers than 0 and 1 will occur in the matrix. Input will be terminated by a value of 0 for <em>n</em>.</p>

### 출력 

 <p>For each matrix in the input file, print one line. If the matrix already has the parity property, print "OK". If the parity property can be established by changing one bit, print "Change bit <em>(i,j)</em>" where <em>i</em> is the row and <em>j</em> the column of the bit to be changed. Otherwise, print "Corrupt".</p>

