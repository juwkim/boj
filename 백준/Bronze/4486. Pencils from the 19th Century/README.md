# [Bronze II] Pencils from the 19th Century - 4486 

[문제 링크](https://www.acmicpc.net/problem/4486) 

### 성능 요약

메모리: 30888 KB, 시간: 72 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math)

### 문제 설명

<p>Before “automaton” was a theoretic computer science concept, it meant “mechanical figure or contrivance constructed to act as if by its own motive power; robot.” Examples include fortunetellers, as shown above, but could also describe a pencil seller, moving pencils from several baskets to a delivery trough.</p>

<p>On National Public Radio, the Sunday Weekend Edition program has a “Sunday Puzzle” segment. The show that aired on Sunday, 29 June 2008, had the following puzzle for listeners to respond to (by Thursday, 3 July, at noon through the NPR web site):</p>

<blockquote>
<p>From a 19th century trade card advertising Bassetts Horehound Troches, a remedy for coughs and colds: A man buys 20 pencils for 20 cents and gets three kinds of pencils in return. Some of the pencils cost four cents each, some are two for a penny and the rest are four for a penny. How many pencils of each type does the man get?</p>
</blockquote>

<p>One clarification from the program of 6 July: correct solutions contain at least one of each pencil type.</p>

<p>For our purposes, we will expand on the problem, rather than just getting 20 pencils for 20 cents (which is shown in the sample output below). The input file will present a number of cases. For each case, give all solutions or print the text “No solution found”. Solutions are to be ordered by increasing numbers of four-cent pencils.</p>

### 입력 

 <p>Each line gives a value for N (2 ≤ N ≤ 256), and your program is to end when N=0 (at most 32 problems).</p>

### 출력 

 <p>The first line gives the instance, starting from 1, followed by a line giving the statement of the problem. Solutions are shown in the three-line format below followed by a blank line, or the single line “No solution found”, followed by a blank line. Note that by the nature of the problem, once the number of four-cent pencils is determined, the numbers of half-cent and quarter-cent pencils are also determined.</p>

<pre>Case n:
nn pencils for nn cents
nn at four cents each
nn at two for a penny
nn at four for a penny</pre>

