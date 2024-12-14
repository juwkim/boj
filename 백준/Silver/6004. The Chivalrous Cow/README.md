# [Silver II] The Chivalrous Cow - 6004 

[문제 링크](https://www.acmicpc.net/problem/6004) 

### 성능 요약

메모리: 114200 KB, 시간: 124 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 12월 15일 02:18:47

### 문제 설명

<p>Farmer John traded one of his cows for a cow that Farmer Don called 'The Knight'. This cow has the unique ability to jump around the pasture in moves that looked like a knight on a chessboard (two squares over, one up... or maybe two squares down and one over, etc.). 'The Knight' can't jump on rocks or trees, but can really make her way around the pasture, which is partitioned for our purposes into an X by Y set of squares (1 <= X <= 150; 1 <= Y <= 150).</p>

<p>'The Knight' likes hay just like any other cow. Given a map of 'The Knight's starting place, locations of the tree, shrub, rock, and other obstacles, and the location of a bale of hay, determine how many 'hops' the Knight must make in order to get to the hay. The Knight cow will be marked by a 'K' on the map; obstacles by '*', and the haybale by 'H'. Here's a typical map:</p>

<pre>                    11 | . . . . . . . . . .
                    10 | . . . . * . . . . . 
                     9 | . . . . . . . . . . 
                     8 | . . . * . * . . . . 
                     7 | . . . . . . . * . . 
                     6 | . . * . . * . . . H 
                     5 | * . . . . . . . . . 
                     4 | . . . * . . . * . . 
                     3 | . K . . . . . . . . 
                     2 | . . . * . . . . . * 
                     1 | . . * . . . . * . . 
                     0 ----------------------
                                           1 
                       0 1 2 3 4 5 6 7 8 9 0 </pre>

<p>The knight could travel the path indicated by A, B, C, ... to get to the hay bale in just 5 moves (other routes of length 5 might be possible):</p>

<pre>                    11 | . . . . . . . . . .
                    10 | . . . . * . . . . .
                     9 | . . . . . . . . . .
                     8 | . . . * . * . . . .
                     7 | . . . . . . . * . .
                     6 | . . * . . * . . . F<
                     5 | * . B . . . . . . .
                     4 | . . . * C . . * E .
                     3 | .>A . . . . D . . .
                     2 | . . . * . . . . . *
                     1 | . . * . . . . * . .
                     0 ----------------------
                                           1
                       0 1 2 3 4 5 6 7 8 9 0</pre>

<p>Hint: This problem is probably most easily solved with a simple first-in/first-out 'queue' data structure implemented as a few parallel arrays.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: X and Y</li>
	<li>Lines 2..Y+1: Line Y-i+2 contains X characters with no spaces (i.e., the map is read in as shown in the text above): map row i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the minimum number of hops to get to the hay bale. It is always possible to get to the haybale.</li>
</ul>

<p> </p>

