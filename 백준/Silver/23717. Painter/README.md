# [Silver IV] Painter - 23717 

[문제 링크](https://www.acmicpc.net/problem/23717) 

### 성능 요약

메모리: 118108 KB, 시간: 396 ms

### 분류

문자열(string)

### 문제 설명

<p>You have recently started to study how to paint, and in one of the first classes you learned about the three primary colors: <i>Red</i>, <i>Yellow</i>, and <i>Blue</i>. If you combine these colors, you can produce many more colors. For now, the combinations that you have studied are the following:</p>

<ul>
	<li><i>Red</i> + <i>Yellow</i> = <i>Orange</i></li>
	<li><i>Red</i> + <i>Blue</i> = <i>Purple</i></li>
	<li><i>Yellow</i> + <i>Blue</i> = <i>Green</i></li>
	<li><i>Red</i> + <i>Yellow</i> + <i>Blue</i> = <i>Gray</i></li>
</ul>

<p>You still do not understand shades of colors, therefore the proportion and order of each color in the combination does not matter. For example, combining <i>Red</i> and <i>Yellow</i> produces the same result as combining <i>Yellow</i> and <i>Red</i>, as well as the same result as combining <i>Red</i>, <i>Yellow</i>, and <i>Red</i> again.</p>

<p>To practice your skills, you want to paint a 1-dimensional painting $P$ of length $N$. Your painting consists of $N$ squares. From left to right, $P_i$ represents the color of the $i-th square. Initially all squares are <i>Uncolored</i>, that is, $P_i$ = <i>Uncolored</i> for every $1≤i≤N$.</p>

<p>In a single stroke, you can choose one of the three primary colors and apply it to a sequence of consecutive squares. In other words, you can choose a color $c$ and two integers $l$ and $r$, such that $1≤l≤r≤N$, and apply color $c$ to all squares $P_j$ such that $l≤j≤r$. If the square being painted is currently <i>Uncolored</i>, then its color will become $c$. Otherwise, the color will be a combination of all the colors applied on this square so far and the new color $c$, as described in the list above.</p>

<p>In order to save time, you want to use as few strokes as possible. Given the description of the painting that you want to paint, figure out what is the minimum number of strokes required to paint it.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, $T$. $T$ test cases follow.</p>

<p>Each test case starts with a line containing an integer $N$, representing the length of the painting. Then on the next line, there will be a string $P$ of length $N$, representing the painting. The $i$-th character represents the color of square $P_i$, according to the following list:</p>

<ul>
	<li><code>U</code> = <i>Uncolored</i></li>
	<li><code>R</code> = <i>Red</i></li>
	<li><code>Y</code> = <i>Yellow</i></li>
	<li><code>B</code> = <i>Blue</i></li>
	<li><code>O</code> = <i>Orange</i></li>
	<li><code>P</code> = <i>Purple</i></li>
	<li><code>G</code> = <i>Green</i></li>
	<li><code>A</code> = <i>Gray</i></li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where $x$ is the test case number (starting from 1) and $y$ is the minimum number of strokes required to paint the painting.</p>

