# [Gold II] Pony Express (Large) - 14808 

[문제 링크](https://www.acmicpc.net/problem/14808) 

### 성능 요약

메모리: 115076 KB, 시간: 412 ms

### 분류

플로이드–워셜, 그래프 이론, 최단 경로

### 제출 일자

2025년 5월 4일 01:22:57

### 문제 설명

<p>It's the year 1860, and the Pony Express is the fastest mail delivery system joining the East and West coasts of the United States. This system serves <strong>N</strong> different cities. In each city, there is one horse (as in the expression "one-horse town"); each horse travels at a certain constant speed and has a maximum total distance it can travel before it becomes too tired to continue.</p>

<p>The Pony Express rider starts off on the starting city's horse. Every time the rider reaches a city, they may continue to use their current horse or switch to that city's horse; switching is instantaneous. Horses never get a chance to rest, so whenever part of a horse's maximum total distance is "used up", it is used up forever! When the rider reaches the destination city, the mail is delivered.</p>

<p>The routes between cities were established via complicated negotiations between company owners, lawmakers, union delegates, and cousin Pete. That means that the distances between cities do not necessarily follow common sense: for instance, they do not necessarily comply with the triangle inequality, and the distance from city A to city B might be different from the distance from city B to city A!</p>

<p>You are a time traveling entrepreneur, and you have brought a fast computer from the future. A single computer is not enough for you to set up an e-mail service and make the Pony Express obsolete, but you can use it to make optimal routing plans for the Pony Express. Given all data about routes between cities and the horses in each city, and a list of pairs of starting and ending cities, can you quickly calculate the minimum time necessary for each delivery? (You should treat all of these deliveries as independent; using cities/horses on one route does not make them unavailable on other routes.)</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case is described as follows:</p>

<ul>
	<li>One line with two integers: <strong>N</strong>, the number of cities with horses, and <strong>Q</strong>, the number of pairs of stops we are interested in. Cities are numbered from 1 to <strong>N</strong>.</li>
	<li><strong>N</strong> lines, each containing two integers <strong>E</strong><sub>i</sub>, the maximum total distance, in kilometers, the horse in the i-th city can go and <strong>S</strong><sub>i</sub>, the constant speed, in kilometers per hour, at which the horse travels.</li>
	<li><strong>N</strong> lines, each containing <strong>N</strong> integers. The j-th integer on the i-th of these lines, <strong>D</strong><sub>ij</sub>, is -1 if there is no direct route from the i-th to the j-th city, and the length of that route in kilometers otherwise.</li>
	<li><strong>Q</strong> lines containing two integers <strong>U</strong><sub>k</sub> and <strong>V</strong><sub>k</sub>, the starting and destination point, respectively, of the k-th pair of cities we want to investigate.</li>
</ul>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>2 ≤ <strong>N</strong> ≤ 100.</li>
	<li>1 ≤ <strong>E</strong><sub>i</sub> ≤ 10<sup>9</sup>, for all i.</li>
	<li>1 ≤ <strong>S</strong><sub>i</sub> ≤ 1000, for all i.</li>
	<li>-1 ≤ <strong>D</strong><sub>ij</sub> ≤ 10<sup>9</sup>, for all i, j.</li>
	<li><strong>D</strong><sub>ii</sub> = -1, for all i. (There are no direct routes from a city to itself.)</li>
	<li><strong>D</strong><sub>ij</sub> ≠ 0, for all i, j.</li>
	<li><strong>U</strong><sub>k</sub> ≠ <strong>V</strong><sub>k</sub>, for all k.</li>
	<li>It is guaranteed that the delivery from <strong>U</strong><sub>k</sub> to <strong>V</strong><sub>k</sub> can be accomplished with the given horses, for all k.</li>
	<li><strong>U</strong><sub>l</sub> ≠ <strong>U</strong><sub>m</sub> and/or <strong>V</strong><sub>l</sub> ≠ <strong>V</strong><sub>m</sub>, for all different l, m. (No ordered pair of cities to investigate is repeated within a test case.)</li>
	<li>1 ≤ <strong>Q</strong> ≤ 100.</li>
	<li>1 ≤ <strong>U</strong><sub>k</sub> ≤ <strong>N</strong>, for all k.</li>
	<li>1 ≤ <strong>V</strong><sub>k</sub> ≤ <strong>N</strong>, for all k.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y<sub>1</sub> y<sub>2</sub> ... y<sub><strong>Q</strong></sub></code>, where <code>x</code> is the test case number (starting from 1) and <code>y<sub>k</sub></code> is the minimum time, in hours, to deliver a letter from city <strong>U</strong><sub>k</sub> to city <strong>V</strong><sub>k</sub>.</p>

<p>Each <code>y<sub>k</sub></code> will be considered correct if it is within an absolute or relative error of 10<sup>-6</sup> of the correct answer.</p>

