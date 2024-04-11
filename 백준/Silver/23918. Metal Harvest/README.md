# [Silver III] Metal Harvest - 23918 

[문제 링크](https://www.acmicpc.net/problem/23918) 

### 성능 요약

메모리: 212876 KB, 시간: 2568 ms

### 분류

사칙연산, 그리디 알고리즘, 수학, 정렬

### 제출 일자

2024년 4월 11일 18:52:46

### 문제 설명

<p>You are in charge of deploying robots to harvest Kickium from a nearby asteroid. Robots are not designed to work as a team, so only one robot can harvest at any point of time. A single robot can be deployed for up to <b>K</b> units of time in a row before it returns for calibration, regardless of how much time it spends on harvesting during that period. Harvesting can only be done during specific time intervals. These time intervals do not overlap. Given <b>K</b> and the time intervals in which harvesting is allowed, what is the minimum number of robot deployments required to harvest at all possible times?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow.</p>

<p>The first line of each test case gives two space separated integers <b>N</b> and <b>K</b>: the number of time intervals in which harvesting is allowed, and the maximum duration a robot can be deployed for before returning for calibration.</p>

<p>The next <b>N</b> lines contain a pair of space separated integers <b>S<sub>i</sub></b> and <b>E<sub>i</sub></b>: the start time and the end time of the i-th interval respectively. Please note that intervals don't include the time unit starting at the moment <b>E<sub>i</sub></b>, so for example an interval with (<b>S<sub>i</sub></b> = 2; <b>E<sub>i</sub></b> = 5) has duration of 3 time units.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the number of times robot deployment is needed so that for each interval there is one robot harvesting at that time.</p>

