# [Silver IV] Appalling Architecture - 16293 

[문제 링크](https://www.acmicpc.net/problem/16293) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현(implementation), 물리학(physics)

### 문제 설명

<p>You have recently been hired as an architect for the BAPC (Bureau of Architecture and Promising Constructions), responsible for top-quality buildings such as the Tower of Pisa. However, in the past couple of weeks, some of the constructions that the BAPC has made have collapsed! It is up to you to figure out whether any other constructions are in danger.</p>

<p>After some research it seems like the x-coordinate of the center of gravity of some of the constructions is off: if this is too much to the left or to the right, the construction will fall over. Hence, you decide to check all the blueprints and see whether the constructions are stable or not.</p>

<p>Given is an up to 100 by 100 grid of characters in <code>.#/\_|-</code>. The <code>.</code> characters denote empty space, while each other character represents a completely filled 1 × 1 box (any difference in symbols used is due to the artistic freedom of the other architects), whose center of mass is at the center of the box.</p>

<p>Every construction forms a single connected component that touches the ground, i.e. the bottom layer of the grid.</p>

<p>The construction falls to the left if the x-coordinate of the center of gravity is less than the x-coordinate of the leftmost point of the construction that touches the ground, and it falls to the right if the x-coordinate of the center of gravity is larger than the x-coordinate of the rightmost point of the construction that touches the ground. It is guaranteed that the center of gravity is never exactly above the leftmost or rightmost point where the building touches the ground.</p>

<p>Given a blueprint, is the construction balanced, does it fall to the left, or does it fall to the right?</p>

### 입력 

 <ul>
	<li>The first line has 1 ≤ h ≤ 100 and 1 ≤ w ≤ 100, the height and width of the grid.</li>
	<li>Then follow h lines with l characters each. Each character is either <code>.</code>, indicating empty space, or one of <code>#/\_|-</code>, indicating a filled 1 × 1 box .</li>
</ul>

### 출력 

 <ul>
	<li>Print a single line containing left, balanced, or right.</li>
</ul>

