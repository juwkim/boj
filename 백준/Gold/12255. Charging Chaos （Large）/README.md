# [Gold IV] Charging Chaos (Large) - 12255 

[문제 링크](https://www.acmicpc.net/problem/12255) 

### 성능 요약

메모리: 111420 KB, 시간: 144 ms

### 분류

백트래킹, 비트마스킹, 브루트포스 알고리즘, 정렬

### 제출 일자

2025년 1월 7일 22:05:14

### 문제 설명

<p>Shota the farmer has a problem. He has just moved into his newly built farmhouse, but it turns out that the outlets haven't been configured correctly for all of his devices. Being a modern farmer, Shota owns a large number of smartphones and laptops, and even owns a tablet for his favorite cow Wagyu to use. In total, he owns <strong>N</strong> different devices.</p>

<p>As these devices have different specifications and are made by a variety of companies, they each require a different electric flow to charge. Similarly, each outlet in the house outputs a specific electric flow. An electric flow can be represented by a string of 0s and 1s of length <strong>L</strong>.</p>

<p>Shota would like to be able to charge all <strong>N</strong> of his devices at the same time. Coincidentally, there are exactly <strong>N</strong> outlets in his new house. In order to configure the electric flow from the outlets, there is a master control panel with <strong>L</strong> switches. The i<sup>th</sup> switch flips the i<sup>th</sup> bit of the electric flow from each outlet in the house. For example, if the electric flow from the outlets is:</p>

<p>Outlet 0: 10</p>

<p>Outlet 1: 01</p>

<p>Outlet 2: 11</p>

<p>Then flipping the second switch will reconfigure the electric flow to:</p>

<p>Outlet 0: 1<strong>1</strong></p>

<p>Outlet 1: 0<strong>0</strong></p>

<p>Outlet 2: 1<strong>0</strong></p>

<p>If Shota has a smartphone that needs flow "11" to charge, a tablet that needs flow "10" to charge, and a laptop that needs flow "00" to charge, then flipping the second switch will make him very happy!</p>

<p>Misaki has been hired by Shota to help him solve this problem. She has measured the electric flows from the outlets in the house, and noticed that they are all different. Decide if it is possible for Shota to charge all of his devices at the same time, and if it is possible, figure out the minimum number of switches that needs to be flipped, because the switches are big and heavy and Misaki doesn't want to flip more than what she needs to.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case consists of three lines. The first line contains two space-separated integers <strong>N</strong> and <strong>L</strong>. The second line contains <strong>N</strong> space-separated strings of length <strong>L</strong>, representing the initial electric flow from the outlets. The third line also contains <strong>N</strong> space-separated strings of length <strong>L</strong>, representing the electric flow required by Shota's devices.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>No two outlets will be producing the same electric flow, initially.</li>
	<li>No two devices will require the same electric flow.</li>
	<li>1 ≤ <strong>N</strong> ≤ 150.</li>
	<li>10 ≤ <strong>L</strong> ≤ 40.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>x</strong>: <strong>y</strong>", where <strong>x</strong> is the case number (starting from 1) and <strong>y</strong> is the minimum number of switches to be flipped in order for Shota to charge all his devices. If it is impossible, <strong>y</strong> should be the string "NOT POSSIBLE" (without the quotes). We suggest copying/pasting the string NOT POSSIBLE into your code.</p>

