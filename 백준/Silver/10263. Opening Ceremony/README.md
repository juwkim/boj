# [Silver II] Opening Ceremony - 10263 

[문제 링크](https://www.acmicpc.net/problem/10263) 

### 성능 요약

메모리: 121212 KB, 시간: 116 ms

### 분류

이분 탐색, 그리디 알고리즘, 정렬

### 제출 일자

2024년 12월 7일 00:59:04

### 문제 설명

<p><img alt="" src="https://www.acmicpc.net/upload/images2/opening.png" style="float:right; height:210px; width:249px">For the grand opening of the algorithmic games in NlogNsglow, a row of tower blocks is set to be demolished in a grand demonstration of renewal. Originally the plan was to accomplish this with controlled explosions, one for each tower block, but time constraints now require a hastier solution.</p>

<p>To help you remove the blocks more rapidly you have been given the use of a Universal Kinetic / Incandescent Energy Particle Cannon (UKIEPC). On a single charge, this cutting-edge contraption can remove either all of the floors in a single tower block, or all the x-th floors in all the blocks simultaneously, for user’s choice of the floor number x. In the latter case, the blocks that are less than x floors high are left untouched, while for blocks having more than x floors, all the floors above the removed x-th one fall down by one level.</p>

<p>Given the number of floors of all towers, output the minimum number of charges needed to eliminate all floors of all blocks.</p>

### 입력 

 <p>The first line of input contains the number of blocks n, where 2 ≤ n ≤ 100 000. The second line contains n consecutive block heights h<sub>i</sub> for i = 1, 2, ... , n, where 1 ≤ h<sub>i</sub> ≤ 1 000 000.</p>

### 출력 

 <p>Output one line containing one integer: the minimum number of charges needed to tear down all the blocks.</p>

