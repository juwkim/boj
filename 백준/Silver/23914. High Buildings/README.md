# [Silver IV] High Buildings - 23914 

[문제 링크](https://www.acmicpc.net/problem/23914) 

### 성능 요약

메모리: 110404 KB, 시간: 116 ms

### 분류

많은 조건 분기

### 제출 일자

2023년 12월 22일 21:03:36

### 문제 설명

<p>In an unspecified country, Google has an office campus consisting of <b>N</b> office buildings in a line, numbered from 1 to <b>N</b> from left to right. When represented in meters, the height of each building is an integer between 1 to <b>N</b>, inclusive.</p>

<p>Andre and Sule are two Google employees working in this campus. On their lunch break, they wanted to see the skyline of the campus they are working in. Therefore, Andre went to the leftmost point of the campus (to the left of building 1), looking towards the rightmost point of the campus (to the right of building <b>N</b>). Similarly, Sule went to the rightmost point of the campus, looking towards the leftmost point of the campus.</p>

<p>To Andre, a building x is visible if and only if there is no building to the left of building x that is strictly higher than building x. Similarly, to Sule, a building x is visible if and only if there is no building to the right of building x that is strictly higher than building x.</p>

<p>Andre learned that there are <b>A</b> buildings that are visible to him, while Sule learned that there are <b>B</b> buildings that are visible to him. After they regrouped and exchanged information, they also learned that there are <b>C</b> buildings that are visible to both of them.</p>

<p>They are wondering about the height of each building. They are giving you the value of <b>N</b>, <b>A</b>, <b>B</b>, and <b>C</b> for your information. As their friend, you would like to construct a possible height for each building such that the information learned on the previous paragraph is correct, or indicate that there is no possible height construction that matches the information learned (thus at least one of them must have been mistaken).</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow. Each consists of a single line with four integers <b>N</b>, <b>A</b>, <b>B</b>, and <b>C</b>: the information given by Andre and Sule.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is <code>IMPOSSIBLE</code> if there is no possible height for each building according to the above information, or <b>N</b> space-separated integers otherwise. The i-th integer in <code>y</code> must be the height of the i-th building (in meters) between 1 to <b>N</b>.</p>

