# [Silver V] Bus Logic - 17566 

[문제 링크](https://www.acmicpc.net/problem/17566) 

### 성능 요약

메모리: 113112 KB, 시간: 128 ms

### 분류

비트마스킹(bitmask), 브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>A core part of the decision of where to live in a city like Nottingham is the availability of transport links to interesting places. This is particularly intersting to Max, who enlivens his stressful life as organiser of UKIEPC by making frequent sightseeing travels around town in a bright orange bus.</p>

<p>Max’s idea of a good time is a visit to a spot that takes exactly one bus journey to get to. He is considering moving house to be near to one specific spot along his favourite bus route—how many such other scenic spots can he reach from there (assuming that on a given trip he can choose a new bus route each time)?</p>

<p style="text-align: center;"><img alt="" src="" style="width: 193px; height: 200px;"></p>

<p style="text-align: center;">Figure B.1: A bus route map illustrating Sample Input 1. Max, as usual, is drawn as a white dot in the centre of each bus stop he can start from.</p>

### 입력 

 <ul>
	<li>The first line of input contains three integers: Max’s starting stop, m (1 ≤ m ≤ s). the number of buses, b (1 ≤ b ≤ 50), and the number of stops, s (1 ≤ s ≤ 50).</li>
	<li>The next b lines contain the bus routes, each written as a string of s characters where having the ith character as ’1’ denotes that this bus route has a stop at i, and ’0’ denotes that it does not.</li>
</ul>

### 출력 

 <p>Output the maximum number of other stops Max can reach from the starting stop by taking exactly one bus.</p>

