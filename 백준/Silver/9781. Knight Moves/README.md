# [Silver I] Knight Moves - 9781 

[문제 링크](https://www.acmicpc.net/problem/9781) 

### 성능 요약

메모리: 114200 KB, 시간: 128 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 21일 18:26:57

### 문제 설명

<p>In Chess, a knight can move two squares in one direction and then one in a perpendicular direction. It can ‘jump’, meaning that it only requires that the destination square be open - the path between can be occupied. In this diagram, the knight could move to any of the Xs.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/10562/1.png" style="width: 145px; height: 150px;"></p>

<p>Given a grid, a starting point and destination point, determine the least number of moves the knight must make to get from the start to the destination. Some squares of the grid may be occupied, so that the knight cannot move there.</p>

### 입력 

 <p>Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. Each test case will begin with two integers n and m (2≤n,m≤100), indicating the height and width of the grid. Each of the next n lines will hold m characters, representing the grid. The grid will consist only of ‘.’ (open square), ‘#’ (occupied square), ‘K’ (the knight’s starting position) or ‘X’ (the knight’s destination). There will be exactly one ‘K’ and exactly one ‘X’ in each test case.</p>

### 출력 

 <p>Output a single line with a single integer indicating the minimum number of moves the knight needs to get to the destination, or -1 if the knight cannot make it. Output no spaces.</p>

