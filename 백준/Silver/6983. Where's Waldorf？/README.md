# [Silver III] Where's Waldorf? - 6983 

[문제 링크](https://www.acmicpc.net/problem/6983) 

### 성능 요약

메모리: 111392 KB, 시간: 156 ms

### 분류

브루트포스 알고리즘, 구현, 문자열

### 제출 일자

2024년 6월 2일 07:01:30

### 문제 설명

<p>Given an m by n grid of letters and a list of words, find the location in the grid at which the word can be found. A word matches a straight, uninterrupted line of letters in the grid, regardless of case. The matching can be done in any of the eight directions either horizontally, vertically or diagonally through the grid.</p>

### 입력 

 <p>The input begins with a number on a line by itself, indicating the number of test cases that follow. Each test case consists of a pair of integers, m followed by n, 1 ≤ m ≤ 50 and 1 ≤ n ≤ 50 in decimal notation on a single line. The next m lines contain n letters each; this is the grid of letters in which the words of the list must be found. The letters in the grid are in upper or lower case. Following the grid of letters, another integer k appears on a line by itself (1 ≤ k ≤ 20). The next k lines of input contain the list of words to search for, one word per line. These words contain upper and lower case letters only (no spaces, hyphens or other non-alphabetic characters). All words have positive length.</p>

### 출력 

 <p>For each word in the word list of one test case, your program must output a pair of integers representing the location of the corresponding word in the grid. The integers must be separated by a single space. The first integer is the line in the grid where the first letter of the given word can be found (1 represents the topmost line in the grid, and m represents the bottommost line). The second integer is the column in the grid where the first letter of the given word can be found (1 represents the leftmost column in the grid, and n represents the rightmost column in the grid). If a word can be found more than once in the grid, then the location which is output should correspond to the uppermost occurrence of the first letter of the word (i.e. the occurrence which places the first letter of the word closest to the top of the grid). If two or more words are uppermost, the output should correspond to the leftmost of these occurrences. If there is no occurence of the given word, print m and n instead. Outputs of different test cases are separated by a blank line.</p>

