# [Silver III] Radix 3 - 22793 

[문제 링크](https://www.acmicpc.net/problem/22793) 

### 성능 요약

메모리: 108080 KB, 시간: 104 ms

### 분류

구현, 수학

### 제출 일자

2024년 2월 13일 04:58:28

### 문제 설명

<p>The Great Sand Council (GSC) of the planet Phleebutt (apologies to Sierra) have devised a base 3 number system to suit their physiology. The symbols used to represent the three valid digits of their number system are ‘0’, ‘1’, and ‘-’, following the unusual configuration of their hands (don’t ask). The decimal counterparts of the three symbols are, respectively, 0, 1 and −1.</p>

<p>Each position in a number has a value three times greater than the position immediately to its right. For example, the number ‘10-’ has the value 8 in decimal, since 1×9+ 0×3+ (−1)× = 8. Similarly, the number ‘-1’ has the decimal value −2, since (−1)×3+1 = −2. GSC representations of integers never start with a digit of zero, except for ‘0’ (a single zero) which has the decimal value 0.</p>

<p>You have to write a program that can convert 32-bit signed decimal integers into their equivalent GSC representations.</p>

### 입력 

 <p>Your program will receive a list of integers as input. Each integer will appear in a separate line and be between −2<sup>31</sup> and 2<sup>31</sup> − 1. The end of list is indicated by the end of file.</p>

### 출력 

 <p>You have to echo the input numbers followed by their GSC representations, as shown in the Sample Output (including all extra symbols).</p>

