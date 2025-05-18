# [Silver I] Best Place - 19704 

[문제 링크](https://www.acmicpc.net/problem/19704) 

### 성능 요약

메모리: 130368 KB, 시간: 184 ms

### 분류

정렬

### 제출 일자

2025년 5월 18일 15:52:11

### 문제 설명

<p>IOI 2020 will be held in Singapore, hosted by School of Computing of the National University of Singapore (NUS), supported by Singapore Ministry of Education (MOE) and Singapore Exhibition & Convention Bureau (SECB).</p>

<p>One of the challenges of hosting such a large event is to find a suitable location for the event. A common suggestion would be to select a location that reduces the travelling distance for the participants. You are thus tasked to write a program to find one such location.</p>

<p>Suppose there are N participants for IOI 2020. Assume the i th participant’s house is located on (Xi , Yi) on the cartesian plane. You aim to find a location to hold IOI 2020 such that the total sum of travelling distance is minimized. Assume IOI 2020 is chosen to be at (X, Y), the travelling distance for the i th participant is the Manhattan distance between (X, Y) and (X<sub>i</sub>, Y<sub>i</sub>), i.e., |X − X<sub>i</sub>| + |Y − Y<sub>i</sub>|.</p>

<p>If there are multiple locations where the total sum of travelling distance is minimized, you are to output any one of these coordinates. It is possible for the location of the event be the same as the location of a participant’s house. However, the event must be held at a position (X, Y) where X and Y are integers. It is also possible that more than 1 participant lives at the same coordinates. In that case, you are to sum their travelling distance separately. (Assume they will travel separately.)</p>

### 입력 

 <p>The input will start with a single integer, N, in a single line. N denotes the total number of participants.</p>

<p>N lines will then follow with 2 integers each, the i<sup>th</sup> line will contain X<sub>i</sub> and Y<sub>i</sub>. This indicates that the coordinate of the i<sup>th</sup> participant’s house is at (X<sub>i</sub>, Y<sub>i</sub>).</p>

### 출력 

 <p>Output 2 integers (X, Y) on the same line, space separated. (X, Y) will denote the coordinates of the event where by the total sum of travelling distance would be minimized.</p>

