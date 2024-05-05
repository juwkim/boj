# [Silver III] Crossword Puzzle Clue Numbering - 9232 

[문제 링크](https://www.acmicpc.net/problem/9232) 

### 성능 요약

메모리: 108080 KB, 시간: 120 ms

### 분류

구현

### 제출 일자

2024년 5월 5일 16:03:10

### 문제 설명

<p>Professor Logophile is the local crossword puzzle setter. He has a very idiosyncratic way of working — he writes the words into a blank grid and then fills in the unused squares. That is the easy bit, but he has trouble doing the next bit — numbering the puzzle and preparing the the clues. </p>

<p>This is where you come in. Given a completed crossword, print out a form on which the clues can be written (showing word lengths). Note that he always prepares a true crossword, i.e. there is always at least one word in each direction and there is always at least one shared letter. All words contain three or more letters.</p>

### 입력 

 <p>Input will be a series of crosswords. The first line of each crossword will be a pair of integers (r and c, 3 ≤ r c ≤ 20) giving the number of rows and columns of the crossword. This will be followed r rows each containing c characters. Each character will be either an uppercase letter or a ‘@’ representing a black square. The file will be terminated by a pair of zeroes (0 0).</p>

### 출력 

 <p>For each crossword, the output will start with a line containing “Crossword puzzle <cwnum>” where <cwnum> is a running number starting at 1, followed by a form showing the clue number and length for both across and down clues. Each form begins with the word ‘Across’ or ‘Down’ as appropriate, followed by a line for each across or down word that appears in the crossword. Each line begins with the word number with no preceding spaces followed by a full stop, two spaces, an open parenthesis (‘(‘), the length of the word with no preceding spaces and a closing parenthesis (‘)’). Leave one blank line between the ‘Across’ and ‘Down’ parts and between successive crosswords.</p>

