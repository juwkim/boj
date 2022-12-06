# [Bronze I] Don’t Break the Ice - 25895 

[문제 링크](https://www.acmicpc.net/problem/25895) 

### 성능 요약

메모리: 114328 KB, 시간: 128 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Mr. Pennybags is enthralled with his new board game which involves knocking out tiny plastic ice blocks from a square grid. Pennybags was never very good at games and would like to practice his breaking strategies without having to reset the board. He has asked Unified Coders For Games (UCF Games) to develop such a tool. Pennybags wants a program to take in the description of a board and a sequence of moves and determine the number of invalid moves.</p>

<p>Given the dimensions (number of rows and columns) of a square game board and a list of moves, determine the number of attempted moves that would knock out an ice block that is no longer in the board. Note that when an ice block is knocked out, other blocks may fall out of the board as well. More specifically, an ice block will fall unless it is in a complete row (the row contains all its ice blocks) or it is in a complete column (the column contains all its ice blocks). Note also that if the fall of block B<sub>1</sub> results in the fall of block B<sub>2</sub>, then other blocks may fall as a result of block B<sub>2</sub> falling.</p>

### 입력 

 <p>The first input line contains a positive integer, t, indicating the number of game boards. This is followed by the data for each game. The first input line for each game contains two integers (separated by a space): the dimensions (length and width) of a square game board (between 1 and 50 inclusive) and the number of attempted moves in Pennybags’ strategy (between 1 and 100 inclusive). This is followed by the row and column (separated by a space) for each attempted move, one move per line. Assume that the input values are valid, e.g., the row/column for an attempted move will always be a cell of the game board.</p>

### 출력 

 <p>For each game board, output “Strategy #b: i” where b is the game board number (starting with 1), and i is the number of invalid moves. Leave a blank line after the output for each game board.</p>

