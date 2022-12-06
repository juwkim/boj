# [Bronze I] Jenga - 9287 

[문제 링크](https://www.acmicpc.net/problem/9287) 

### 성능 요약

메모리: 114328 KB, 시간: 132 ms

### 분류

Empty

### 문제 설명

<p>You are writing a computer program that will play Jenga, but first you need to figure out what boards are legal! Given a set of possible jenga boards, determine if each board is standing or if it has fallen over. A board falls over if any two consecutive blocks in a row (not column) are both missing, including within the top row. Assume that even two consecutive missing blocks on the top row makes the tower ”Fallen.”</p>

### 입력 

 <p>The first line of input is the number of test cases that follow.</p>

<p>Each input case will start with a single integer representing the height of the Jenga tower. Each row in the tower appears on a single line and represents the blocks currently still in the board for that row. A ’1’ represents the block being present, a ’0’ represents a removed block.</p>

<p>There will be between 1 and 100 test cases, each with one jenga board of height between 1 and 20.</p>

### 출력 

 <p>For each case, output the line “Case x:” where x is the case number, on a single line followed by a single space and either the word ”Fallen” or ”Standing”</p>

