# [Silver III] The Geneva Confection - 10106 

[문제 링크](https://www.acmicpc.net/problem/10106) 

### 성능 요약

메모리: 123716 KB, 시간: 244 ms

### 분류

자료 구조, 스택

### 제출 일자

2024년 4월 30일 04:41:28

### 문제 설명

<p>In order to ensure peace and prosperity for future generations, the United Nations is creating the world’s largest candy. The ingredients must be taken in railway cars from the top of a mountain and poured into Lake Geneva. The railway system goes steeply from the mountaintop down to the lake, with a T-shaped branch in the middle as shown below.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/7e6d682e-c91f-4d11-9d8a-3778a5d45388/-/preview/" style="width: 304px; height: 241px;"></p>

<p>Right now, each of the N ingredients is in its own railway car. Each railway car is assigned a positive integer from 1 to N. The ingredients must be poured into the lake in the order 1, 2, 3, . . . , N but the railway cars are lined up in some random order. The difficulty is that, because of the especially heavy gravity today, you can only move cars downhill to the lake, or sideways on the branch line. Is it still possible to pour the ingredients into the lake in the order 1, 2, 3, . . . , N ?</p>

<p>For example, if the cars were in the order 2, 3, 1, 4, we can slide these into the lake in order as described below:</p>

<p><img alt="" src="https://upload.acmicpc.net/d03864f5-f3dc-4e45-a1e4-f9d352d84534/-/preview/" style="width: 303px; height: 236px;" class="left-float"></p>

<ul>
	<li>Slide car 4 out to the branch</li>
	<li>Slide car 1 into the lake</li>
	<li>Slide car 3 out to the branch</li>
	<li>Slide car 2 into the lake</li>
	<li>Slide car 3 from the branch into the lake</li>
	<li>Slide car 4 from the branch into the lake</li>
</ul>

### 입력 

 <p>The first line will contain the number T (1 ≤ T ≤ 10) which is the number of different tests that will be run. Each test has the form of an integer N (1 ≤ N ≤ 100 000) on the first line of the test, followed by a list of the N cars listed from top to bottom. The cars will always use the numbers from 1 to N in some order.</p>

### 출력 

 <p>For each test, output one line which will contain either Y (for “yum”) if the recipe can be completed, and N otherwise.</p>

