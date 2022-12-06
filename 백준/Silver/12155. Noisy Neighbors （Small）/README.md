# [Silver V] Noisy Neighbors (Small) - 12155 

[문제 링크](https://www.acmicpc.net/problem/12155) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>You are a landlord who owns a building that is an <strong>R</strong> x <strong>C</strong> grid of apartments; each apartment is a unit square cell with four walls. You want to rent out <strong>N</strong> of these apartments to tenants, with exactly one tenant per apartment, and leave the others empty. Unfortunately, all of your potential tenants are noisy, so whenever any two occupied apartments share a wall (and not just a corner), this will add one point of <em>unhappiness</em> to the building. For example, a 2x2 building in which every apartment is occupied has four walls that are shared by neighboring tenants, and so the building's unhappiness score is 4.<br>
<br>
If you place your <strong>N</strong> tenants optimally, what is the minimum unhappiness value for your building?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> lines follow; each contains three space-separated integers: <strong>R</strong>, <strong>C</strong>, and <strong>N</strong>.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 1000.</li>
	<li>0 ≤ <strong>N</strong> ≤ <strong>R*C</strong>.</li>
	<li>1 ≤ <strong>R*C</strong> ≤ 16.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum possible unhappiness for the building.</p>

