# [Silver IV] Square Tiles (Small) - 12491 

[문제 링크](https://www.acmicpc.net/problem/12491) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘(bruteforcing), 그리디 알고리즘(greedy)

### 문제 설명

<p>You are selling beautiful geometric pictures. Each one consists of 1x1 square tiles arranged into a non-overlapping grid. For example:</p>

<pre>    . ## . .
    . ####
    . ####
    . ## . .
</pre>

<p>Blue tiles are represented by '#' characters, and white tiles are represented by '.' characters. You do not use other colors.</p>

<p> </p>

<p>Not everybody likes blue though, and some customers want you to replace all the blue tiles in your picture with red tiles. Unfortunately, red tiles only come in the larger 2x2 size, which makes this tricky.</p>

<p>You can cover any 2x2 square of blue tiles with a single red tile, and then repeat until finished. A red tile cannot overlap another red tile, it cannot cover white tiles, and it cannot go outside the picture. For example, you could add red tiles to the previous picture as follows:</p>

<pre>    . /\ . .
    . \/ /\
    . /\ \/
    . \/ . .
</pre>

<p>Each red tile is represented here by a pair of '/' characters in the top-left and bottom-right corners, and a pair of '\' characters in the other two corners.</p>

<p>Given a blue and white picture, can you transform it into a red and white picture in this way?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow.</p>

<p>Each test case begins with a line containing <strong>R</strong> and <strong>C</strong>, the number of rows and columns in a picture. The next <strong>R</strong> lines each contain exactly <strong>C</strong> characters, describing the picture. As above, '#' characters represent blue tiles, and '.' characters represent white tiles.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 20.</li>
	<li>1 ≤ <strong>R</strong> ≤ 6.</li>
	<li>1 ≤ <strong>C</strong> ≤ 6.</li>
</ul>

### 출력 

 <p>For each test case, first output one line containing "Case #x:" where x is the case number (starting from 1).</p>

<p>If it is possible to cover the blue tiles with non-overlapping red tiles, output <strong>R</strong> lines each containing <strong>C</strong> characters, describing the resulting red and white picture. As above, red tiles should be represented by '/' and '\' characters, while white tiles are represented by '.' characters. If multiple solutions are possible, you may output any of them.</p>

<p>If the task is impossible, output a single line containing the text "Impossible" instead.</p>

