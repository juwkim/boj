# [Bronze II] Grid Pattern - 14539 

[문제 링크](https://www.acmicpc.net/problem/14539) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Games that are commonly found in the Unix System during the 70s and 80s are design in text mode. Grid is the basic layout for many of these games where pieces or items are positioned in rows and columns. Classic examples would be tic-tac-toe, chess and minesweeper. You are to design a simple text-based grid layout engine that can be used in the games.</p>

<p>Given specified dimensions, print a text-based grid pattern. Use the | (pipe) sign to print vertical elements, the – (minus) to print horizontal ones and + (plus) for crossing. The rest of the spaces are filled with * (asterisk).</p>

### 입력 

 <p>The first line of input contains a positive integer <em>N</em> (<em>N</em> ≤ 100) which indicates the number of test cases. Each of the following <em>N</em> lines contains four positive integers: <em>row</em> – the number of rows, <em>col</em> – the number of columns, <em>w</em> and <em>h</em> – the width and height of the single grid respectively. (1 ≤ <em>row</em>, <em>col</em> ≤ 10; 1 ≤  <em>w</em>, <em>h</em> ≤ 5 )</p>

### 출력 

 <p>For each test case, output a line in the format "Case #x:" where x is the case number (starting from 1), follow by the grid pattern as shown in the sample output.</p>

