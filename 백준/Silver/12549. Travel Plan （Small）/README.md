# [Silver I] Travel Plan (Small) - 12549 

[문제 링크](https://www.acmicpc.net/problem/12549) 

### 성능 요약

메모리: 112588 KB, 시간: 3276 ms

### 분류

백트래킹, 브루트포스 알고리즘, 구현

### 제출 일자

2025년 8월 14일 00:42:28

### 문제 설명

<p>In a yet-to-be-announced and rechecked discovery by Antarctic astronomers, it is written that there are <strong>N</strong> inhabited planets in space, all lying along the same straight line, with the <strong>i</strong>-th planet lying at coordinate <strong>X</strong><sub><strong>i</strong></sub> along the line (<strong>i</strong> = 1, 2, ..., <strong>N</strong>). Earth is the first planet, lying at coordinate zero, so <strong>X</strong><sub>1</sub> will always be equal to 0.</p>

<p>Being very excited about this fact, you start planning a trip to visit all the planets. Since unknown planets can be dangerous, you want to visit each planet exactly once before returning to Earth. You have <strong>F</strong> units of fuel, and you want to spend as much of it on this trip as possible so that your final landing on Earth is safer. Your spaceship is pretty basic and can only fly along a straight line from any planet <strong>i</strong> to any other planet <strong>j</strong>, consuming |<strong>X</strong><sub><strong>i</strong></sub>-<strong>X</strong><sub><strong>j</strong></sub>| units of fuel along the way. It can't turn without landing.</p>

<p>So you need to create a travel plan that requires at most <strong>F</strong> units of fuel, starts from Earth, visits each of the other planets exactly once, and then returns to Earth. If there are several such plans, you should find the one that consumes most fuel. Output the amount of fuel consumed.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> test cases follow. Each test case description starts with a line containing the number of planets <strong>N</strong>. The next line contains <strong>N</strong> numbers <strong>X</strong><sub><strong>i</strong></sub>, the coordinates of the planets. The next line contains the amount of fuel <strong>F</strong> that you have.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>F</strong> ≤ 10<sup>17</sup>.</li>
	<li>-10<sup>15</sup> ≤ <strong>X</strong><sub>i</sub> ≤ 10<sup>15</sup>.</li>
	<li><strong>X</strong><sub>1</sub>=0.</li>
	<li>All <strong>X</strong><sub>i</sub> are different.</li>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>2 ≤ <strong>N</strong> ≤ 10.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing either "Case #x: NO SOLUTION", when there's no such travel plan, or "Case #x: y", where x is the case number (starting from 1) and y is the maximum amount of fuel consumed.</p>

