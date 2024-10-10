# [Silver III] Coverity Crossword - 11326 

[문제 링크](https://www.acmicpc.net/problem/11326) 

### 성능 요약

메모리: 110536 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 10월 10일 13:18:58

### 문제 설명

<p>What is your crossword telling you today? Can you scan your code for patterns, in the time it takes to get a cup of coffee? You have just landed a job at Coverity, and your first challenge is to demonstrate your searching and testing abilities. Can you find and analyze code that looks like random strings? Up to ten secret messages are hidden in a crossword of size 8x8, and your task is to determine if they are all present in the code or not.</p>

<p>Secrets are hidden horizontally, from left to right, vertically, from top to bottom, and diagonally, from top-left to bottom-right.</p>

### 입력 

 <p>The first line of the input contains an integer <strong>T</strong> (1 ≤ <strong>T</strong> ≤ 100), the number of test cases. Then follow <strong>T</strong> test cases. Each case starts with an integer <strong>N</strong> on a line (1 ≤ <strong>N</strong> ≤ 10), the number of words we are searching for. Each of the next <strong>N</strong> lines contains a non-empty string of length at most 8 characters over the alphabet [A-Z], the words we are searching for. Then follows 8 lines, each containing a string of exactly 8 characters over the alphabet [A-Z], the<strong>i</strong>'th horizontal line in the crossword, from left to right, starting from the topmost line down to the bottommost line.</p>

### 출력 

 <p>For each test case print on a separate line either "Yes" or "No", the answer to the question "Is it the case that all <strong>N</strong> messages are present in the crossword?"</p>

