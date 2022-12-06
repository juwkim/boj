# [Bronze I] Rect - 9891 

[문제 링크](https://www.acmicpc.net/problem/9891) 

### 성능 요약

메모리: 30840 KB, 시간: 632 ms

### 분류

많은 조건 분기(case_work), 기하학(geometry), 구현(implementation)

### 문제 설명

<p>A rectangle is <em>axis-parallel</em> if its top and bottom sides are parallel to the x-axis and its left and right sides are parallel to the y-axis. From now on by a rectangle we mean an axis-parallel rectangle.</p>

<p>A rectangle will be specified by a 4-tuple (x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, y<sub>2</sub>) in which (x<sub>1</sub>, y<sub>1</sub>) is the bottom-left corner and (x<sub>2</sub>, y<sub>2</sub>) is the top-right corner of the rectangle. We will also say the rectangle (x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, y<sub>2</sub>) is a (x<sub>2</sub> − x<sub>1</sub>) × (y<sub>2</sub> − y<sub>1</sub>) rectangle.</p>

<p>Two rectangles are <em>incomparable</em> if neither will fit inside the other possibly with translation and 90<sup>◦</sup> rotation; otherwise, the two rectangles are comparable. Given a list of rectangles, you are to output the number of pairs of incomparable rectangles.</p>

### 입력 

 <p>The first input line contains an integer which is the number of rectangles n (where 0 ≤ n ≤ 10000). Each of the next n lines describes a rectangle and contains four integers x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, y<sub>2</sub>, a space separates two adjacent integers. Recall that coordinates (x<sub>1</sub>, y<sub>1</sub>), (x<sub>2</sub>, y<sub>2</sub>) specify respectively the bottom-left and top-right corner of the rectangle. All coordinate values are in the range of 0 to 10,000; that is, 0 ≤ x<sub>1</sub> ≤ 10000, 0 ≤ y<sub>1</sub> ≤ 10000, 0 ≤ x<sub>2</sub> ≤ 10000, 0 ≤ y<sub>2</sub> ≤ 10000.</p>

### 출력 

 <p>The output file contains a single integer which is the number of pairs of incomparable rectangles.</p>

