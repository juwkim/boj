# [Silver I] Pollock's conjecture - 4957 

[문제 링크](https://www.acmicpc.net/problem/4957) 

### 성능 요약

메모리: 159608 KB, 시간: 2836 ms

### 분류

다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 너비 우선 탐색

### 제출 일자

2025년 5월 14일 04:59:49

### 문제 설명

<p>The nth triangular number is defined as the sum of the first n positive integers. The nth tetrahedral number is defined as the sum of the first n triangular numbers. It is easy to show that the nth tetrahedral number is equal to n(n+1)(n+2) ⁄ 6. For example, the 5th tetrahedral number is 1+(1+2)+(1+2+3)+(1+2+3+4)+(1+2+3+4+5) = 5×6×7 ⁄ 6 = 35.</p>

<p>The first 5 triangular numbers: 1, 3, 6, 10, 15</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images2/C-11.png" style="height:108px; width:108px"><img alt="" src="https://www.acmicpc.net/upload/images2/C-12.png" style="height:108px; width:108px"><img alt="" src="https://www.acmicpc.net/upload/images2/C-13.png" style="height:108px; width:108px"><img alt="" src="https://www.acmicpc.net/upload/images2/C-14.png" style="height:108px; width:108px"><img alt="" src="https://www.acmicpc.net/upload/images2/C-15.png" style="height:108px; width:108px"></p>

<p>The first 5 tetrahedral numbers: 1, 4, 10, 20, 35</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images2/C-1.png" style="height:108px; width:108px"><img alt="" src="https://www.acmicpc.net/upload/images2/C-2.png" style="height:108px; width:108px"><img alt="" src="https://www.acmicpc.net/upload/images2/C-3.png" style="height:108px; width:108px"><img alt="" src="https://www.acmicpc.net/upload/images2/C-4.png" style="height:108px; width:108px"><img alt="" src="https://www.acmicpc.net/upload/images2/C-5.png" style="height:108px; width:108px"></p>

<p>In 1850, Sir Frederick Pollock, 1st Baronet, who was not a professional mathematician but a British lawyer and Tory (currently known as Conservative) politician, conjectured that every positive integer can be represented as the sum of at most five tetrahedral numbers. Here, a tetrahedral number may occur in the sum more than once and, in such a case, each occurrence is counted separately. The conjecture has been open for more than one and a half century.</p>

<p>Your mission is to write a program to verify Pollock's conjecture for individual integers. Your program should make a calculation of the least number of tetrahedral numbers to represent each input integer as their sum. In addition, for some unknown reason, your program should make a similar calculation with only odd tetrahedral numbers available.</p>

<p>For example, one can represent 40 as the sum of 2 tetrahedral numbers, 4×5×6 ⁄ 6 + 4×5×6 ⁄ 6, but 40 itself is not a tetrahedral number. One can represent 40 as the sum of 6 odd tetrahedral numbers, 5×6×7 ⁄ 6 + 1×2×3 ⁄ 6 + 1×2×3 ⁄ 6 + 1×2×3 ⁄ 6 + 1×2×3 ⁄ 6 + 1×2×3 ⁄ 6, but cannot represent as the sum of fewer odd tetrahedral numbers. Thus, your program should report 2 and 6 if 40 is given.</p>

### 입력 

 <p>The input is a sequence of lines each of which contains a single positive integer less than 106. The end of the input is indicated by a line containing a single zero.</p>

### 출력 

 <p>For each input positive integer, output a line containing two integers separated by a space. The first integer should be the least number of tetrahedral numbers to represent the input integer as their sum. The second integer should be the least number of odd tetrahedral numbers to represent the input integer as their sum. No extra characters should appear in the output.</p>

