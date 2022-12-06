# [Bronze II] iChess - 3602 

[문제 링크](https://www.acmicpc.net/problem/3602) 

### 성능 요약

메모리: 29200 KB, 시간: 76 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>The Jury of NEERC’07 quarterfinals is proud to present you a new game — chess patience. This patience is played not with cards, but with black and white square tiles. The goal of the game is to place these tiles on a flat surface so that they form a square colored in a chess-like pattern. The square should be totally filled and be of the maximal possible size. There may remain some spare tiles, if they do not fit into the resulting square.</p>

<p>To make this game more popular, a computer version of this patience named <em>iChess</em> was developed. The rules are the same with the exception that the player is given the number of tiles, not the actual tiles. Also, the result of the patience is not the actual layout, but the side length (measured in tiles) of the maximal square with the required layout.</p>

<p>Your task is to write a program which can play <em>iChess</em> patience.</p>

### 입력 

 <p>The input file contains two integer numbers b and w — the number of black and white tiles respectively (0 ≤ b, w ≤ 10 000).</p>

### 출력 

 <p>The first line of the input file must contain a single integer number s — the side length of the maximum possible square made of at most b black and w white tiles.</p>

<p>If no square can be formed with the given tiles, output a single word “Impossible”.</p>

