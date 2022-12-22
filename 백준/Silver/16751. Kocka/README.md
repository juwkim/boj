# [Silver V] Kocka - 16751 

[문제 링크](https://www.acmicpc.net/problem/16751) 

### 성능 요약

메모리: 128564 KB, 시간: 132 ms

### 분류

수학(math)

### 문제 설명

<blockquote>
<p>I’m again in the cube!<br>
I’m again in the cube!</p>
</blockquote>

<p>While watching the kids’ playground in the early morning hours, the author of this task caught sight of an interesting object: a cube made out of metal bars, composed of many unit-sized cubes made out of metal bars.</p>

<p>While observing the cube, an interesting problem came to his mind. Here follows the two-dimensional version of the problem, since nobody likes problems involving 3D objects:</p>

<p>You’re given N × N matrix (square for reference). Some of the fields in the square are blocked and some are empty. The author was watching the square from each of its 4 sides. Firstly, he looked at the square from its left side, and for each of its N rows he wrote how many empty field there were in the row in front of the first blocked field he could see. If there were no blocked fields in a row, he wrote down the number -1. Then he repeated the same procedure looking at the square from its right, top and bottom side, in that order.</p>

<p>By doing so, he wrote 4N numbers in total, as he wrote N numbers for each side of the square. However, unknown villains destroyed his square and the only thing left were the numbers he had written down. The author of the task wonders if those numbers make any sense, i.e. if it is possible to form a square for which the same sequence of numbers will be obtained by doing the described procedure.</p>

### 입력 

 <p>The first line contains a positive integer N (1 ≤ N ≤ 100 000), dimension of the square.</p>

<p>The second line contains N integers L<sub>i</sub> (-1 ≤ L<sub>i</sub> < N), numbers obtained by watching the square from its left side, in order from 1<sup>st</sup> to N<sup>th</sup> row.</p>

<p>The third line contains N integers R<sub>i</sub> (-1 ≤ R<sub>i</sub> < N), numbers obtained by watching the square from its right side, in order from 1st to N<sup>th</sup> row.</p>

<p>The fourth line contains N integers U<sub>i</sub> (-1 ≤ U<sub>i</sub> < N), numbers obtained by watching the square from its top side, in order from 1<sup>st</sup> to N<sup>th</sup> column.</p>

<p>The fifth line contains N integers D<sub>i</sub> (-1 ≤ D<sub>i</sub> < N), numbers obtained by watching the square from its bottom side, in order from 1<sup>st</sup> to N<sup>th</sup> column.</p>

### 출력 

 <p>If it is possible to from a square which satisfies the given conditions, print “DA” (Croatian for yes, without quotation marks), otherwise print “NE” (Croatian for no).</p>

