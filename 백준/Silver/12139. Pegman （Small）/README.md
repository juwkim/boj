# [Silver III] Pegman (Small) - 12139 

[문제 링크](https://www.acmicpc.net/problem/12139) 

### 성능 요약

메모리: 109240 KB, 시간: 112 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 2월 14일 03:10:28

### 문제 설명

<p>While using Google Street View, you may have picked up and dropped the character Pegman before. Today, a mischievous user is going to place Pegman in some cell of a rectangular grid of unit cells with <strong>R</strong> rows and <strong>C</strong> columns. Each of the cells in this grid might be blank, or it might be labeled with an arrow pointing in one of four possible directions: up, right, down, or left.<br>
<br>
When Pegman is placed on a grid cell, if that cell is blank, Pegman stands still forever. However, if that cell has an arrow, Pegman starts to walk in that direction. As he walks, whenever he encounters a blank cell, he just keeps walking in his current direction, but whenever he encounters another arrow, he changes to the direction of that arrow and then keeps walking.<br>
<br>
You know that it is possible that Pegman might keep happily walking around and around the grid forever, but it is also possible that Pegman's walk will take him over the edge of the grid! You may be able to prevent this and save him by changing the direction of one or more arrows. (Each arrow's direction can only be changed to one of the other three possible directions; arrows can only be changed, not added or removed.)<br>
<br>
What is the smallest number of arrows you will need to change to ensure that Pegman will not walk off the edge, no matter where on the grid he is initially placed?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each begins with one line with two space-separated integers <strong>R</strong>, <strong>C</strong>. This line is followed by <strong>R</strong>lines, each of which has <strong>C</strong> characters, each of which describes a grid cell and is one of the following:<br>
<br>
<code>. period = no arrow<br>
^ caret = up arrow<br>
> greater than = right arrow<br>
v lowercase v = down arrow<br>
< less than = left arrow</code></p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>R, C</strong> ≤ 4.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of arrows that must be changed to ensure that Pegman will not leave the grid no matter where he is initially placed, or the text <code>IMPOSSIBLE</code> if it is not possible to ensure this, no matter how many arrows you change.</p>

