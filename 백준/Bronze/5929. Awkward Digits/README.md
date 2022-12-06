# [Bronze I] Awkward Digits - 5929 

[문제 링크](https://www.acmicpc.net/problem/5929) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>Bessie the cow is just learning how to convert numbers between different bases, but she keeps making errors since she cannot easily hold a pen between her two front hooves.</p><p>Whenever Bessie converts a number to a new base and writes down the result, she always writes one of the digits wrong.  For example, if she converts the number 14 into binary (i.e., base 2), the correct result should be "1110", but she might instead write down "0110" or "1111".  Bessie never accidentally adds or deletes digits, so she might write down a number with a leading digit of "0" if this is the digit she gets wrong.</p><p>Given Bessie's output when converting a number N into base 2 and base 3, please determine the correct original value of N (in base 10). You can assume N is at most 1 billion, and that there is a unique solution for N.</p><p>Please feel welcome to consult any on-line reference you wish regarding base-2 and base-3 numbers, if these concepts are new to you.</p>

### 입력 

 <ul><li>Line 1: The base-2 representation of N, with one digit written incorrectly.</li><li>Line 2: The base-3 representation of N, with one digit written incorrectly.</li></ul>

### 출력 

 <ul><li>Line 1: The correct value of N.</li></ul>

