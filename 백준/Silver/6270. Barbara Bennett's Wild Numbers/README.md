# [Silver III] Barbara Bennett's Wild Numbers - 6270 

[문제 링크](https://www.acmicpc.net/problem/6270) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 6월 7일 14:34:52

### 문제 설명

<p>A wild number is a string containing digits and question marks (like 36?1?8). A number X matches a wild number W if they have the same length, and every non-question mark character in X is equal to the character in the same position in W (it means that you can replace a question mark with any digit). For example, 365198 matches the wild number 36?1?8, but 360199, 361028, or 36128 does not. Write a program that reads a wild number W and a number X from input, both of length n , and determines the number of n -digit numbers that match W and are greater than X .</p>

### 입력 

 <p>There are multiple test cases in the input. Each test case consists of two lines of the same length. The first line contains a wild number W , and the second line contains an integer number X . The length of input lines is between 1 and 10 characters. The last line of input contains a single character #.</p>

### 출력 

 <p>For each test case, write a single line containing the number of n -digit numbers matching W and greater than X (n is the length of W and X ).</p>

