# [Silver IV] Frosh Week - 15282 

[문제 링크](https://www.acmicpc.net/problem/15282) 

### 성능 요약

메모리: 155832 KB, 시간: 220 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting)

### 문제 설명

<p>Professor Zac is trying to finish a collection of tasks during the first week at the start of the term. He knows precisely how long each task will take, down to the millisecond. Unfortunately, it is also Frosh Week. Zac’s office window has a clear view of the stage where loud music is played. He cannot focus on any task when music is blaring.</p>

<p>The event organizers are also very precise. They supply Zac with intervals of time when music will not be playing. These intervals are specified by their start and end times down to the millisecond.</p>

<p>Each task that Zac completes must be completed in one quiet interval. He cannot pause working on a task when music plays (he loses his train of thought). Interstingly, the lengths of the tasks and quiet intervals are such that it is impossible to finish more than one task per quiet interval!</p>

<p>Given a list of times t<sub>i</sub> (in milliseconds) that each task will take and a list of times ℓ<sub>j</sub> (in milliseconds) specifying the lengths of the intervals when no music is being played, what is the maximum number of tasks that Zac can complete?</p>

### 입력 

 <p>The first line of input contains a pair of integers n and m, where n is the number of tasks and m is the number of time intervals when no music is played. The second line consists of a list of integers t<sub>1</sub>, t<sub>2</sub>, . . . , t<sub>n</sub> indicating the length of time of each task. The final line consists of a list of times ℓ<sub>1</sub>, ℓ<sub>2</sub>, . . . , ℓ<sub>m</sub> indicating the length of time of each quiet interval when Zac is at work this week.</p>

<p>You may assume that 1 ≤ n, m ≤ 200, 000 and 100, 000 ≤ t<sub>i</sub>, ℓ<sub>j</sub> ≤ 199, 999 for each task i and each quiet interval j.</p>

### 출력 

 <p>Output consists of a single line containing a single integer indicating the number of tasks that Zac can accomplish from his list during this first week.</p>

