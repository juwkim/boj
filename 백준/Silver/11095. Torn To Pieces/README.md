# [Silver I] Torn To Pieces - 11095 

[문제 링크](https://www.acmicpc.net/problem/11095) 

### 성능 요약

메모리: 110068 KB, 시간: 108 ms

### 분류

너비 우선 탐색, 자료 구조, 깊이 우선 탐색, 그래프 이론, 그래프 탐색, 해시를 사용한 집합과 맵

### 제출 일자

2025년 4월 21일 15:41:08

### 문제 설명

<p>You have arrived in The Big City but your journey is not yet complete. You must still navigate the subway and get to your final destination. The information booth in the subway station is unattended and fresh out of maps of the subway system. On the floor you notice fragments of a map. Can you piece together enough of the map to figure out how to get to your final destination?</p>

<p>Each fragment of the map happens to perfectly contain a single subway station while also identifying all of the other stations that it connects to. Each connection between stations is bi-directional such that it can be travelled going either direction. Using all of the available fragments, your task is to determine the sequence of stations you must pass through in order to reach your final destination or state that there is no route if you don’t have enough information to complete your journey.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11095/1.png" style="height:140px; width:555px"></p>

### 입력 

 <p>The first line of input has an integer, 2 ≤ N ≤ 32, that identifies the number of pieces of the map that were found.</p>

<p>The following N lines each describe a station depicted on one of those pieces. Each of these lines starts with the name of the station they describe and is followed by a space-separated list of all of the station names that are directly connected to that station (there may be as many as N − 1).</p>

<p>The final line identifies a starting station and a destination station. The destination station is guaranteed to be different than the starting station.</p>

<p>Each station name is a string of up to 20 characters using only letters a–z and A–Z. It is guaranteed that there is at most one simple route (without revisiting stations) from the starting station to the destination station</p>

### 출력 

 <p>Give the sequence of stations that leads from the starting station to the destination station. Separate station names with spaces. If there are not enough pieces of the map to find a route from the starting station to the destination station then output “no route found”.</p>

