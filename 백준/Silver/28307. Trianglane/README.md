# [Silver V] Trianglane - 28307 

[문제 링크](https://www.acmicpc.net/problem/28307) 

### 성능 요약

메모리: 162336 KB, 시간: 208 ms

### 분류

다이나믹 프로그래밍

### 문제 설명

<p>Bocchi the Builder has just finished constructing her latest project: a pathway consisting of two rows of white equilateral triangular tiles. However, at the last moment, disaster struck, and she accidentally spilled black paint on some of the tiles! Now, she must purchase warning tape to block off the wet areas. Can you help her determine how many meters of tape she needs?</p>

<p>The first triangle will always point upwards, and any pair of adjacent tiles (that is, tiles that share a common side) will point in opposite directions. Every triangle has a side length of 1 meter.</p>

### 입력 

 <p>The first line will consist of one integer, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$C$</span></mjx-container>, representing the number of columns.</p>

<p>The next two lines will each consist of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$C$</span></mjx-container> integers separated by spaces. Each integer represents the colour of a tile in the room, with 1 indicating that the tile is black and 0 indicating that the tile is white.</p>

### 출력 

 <p>Output a single integer representing the length of the tape Bocchi must purchase in meters.</p>

