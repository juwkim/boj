# [Silver II] Space Coconut Crab II - 13827 

[문제 링크](https://www.acmicpc.net/problem/13827) 

### 성능 요약

메모리: 111608 KB, 시간: 620 ms

### 분류

브루트포스 알고리즘, 수학, 정수론, 소수 판정, 에라토스테네스의 체

### 제출 일자

2025년 1월 7일 22:23:30

### 문제 설명

<p>A space hunter, Ken Marineblue traveled the universe, looking for the space coconut crab. The space coconut crab was a crustacean known to be the largest in the universe. It was said that the space coconut crab had a body of more than 400 meters long and a leg span of no shorter than 1000 meters long. Although there were numerous reports by people who saw the space coconut crab, nobody have yet succeeded in capturing it.</p>

<p>After years of his intensive research, Ken discovered an interesting habit of the space coconut crab. Surprisingly, the space coconut crab went back and forth between the space and the hyperspace by phase drive, which was the latest warp technology. As we, human beings, was not able to move to the hyperspace, he had to work out an elaborate plan to capture them. Fortunately, he found that the coconut crab took a long time to move between the hyperspace and the space because it had to keep still in order to charge a sufficient amount of energy for phase drive. He thought that he could capture them immediately after the warp-out, as they moved so slowly in the space.</p>

<p>He decided to predict from the amount of the charged energy the coordinates in the space where the space coconut crab would appear, as he could only observe the amount of the charged energy by measuring the time spent for charging in the hyperspace. His recent spaceship, Weapon Breaker, was installed with an artificial intelligence system, CANEL. She analyzed the accumulated data and found another surprising fact; the space coconut crab always warped out near to the center of a triangle that satisfied the following conditions:</p>

<ul>
	<li>each vertex of the triangle was one of the planets in the universe;</li>
	<li>the length of every side of the triangle was a prime number; and</li>
	<li>the total length of the three sides of the triangle was equal to T, the time duration the space coconut crab had spent in charging energy in the hyperspace before moving to the space.</li>
</ul>

<p>CANEL also devised the method to determine the three planets comprising the triangle from the amount of energy that the space coconut crab charged and the lengths of the triangle sides. However, the number of the candidate triangles might be more than one.</p>

<p>Ken decided to begin with calculating how many different triangles were possible, analyzing the data he had obtained in the past research. Your job is to calculate the number of different triangles which satisfies the conditions mentioned above, for each given T.</p>

### 입력 

 <p>The input consists of multiple datasets. Each dataset comes with a line that contains a single positive integer T (1 ≤ T ≤ 30000).</p>

<p>The end of input is indicated by a line that contains a zero. This should not be processed.</p>

### 출력 

 <p>For each dataset, print the number of different possible triangles in a line. Two triangles are different if and only if they are not congruent.</p>

