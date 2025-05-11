# [Silver I] Border Restrictions - 21837 

[문제 링크](https://www.acmicpc.net/problem/21837) 

### 성능 요약

메모리: 110068 KB, 시간: 112 ms

### 분류

너비 우선 탐색, 자료 구조, 그래프 이론, 그래프 탐색, 해시를 사용한 집합과 맵, 파싱, 문자열, 집합과 맵

### 제출 일자

2025년 5월 11일 21:10:38

### 문제 설명

<p>To prevent the spread of the virus, many countries have closed their borders to travellers arriving from certain other countries. Over time, different people travel to different countries and it is still possible for the virus to spread from country to country. If the virus starts in one country, how long will it be before it has spread to other countries? We will assume that if the virus is in one country in week i and a second country allows travellers from the first country, the virus will reach the second country in week i+ 1. Once the virus reaches a country, it is there forever, until a vaccine is found.</p>

### 입력 

 <p>The first line of input contains N, the number of countries in the world, with 1 ≤ N ≤ 300. N lines of input follow, each describing a country. Each line has the form <code>DESTINATION allows travellers from ORIGIN1 ORIGIN2 ORIGIN3</code>, where <code>DESTINATION</code>, <code>ORIGIN1</code>, <code>ORIGIN2</code>, <code>ORIGIN3</code> are names of countries consisting of at most 30 uppercase letters from <code>A</code> to <code>Z</code>. Every country has a unique name. Note that there may be as few as 0 and as many as N-1 origin countries on a line, not always three. Also, the origin countries on each line are distinct and do not include the destination country. In week one, the virus is only in the first country listed in the input.</p>

### 출력 

 <p>Output N lines, one for each country, sorted in alphabetical order. On each line, output the country name followed by the number of the week in which the virus reaches that country. If the virus can never reach some country, output 0 instead of the number of the week in which the virus reaches that country.</p>

