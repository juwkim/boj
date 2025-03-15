# [Silver II] Bingo! - 4552 

[문제 링크](https://www.acmicpc.net/problem/4552) 

### 성능 요약

메모리: 111420 KB, 시간: 368 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 3월 16일 04:25:51

### 문제 설명

<p>Bingo is a game in which players try to form patterns on a 5 x 5 grid (or card). Each column on the card is represented by a letter in the game's namesake: B, I, N, G, or O. Each square on the grid contains a number. Players mark numbers as they are chosen randomly until a person has a card with a winning pattern marked (or bingo). An exception to this is the center square in the grid, which is a free spot and is already marked for all players at the beginning of each game. The possible numbers called are 1-75, inclusive, with each set of fifteen numbers corresponding to a letter: B for 1-15, I for 16-30, N for 31-45, G for 46-60, and O for 61-75.</p>

<p>Given the amount of numbers for each letter already called and information used to determine the set of winning patterns, write a program to determine the fewest amount of numbers that still need to be called for a possible bingo.</p>

### 입력 

 <p>Input to this problem will begin with a line containing a single integer n indicating the number of data sets. The first line in each data set will be in the format B I N G O X Y where:</p>

<ol>
	<li>B is the amount of numbers in the B category that have already been called;</li>
	<li>I is the amount of numbers in the I category that have already been called;</li>
	<li>N is the amount of numbers in the N category that have already been called;</li>
	<li>G is the amount of numbers in the G category that have already been called;</li>
	<li>O is the amount of numbers in the O category that have already been called;</li>
	<li>X (where 1 <= X <= 19) is the number of input patterns (the winning patterns are described through combinations of the input patterns);</li>
	<li>and Y (where 1 <= Y <= minimum (5, X)) is the minimum number of input patterns that must be combined to form a winning pattern.</li>
</ol>

<p>The next 5 lines in each data set will be a series of 5 x 5 grids of the input patterns in a format where X represents a square that must be marked and O represents a square that does not have to be marked. Using the input patterns and Y given above, the entire set of winning patterns can be determined.</p>

<p>For example, given an X of 4, a Y of 2, and a set of input patterns as follows:</p>

<pre>XXOOO OOOXX OOOOO OOOOO
XXOOO OOOXX OOOOO OOOOO
OOOOO OOOOO OOOOO OOOOO
OOOOO OOOOO XXOOO OOOXX
OOOOO OOOOO XXOOO OOOXX
</pre>

<p>the set of winning patterns (of which only one must be marked to have a bingo) is:</p>

<pre>XXOXX XXOOO XXOOO OOOXX OOOXX OOOOO
XXOXX XXOOO XXOOO OOOXX OOOXX OOOOO
OOOOO OOOOO OOOOO OOOOO OOOOO OOOOO
OOOOO XXOOO OOOXX XXOOO OOOXX XXOXX
OOOOO XXOOO OOOXX XXOOO OOOXX XXOXX</pre>

### 출력 

 <p>For each data set, output a single line containing the fewest amount of numbers that still need to be called to form a bingo.</p>

