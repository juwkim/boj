# [Gold V] Large Weird Measurements - 14009 

[문제 링크](https://www.acmicpc.net/problem/14009) 

### 성능 요약

메모리: 51672 KB, 시간: 308 ms

### 분류

다이나믹 프로그래밍(dp), 두 포인터(two_pointer)

### 문제 설명

<p><strong>"Almonds? Oh yeah, I have tried those before. Covered in chocolate."</strong> - Dudu, 2015.</p>

<p><strong>Note:</strong> This problem is identical to Small and Medium Weird Measurements, but with different bounds.</p>

<p>Dudu is trying to achieve a perfect beach body for his upcoming trip to Thailand. As such, as part of his strict regime he weighs himself every morning.</p>

<p>A few intervals of time are good, with a constant decrease of weight, and a few are bad, with a constant increase of weight. But some intervals are just weird.</p>

<p>We say that the measurements from an interval are <strong>weird</strong> if they alternate between increasing and decreasing. For instance, if the measurements for consecutive days are [1,3,2,5,1], these measurements are weird. If the measurements are [1,3,5,4], then they are not weird, since the value increases between 1 and 3 and between 3 and 5. Note that all intervals of size 1 are weird by this definition.</p>

<p>Given a sequence of integers, we are interested in figuring out how many intervals are weird. See the sample below for a better explanation.</p>

### 입력 

 <p>The first line of input will contain a single integer N, the size of the sequence.</p>

<p>The next line contains N numbers: a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>N</sub> representing the sequence of measurements.</p>

<ul>
	<li>1 ≤ N ≤ 200000</li>
	<li>0 ≤ a<sub>i</sub> ≤ 10<sup>9</sup></li>
</ul>

### 출력 

 <p>Output a single integer indicating the number of non-empty periods with weird measurements the sequence from the input has.</p>

