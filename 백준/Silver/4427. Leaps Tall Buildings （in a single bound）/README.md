# [Silver I] Leaps Tall Buildings (in a single bound) - 4427 

[문제 링크](https://www.acmicpc.net/problem/4427) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 물리학

### 제출 일자

2025년 8월 16일 03:23:37

### 문제 설명

<p><em>It's a bird! It's a plane! It's coming right at us!</em></p>

<p>Although it sometimes seems like it, Superman can't fly (without a plane). Instead, he makes super-human leaps, especially over tall buildings. Since he never knows when he will need to catch a criminal, he can't register flight paths. To avoid hitting planes, he tries to keep his jumps as low to the ground as he can. Given a city-scape as input, find the angle and velocity of Superman's jump that minimizes his maximum altitude.</p>

<p>Recall that gravity provides an acceleration of 9.8 m/s<sup>2</sup> downwards and the formula for Superman's vertical distance from his starting location is <var>d(t)</var>=<var>v</var> <var>t</var> + 0.5 <var>a</var> <var>t</var><sup>2</sup> where <var>v</var> is his initial velocity, <var>a</var> is his acceleration and <var>t</var> is time in seconds since the start of the leap.</p>

### 입력 

 <p>Input consists of a sequence of city-scapes, each of the form</p>

<pre>n
0 d<sub>1</sub>
h<sub>2</sub> d<sub>2</sub>
:
h<sub>(n-1)</sub> d<sub>(n-1)</sub>
0 d<sub>n</sub></pre>

<p>Superman starts at ground level and leaps d<sub>1</sub>+...+d<sub>n</sub> metres, landing at ground level and clearing all of the buildings at heights h<sub>2</sub> to h<sub>(n-1)</sub>, each with the given widths. n will be at most 100.</p>

### 출력 

 <p>Output is the angle and initial velocity that minimizes the height that Superman attains, both appearing on the same line. The values should be given to two decimal places and be accurate within 0.01 degrees or m/s, as appropriate.</p>

