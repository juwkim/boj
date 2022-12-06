# [Bronze I] Darts - 3412 

[문제 링크](https://www.acmicpc.net/problem/3412) 

### 성능 요약

메모리: 117228 KB, 시간: 1688 ms

### 분류

기하학(geometry), 구현(implementation), 피타고라스 정리(pythagoras)

### 문제 설명

<p>Consider a game in which darts are thrown at a board. The board is formed by 10 circles with radii 20, 40, 60, 80, 100, 120, 140, 160, 180, and 200 (measured in millimeters), centered at the origin. Each throw is evaluated depending on where the dart hits the board. The score is p points (p ∈ {1, 2, ... , 10}) if the smallest circle enclosing or passing through the hit point is the one with radius 20 · (11 − p). No points are awarded for a throw that misses the largest circle.</p>

<p>Your task is to compute the total score of a series of n throws.</p>

### 입력 

 <p>The first line of the input contains the number of test cases T. The descriptions of the test cases follow:</p>

<p>Each test case starts with a line containing the number of throws n (1 ≤ n ≤ 10<sup>6</sup>). Each of the next n lines contains two integers x and y (−200 ≤ x, y ≤ 200) separated by a space—the coordinates of the point hit by a throw.</p>

### 출력 

 <p>Print the answers to the test cases in the order in which they appear in the input. For each test case print a single line containing one integer—the sum of the scores of all n throws.</p>

