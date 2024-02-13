# [Silver III] Sort a scrambled itinerary (Small) - 12186 

[문제 링크](https://www.acmicpc.net/problem/12186) 

### 성능 요약

메모리: 113164 KB, 시간: 144 ms

### 분류

브루트포스 알고리즘, 자료 구조, 그래프 이론, 그래프 탐색, 해시를 사용한 집합과 맵, 문자열, 트리를 사용한 집합과 맵

### 제출 일자

2024년 2월 14일 02:24:50

### 문제 설명

<p>Once upon a day, Mary bought a one-way ticket from somewhere to somewhere with some flight transfers.</p>

<p>For example: SFO->DFW DFW->JFK JFK->MIA MIA->ORD.</p>

<p>Obviously, transfer flights at a city twice or more doesn't make any sense. So Mary will not do that.</p>

<p>Unfortunately, after she received the tickets, she messed up the tickets and she forgot the order of the ticket.</p>

<p>Help Mary rearrange the tickets to make the tickets in correct order.</p>

### 입력 

 <p>The first line contains the number of test cases <b>T</b>, after which <b>T</b> cases follow.</p>

<p>For each case, it starts with an integer <b>N</b>. There are <b>N</b> flight tickets follow.</p>

<p>Each of the next 2 lines contains the source and destination of a flight ticket.</p>

### 출력 

 <p>For each test case, output one line containing "Case #x: itinerary", where <b>x</b> is the test case number (starting from 1) and <b>itinerary</b> is sorted list of flight tickets which represents the actual itinerary. Each flight segment in the itinerary should be outputted as pair of source-destination airport codes.</p>

