# [Bronze I] Complimentary - 26512 

[문제 링크](https://www.acmicpc.net/problem/26512) 

### 성능 요약

메모리: 30616 KB, 시간: 36 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Two’s complement is used to express negative numbers in binary. For example, the value 30 in signed 8- bit binary is 00011110, and the signed 8-bit two’s complement representation of -30 is 11100010. An easy way to convert from 00011110 to 11100010 is simply reverse 00011110 to become 11100001, and then add 1, which produces 11100010.</p>

<p>Your job is to read in two positive integers, express them in 8-bit signed binary, then their negative values in two’s complement, and then the difference between the two in 8-bit signed binary.</p>

<p>For example, the difference between 30 and 18 is 12, which in 8-bit signed binary is 00001100, or if you subtract 18 – 30, you get -12, which in two’s complement (signed 8-bit) is the reverse of 00001100 + 1, or 11110011 + 1, or 11110100.</p>

### 입력 

 <p>Several pairs of positive integers X and Y, each pair on one line, with 0</p>

### 출력 

 <p>For each pair of values, five 8-bit signed strings, representing X, Y, -X, -Y, and X-Y, with a blank line following each output set.</p>

