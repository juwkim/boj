# [Silver I] Crank - 9365 

[문제 링크](https://www.acmicpc.net/problem/9365) 

### 성능 요약

메모리: 113496 KB, 시간: 116 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 5월 3일 19:54:44

### 문제 설명

<p>Chev Chelios had his heart stolen from him, by the boss of the most dangerous gang in the city. His heart has been replaced with an artificial chargeable one! </p>

<p>Chelios was on mission of locating the boss of the gang to get his heart back since then without luck! Now the artificial heart’s battery lifetime is about to expire! Fortunately, he finally located the target but he needs your help to get there before his artificial heart stops beating! </p>

<p>Chelios decided to attack the boss building from the roof because all gates are heavily protected by gangsters. Chelios has the map of the gang block which shows the heights of all buildings within the block. The plan is that a helicopter will drop Chelios on the roof of one of the buildings on the boundary of the block during night. Then Chelios will get to the boss building by moving to adjacent buildings, vertically or horizontally. Chelios can only move to a building which has the same or smaller height as the current building (going up severely affects his damaged heart). </p>

<p>Given the gang building block map which shows the heights of all buildings in the block along with the boss building, write a program to help Chev Chelios determine the number of buildings on the boundary of the block he can be dropped by the helicopter at so that he would be able to reach the boss’s building without climbing! </p>

### 입력 

 <p>The first line of input contains an integer T, the number of test cases. T test cases follow, the first line of each test case contains two integers (1 <= R,C <= 10) the height and width of the building block. The second line contains two integers (1 <= A <= R), and (1 <= B <= C), the coordinates of the boss building on the map. R lines follows; each line consists of C space separated integers representing the heights of all buildings. A height H of a building satisfies (1 <= H <= 1000). </p>

### 출력 

 <p>For each test case, print the number of buildings on the boundary of the block Chev Chelios can be dropped by the helicopter at so that he would be able to reach the boss’s building without climbing up! Follow the output format below. </p>

