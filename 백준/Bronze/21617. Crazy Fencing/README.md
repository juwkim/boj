# [Bronze II] Crazy Fencing - 21617 

[문제 링크](https://www.acmicpc.net/problem/21617) 

### 성능 요약

메모리: 29284 KB, 시간: 72 ms

### 분류

기하학(geometry), 수학(math)

### 문제 설명

<p>You need to paint a wooden fence between your house and your neighbour’s house. You want to determine the area of the fence, in order to determine how much paint you will use.</p>

<p>However, the fence is made out of N non-uniform pieces of wood, and your neighbour believes that they have an artistic flair. In particular, the pieces of wood may be of various widths. The bottom of each piece of wood will be horizontal, both sides will be vertical, but its top may be cut on an angle. Two such pieces of wood are shown below:</p>

<p style="text-align: center;"><img alt="" src="" style="width: 126px; height: 123px;"></p>

<p>Thankfully, the fence has been constructed so that adjacent pieces of wood have the same height on the sides where they touch, which makes the fence more visually appealing.</p>

### 입력 

 <p>The first line of the input will be a positive integer N, where N ≤ 10 000.</p>

<p>The second line of input will contain N + 1 space-separated integers h<sub>1</sub>, . . . , h<sub>N+1</sub> (1 ≤ h<sub>i</sub> ≤ 100, 1 ≤ i ≤ N + 1) describing the left and right heights of each piece of wood. Specifically, the left height of the i<sup>th</sup> piece of wood is h<sub>i</sub> and the right height of the i<sup>th</sup> piece of wood is h<sub>i+1</sub>.</p>

<p>The third line of input will contain N space-separated integers w<sub>i</sub> (1 ≤ w<sub>i</sub> ≤ 100, 1 ≤ i ≤ N) describing the width of the i<sup>th</sup> piece of wood.</p>

### 출력 

 <p>Output the total area of the fence. If the correct answer is C, the grader will view A correct if |A − C|≤10<sup>−6</sup>.</p>

