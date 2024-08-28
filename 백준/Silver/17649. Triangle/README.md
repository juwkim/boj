# [Silver III] Triangle - 17649 

[문제 링크](https://www.acmicpc.net/problem/17649) 

### 성능 요약

메모리: 113948 KB, 시간: 1960 ms

### 분류

사칙연산, 브루트포스 알고리즘, 기하학, 구현, 수학

### 제출 일자

2024년 8월 28일 10:04:05

### 문제 설명

<p>In the plane are given N distinct points with coordinates that are decimal fractions. Write program that handles Q queries. Each query is given with two fractional numbers x and y. For each query, the program has to calculate the number of epsilon-isosceles triangles such that each of them has a vertex with coordinates - the point (x, y) and the other two vertices are two different points among the given N points.</p>

<p>We say that a triangle is epsilon-isosceles when the absolute value of the difference between the lengths of two of its sides is less than 0.0001 and for that triangle we do not require for a pair of its vertices to be necessarily non-coincident points and we do not require its three vertices to be necessarily non-collinear.</p>

### 입력 

 <p>The first line of the input contains the integers N and Q. Each of the next N lines of the input contains two decimal fractions - coordinates of the next given point. There are following Q lines, each containing two decimal fractions - the coordinates of a point in the next query.</p>

### 출력 

 <p>The program should output Q lines, each containing a single integer, equal to the answer to each of the queries printed in the order of the input.</p>

