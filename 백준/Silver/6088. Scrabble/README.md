# [Silver IV] Scrabble - 6088 

[문제 링크](https://www.acmicpc.net/problem/6088) 

### 성능 요약

메모리: 118424 KB, 시간: 156 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현

### 제출 일자

2024년 1월 27일 10:02:28

### 문제 설명

<p>Bessie is playing Bovine Scrabble which is just like regular Scrabble except that a player's tray has T (3 <= T <= 20) letters instead of always having 7 letters as in the normal game.</p>

<p>For those who haven't played English Scrabble, it is a word game where each player has a set of T letters and uses them to form a word to place on a gameboard which ends up looking a little bit like a crossword puzzle. For this task, Bessie has the first play and cares only to make a word from one or more of her letters (without worrying how to fit it onto the board).</p>

<p>Each letter has a value (see the table below). A word's value, for this task's purposes, is the sum of values of each of the letters. Thus, the word "TAX" has three letters, each with a value: "T" with 1 point, "A" with 1 point, and "X" with 8 point -- total: 10 points. No other bonus points are considered in this task. Bessie might use one, some, or all of her letters to make the highest scoring word.</p>

<p>This game also includes blank letters (which are represented as "#" in the input). Blank letters can be used to represent any other letter but receives 0 points no matter which letter is chosen. Only three of the test data inputs will contain one or more blanks. Each blank letter can, if desired, represent a different actual letter for purposes of forming words.</p>

<p>Given T and a set of T letters, read the dictionary from file dict.txt (which is alphabetized and has fewer than 25,000 words; each word is no longer than 20 characters) and determine which is the most valuable word that can be made from Bessie's letters. If two words have the same value, choose the one that comes first alphabetically.</p>

<p>The actual dictionary used in this task is available at <a href="https://upload.acmicpc.net/0af412b5-ec50-4f94-a9b6-530c321a70d2/">dict.txt</a>. Bessie can always find some word in that dictionary to form with her letters.</p>

<pre>Letter values:
     0 points:  # (blank)
     1 point:   A, E, I, L, N, O, R, S, T, U
     2 points:  D, G
     3 points:  B, C, M, P
     4 points:  F, H, V, W, Y
     5 points:  K
     8 points:  J, X
     10 points: Q, Z</pre>

### 입력 

 <ul>
	<li>Line 1: A single integer: T</li>
	<li>Lines 2..T+1: Each line has a single character that appears in Bessie's letter tray</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single line with a single word (the word -- no '#' blanks) that is the highest-scoring word Bessie can make.</li>
</ul>

