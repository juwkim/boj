# [Bronze I] Friendly Rooks - 24843 

[문제 링크](https://www.acmicpc.net/problem/24843) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구성적(constructive)

### 문제 설명

<p>Rook is a piece in the game of chess. It moves horizontally or vertically through any number of unoccupied squares, and can not jump over pieces. The rook can capture other piece if the piece is on the same vertical or horizontal line with the rook. There can be no more than one rook in one square of the chess board.</p>

<p>You are given $k$ rooks and a chess board with of $n \times m$. You need place these rooks on the board so that they cannot capture each other.</p>

### 입력 

 <p>The only line of input contains three integers $n$, $m$ and $k$ --- the lengths of the chess board sides and the number of rooks ($1 \le n, m, k \le 100$).</p>

### 출력 

 <p>If it is impossible to place $k$ rooks on an $n \times m$ chess board, print the line <code>Impossible</code>.</p>

<p>If there is at least one correct placement, print <code>Possible</code>. Then output $n$ lines of $m$ characters each --- the description of the placement of the rooks on the chess board. The $j$-th character of the $i$-th line must be "<code>*</code>" if the square $(i, j)$ contains a rook, or "<code>.</code>" if the corresponding square in your placement is empty.</p>

<p>If there are several correct placements, you can output any of them.</p>

