# [Silver I] Food portion size - 6499 

[문제 링크](https://www.acmicpc.net/problem/6499) 

### 성능 요약

메모리: 129780 KB, 시간: 1368 ms

### 분류

애드 혹, 브루트포스 알고리즘

### 제출 일자

2025년 8월 16일 12:54:41

### 문제 설명

<p>The university canteen does not want any student to leave the canteen hungry. Therefore, as long as a student is hungry, he can get another portion of food for free. The canteen uses a fixed food portion size, because it would take too much time to first ask a student how much food he wanted. It can happen that a student doesn't finish his last portion of food and the remainder has to be thrown away.</p>

<p>To minimize costs, the manager of the canteen wants to determine a food portion size <em>S</em> such that the amount of food that is wasted is small, but also the number of times the students have to fetch another portion of food is not too big. Note that these two goals can be conflicting:</p>

<ul>
	<li>By choosing a very small food portion size, one does not waste food, but simultaneously the number of times the students have to fetch food is big.</li>
	<li>By choosing a large food portion size, one can make sure each student has to fetch only one portion, but at the same time it may happen that a large quantity of food is wasted.</li>
</ul>

<p>The manager of the canteen has collected data about how many units of food each student eats. The problem to be solved can now be formulated mathematically as follows: Let <em>x</em> be the amount of food that is wasted, and <em>y</em> the number of times the students go to fetch food. Then, the goal is to minimize <em>a × x + b × y</em>, where <em>a, b</em> are weights that represent the relative importance of the two opposing goals. Note that <em>x</em> and <em>y</em> depend on the food portion size <em>S</em> and the quantities of food each student eats. We impose the additional constraint that no student should have to go more than 3 times to fetch food.</p>

### 입력 

 <p>The input file contains several test cases. Each test case starts with a line containing an integer <em>n</em>, (<em>1 ≤ n ≤ 1000</em>), the number of students eating in the canteen. The next line contains the values <em>a</em> and <em>b</em> (<em>1 ≤ a, b ≤ 10</em>). The third line of each test case consists of <em>n</em> integers <em>y<sub>1</sub>, ..., y<sub>n</sub></em> (<em>1 ≤ y<sub>i</sub> ≤ 100</em>), where <em>y<sub>i</sub></em> is the amount of food student <em>i</em> eats. Input is terminated by <em>n=0</em>.</p>

### 출력 

 <p>For each test case print one line containing the costs resulting from an optimal choice of the food portion size. Print each value as a reduced fraction. If the result is an integer, do not print the denominator 1. See the sample output for details.</p>

