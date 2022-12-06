# [Bronze I] TicTacToe - 13227 

[문제 링크](https://www.acmicpc.net/problem/13227) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>We want to create a program to check the result of a tic tac toe game. A tic tac toe board is a 3x3 grid. Each position can contain either X or O. The game finishes with a winner when a player creates a straight line of 3 equal symbols. The next 3 boards show finished games with a winner. The empty positions are represented using dots. </p>

<pre>X.X     OX.    .X.
OOO     .O.    .X.
...     X.O    .XO</pre>

<p>In contrast, these 3 boards have not finished with a winner.</p>

<pre>OXO    X..    ...
XXO    O.O    .X.
OOX    .XX    ..O</pre>

### 입력 

 <p>The test case consists of 3 lines. Each one with 3 characters (dot, O or X). Note that we are using the letter “O” not the digit zero.</p>

### 출력 

 <p>For each test case, write YES if the board finished with a winner or NO if there is no winner.</p>

