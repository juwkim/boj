# [Silver I] Refueling Stops - 10515 

[문제 링크](https://www.acmicpc.net/problem/10515) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

그리디 알고리즘, 구현, 시뮬레이션

### 제출 일자

2025년 5월 10일 19:55:12

### 문제 설명

<p>John is taking a long drive from Rawalpindi to Karachi along the Indus Highway. His car’s full fuel tank holds enough petrol to travel k kilometers. You have a map that gives distances between fuel stations along the route. Let d<sub>1</sub> < d<sub>2</sub> < … < d<sub>n</sub> be the locations of all the gas stations along the route where d<sub>i</sub> is the distance from Rawalpindi to the fuel station i.</p>

<p>Your goal is to help John decide which petrol stations he should stop at for refueling along the path so that he has to take minimum stops. Assume that he starts with a full tank.</p>

### 입력 

 <p>The input consists of multiple test cases. The first line of input is the number of test cases N(1≤N≤100). Each of the following N lines contain the total distance D from Rawalpindi to Karachi in kilometers (1≤D≤10000), the number of kilometers K that his car can travel with a full tank (1≤K≤10000), the total number of filling stations S along the route (1≤S≤100), followed by S integers representing (distance from Rawalpindi in kilometers) the positions of the filling stations.</p>

### 출력 

 <p>For each test case, print a single line that saying “Case #n:” where n is the test case number followed by a space followed by space separated list of petrol pump locations where John should stop for refueling for that test case. If John is going to run out of petrol, say “out of petrol” for that case.</p>

