# [Bronze I] City of Lights - 17554 

[문제 링크](https://www.acmicpc.net/problem/17554) 

### 성능 요약

메모리: 122144 KB, 시간: 124 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Paris has been called “ville lumière” (city of lights) since the 17th century. It earned this nickname in part because of the many city lights illuminating famous sites such as monuments, statues, churches, or fountains.</p>

<p>Those public lights in Paris are numbered from 1 to N and are all on by default. A group of hackers has gained the capability to toggle groups of lights. Every time the hackers use their program, they cause a number i (that they cannot control) to be sent to the system controlling the city lights. The lights numbered i, 2i, 3i, and so on (up to N) then change state instantly: lights that were on go off, and lights that were off go on.</p>

<p>During the night, the hackers use their programs k times. What is the greatest number of lights that are simultaneously off at the same time?</p>

### 입력 

 <p>The input comprises several lines, each consisting of a single integer:</p>

<ul>
	<li>The first line contains the number N of lights.</li>
	<li>The second line contains the number k of uses hackers’s program.</li>
	<li>The next k lines contain a number i sent to the system controlling the lights.</li>
</ul>

### 출력 

 <p>The output should consist of a single line, whose content is an integer, the greatest number of lights that are simultaneously off at the same time.</p>

