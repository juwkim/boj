# [Silver IV] Captain Hammer (Small) - 12084 

[문제 링크](https://www.acmicpc.net/problem/12084) 

### 성능 요약

메모리: 115552 KB, 시간: 360 ms

### 분류

이분 탐색(binary_search), 수학(math), 물리학(physics)

### 문제 설명

<p>The Hamjet is a true marvel of aircraft engineering. It is a jet airplane with a single engine so powerful that it burns all of its fuel instantly during takeoff. The Hamjet doesn't have any wings because who needs them when the fuselage is made of a special Wonderflonium isotope that makes it impervious to harm.</p>

<p>Piloting the Hamjet is a not a job for your typical, meek-bodied superhero. That's why the Hamjet belongs to Captain Hammer, who is himself impervious to harm. The G-forces that the pilot endures when taking a trip in the Hamjet are legen-dary.</p>

<p>The Hamjet takes off at an angle of θ degrees up and a speed of <strong>V</strong> meters per second. <strong>V</strong>is a fixed value that is determined by the awesome power of the Hamjet engine and the capacity of its fuel tank. The destination is <strong>D</strong> meters away. Your job is to program the Hamjet's computer to calculate θ given <strong>V</strong> and <strong>D</strong>.</p>

<p>Fortunately, the Hamjet's Wondeflonium hull is impervious to air friction. Even more fortunately, the Hamjet doesn't fly too far or too high, so you can assume that the Earth is flat, and that the acceleration due to gravity is a constant 9.8 m/s<sup>2</sup> down.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> lines follow. Each line will contain two positive integers -- <strong>V</strong> and <strong>D</strong>.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 4500;</li>
	<li>1 ≤ <strong>V</strong> ≤ 300;</li>
	<li>1 ≤ <strong>D</strong> ≤ 10000;</li>
	<li>It is guaranteed that each test case will be solvable.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: θ", where x is the case number (starting from 1) and θ is in degrees up from the the horizontal. If there are several possible answers, output the smallest positive one.</p>

<p>An answer will be considered correct if it is within 10<sup>-6</sup> of the exact answer, in absolute or relative error. See the <a href="https://code.google.com/codejam/faq.html#floating_point" style="color: rgb(85, 26, 139);" target="_blank">FAQ</a> for an explanation of what that means, and what formats of floating-point numbers we accept.</p>

