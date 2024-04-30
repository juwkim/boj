# [Silver III] Scrabble Scoring - 7292 

[문제 링크](https://www.acmicpc.net/problem/7292) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

구현

### 제출 일자

2024년 4월 30일 12:08:29

### 문제 설명

<p>Scrabble is a word game which has now sold in excess of 100 million sets in 121 countries and 29 languages. The game is played by placing tiles, each of which is inscribed with a letter, on a board, according to some simple rules, which we will not bother about now. The values of the tiles in the English version are:</p>

<p>10: Q, Z<br>
8: J, X<br>
5: K<br>
4: F, H, V, W, Y<br>
3: B, C, M, P<br>
2: D, G<br>
1: A, E, I, L, N, O, R, S, T, U</p>

<p>The board consists of a 15×15 grid of squares. Some of these squares are coloured and there is a bonus for using them. Letter bonus squares (2L, 3L) multiply the value of the letter placed on them by two or three respectively; word bonus squares (2W, 3W) multiply the score of the entire word (after any relevant letter multipliers) by two or three respectively. Thus if I had placed the word ‘BANQUET’ as shown on the right of the figure below then I would score 84 (3+1+1+10*2+1+1+1)*3. If I had played ‘BANQUETS’ starting in the same place I would have scored 261 (3+1+1+2*10+1+1+1+1)*3*3.</p>

<p>Bonus squares are shown below for the top left quadrant of the board and are symmetrically placed on the rest of the board, i.e. the board is reflected about column H and row 8.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/7292/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-01-12%20%EC%98%A4%EC%A0%84%209.18.29.png" style="height:323px; width:650px">A play is denoted by specifying a starting position and orientation (row, column for horizontal words and column, row for vertical words) and the word. In actual play one would also need to worry about tiles already on the board, blank tiles, tiles in adjacent squares, bonus points for playing all the letters on your rack and so on, but we will ignore those details for this problem.</p>

### 입력 

 <p>Input will consist of a series of lines, each denoting a play. Each line will start with the designation of the starting position of the word followed by a space and the word itself — a sequence of 2 to 15 upper case letters. The placement of the word will be such that it will fit on the board. Rows will be designated by a number in the range 1 to 15, columns by an upper case letter in the range ‘A’ to ‘O’. If the row is specified first then the word is played horizontally, if the column is specified first then the word is played vertically. The sequence of plays will be terminated by a line containing a single ‘#’.</p>

### 출력 

 <p>Output will consist of one line for each play in the input, consisting of the play itself, followed by a space and the score for that play, as outlined above.</p>

