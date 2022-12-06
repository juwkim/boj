# [Bronze II] Longest Subsequence - 10202 

[문제 링크](https://www.acmicpc.net/problem/10202) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Gru and Lucy are trying to break into El Macho’s lair. They arrive at a hallway that they need to walk across, which is likely booby-trapped. The hallway is a single line of squares, each of which is annotated either X or O. Gru believes that the only “safe” squares are the ones that comprise the longest subsequence of X’s, i.e., the longest contiguous set of squares that are all annotated X.</p>

<p>Your goal is to help Gru find the safe squares to jump on.</p>

### 입력 

 <p>The first line in the test data file contains the number of test cases (< 100). After that, each line contains one test case: the first number is the number of entries in the sequence, n (provided as an int), and the next n Strings (which can only be “X” or “O”) are the sequence itself.</p>

### 출력 

 <p>For each test case, you are to find the longest subsequence of consecutive X’s, and output the number of X’s in that sequence. The exact format is shown below in the examples.</p>

