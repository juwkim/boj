# [Bronze I] Goat Rope - 16410 

[문제 링크](https://www.acmicpc.net/problem/16410) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

많은 조건 분기(case_work), 기하학(geometry)

### 문제 설명

<p>You have a fence post located at the point (x, y) in the plane, to which a goat is tethered by a rope. You also have a house, which you model as an axis-aligned rectangle with diagonally opposite corners at the points (x<sub>1</sub>, y<sub>1</sub>) and (x<sub>2</sub>, y<sub>2</sub>). You want to pick a length of rope that guarantees the goat cannot reach the house. Determine the minimum distance from the fence post to the house, so that you can make sure to use a shorter rope.</p>

### 입력 

 <p>The input consists of a single line containing six space-separated integers x, y, x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, and y<sub>2</sub>, each in the range [−999, 999].</p>

<p>It is guaranteed that x<sub>1</sub> < x<sub>2</sub> and y<sub>1</sub> < y<sub>2</sub>, and that (x, y) is strictly outside the axis-aligned rectangle with corners at (x<sub>1</sub>, y<sub>1</sub>) and (x<sub>2</sub>, y<sub>2</sub>).</p>

### 출력 

 <p>Print the minimum distance from the goat’s post to the house, with a relative or absolute error no more than 0.001.</p>

