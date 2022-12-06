# [Bronze I] Set! - 24777 

[문제 링크](https://www.acmicpc.net/problem/24777) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p><img alt="" src="" style="width: 250px; height: 208px; float: right;">Set is a card game designed by Marsha Falco in 1974 which is marketed by Set Enterprises, Inc. It also appears in syndicated form on the website of the New York Times.  The player is shown 12 cards (see illustration), each of which contains 1, 2, or 3 symbols. The symbols are either diamonds, squiggles, or ovals.  Symbols are drawn using either a solid, striped, or open fill style.  Each symbol's color is either red, green, or purple. On a given card, all symbols are of the same type, same color, and have the same fill style.</p>

<p>To make a set, you must select three cards for which all 4 characteristics are either the same or pairwise different.  For instance, 3 cards where the first shows 2 striped red ovals, the second shows 3 striped green squiggles, and the third shows 1 striped purple diamond form a set.  They show 2, 3, and 1 symbols (each has a different number); they show ovals, squiggles, and diamonds (each shows a different shape); they use colors red, green, and purple (3 different colors); and lastly, they all share the same fill style: striped.</p>

<p>Write a program that finds all sets for 12 provided cards!</p>

### 입력 

 <p>The input to your program will consist of 4 lines, each containing 3 strings representing 3 cards, each is of the form <code>ABCD</code> where</p>

<ul>
	<li><code>A</code> is <code>{1, 2, 3</code>}, corresponding to the number of symbols.</li>
	<li><code>B</code> is <code>{D, S, O</code>}, corresponding to diamonds (D), squiggles (S), and ovals (O).</li>
	<li><code>C</code> is <code>{S, T, O</code>}, corresponding to solid (S), striped (T), and open (O) fill styles.</li>
	<li><code>D</code> is <code>{R, G, P</code>}, corresponding to red (R), green (G), and purple (P). \end{itemize}</li>
</ul>

<p>Think of the cards as being arranged in the input as follows:</p>

<pre>+----------+
|  1  2  3 |
|  4  5  6 |
|  7  8  9 |
| 10 11 12 |
+----------+</pre>

### 출력 

 <p>Output all sets you can find, one per line. For each set, output the numbers of the card in the set in sorted order. The sets should be listed in sorted order using the  number of their first card, breaking ties using the numbers of the second and third card in the set.</p>

<p>If no sets can be formed, output "<code>no sets</code>". (Do not include any punctuation.)</p>

<p>The sample input/output corresponds to the illustration.</p>

