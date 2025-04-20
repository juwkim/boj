# [Silver I] Dominos 2 - 4191 

[문제 링크](https://www.acmicpc.net/problem/4191) 

### 성능 요약

메모리: 112676 KB, 시간: 148 ms

### 분류

깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 20일 20:11:55

### 문제 설명

<p>Dominos are lots of fun. Children like to stand the tiles on their side in long lines. When one domino falls, it knocks down the next one, which knocks down the one after that, all the way down the line. However, sometimes a domino fails to knock the next one down. In that case, we have to knock it down by hand to get the dominos falling again.</p>

<p>Given a set of dominos that are knocked down by hand, your task is to determine the total number of dominos that fall.</p>

### 입력 

 <p>The first line of input contains one integer specifying the number of test cases to follow. Each test case begins with a line containing three integers n, m, l no larger than 10 000, followed by m+l additional lines. The first integer n is the number of domino tiles. The domino tiles are numbered from 1 to n. Each of the m lines after the first line contains two integers x and y indicating that if domino number x falls, it will cause domino number y to fall as well. Each of the following l lines contains a single integer z indicating that the domino numbered z is knocked over by hand.</p>

### 출력 

 <p>For each test case, output a line containing one integer, the total number of dominos that fall over.</p>

