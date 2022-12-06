# [Bronze III] Golf - 6437 

[문제 링크](https://www.acmicpc.net/problem/6437) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

구현(implementation)

### 문제 설명

<p>Whoever wants to learn the game of golf has to cope with several oddities first (as with every other game that originates from Great Britain). One of them is the way to count the number of strokes a player needed to put his golf ball in a hole. There is a "par" for every hole, and practically all scores are expressed relative to the par. Examples are terms like "par", "birdie" (1 below par) and "bogey" (1 over par), and, in rare cases, "hole-in-one", "eagle" (2 below par), "double eagle" (3 below par) and "double bogey" (2 over par). Although it is possible to get worse than a double bogey and there are names for those, too, we will just assume that most people will cheat and just write down "double bogey", anyway.</p>

<p>John has just joined a golf club and is new to all these names. On his first visit to the golf course, he just fills in the number of strokes for every hole in his score card. He now needs these numbers translated into their proper names.</p>

<p>As John's caddy, you are to write a program that, given the par for a hole and the number of strokes John wrote down, prints the proper name of the score. Make sure that you write a "hole-in-one" even if another description would fit as well.</p>

### 입력 

 <p>The input file consists of several test cases. Each test case consists of a single line that contains two integers <i>p</i> and <i>s</i>, where <i>p</i> is the par for the hole (either 3, 4, or 5) and <i>s</i> is the number of strokes John needed for that hole, 1 ≤ <i>s</i> < 20.</p>

<p>The input ends with a hole having <i>p </i>= 0, which should not be processed.</p>

### 출력 

 <p>For each test case, output a line containing the number of the hole (<tt>'Hole #1'</tt>, <tt>'Hole #2'</tt>, etc.).</p>

<p>On the next line print the proper name of the score, followed by a period, i.e. one of <tt>'Hole-in-one.'</tt>, <tt>'Double eagle.'</tt>, <tt>'Eagle.'</tt>, <tt>'Birdie.'</tt>, <tt>'Par.'</tt>, <tt>'Bogey.'</tt>, or <tt>'Double Bogey.'</tt>.</p>

