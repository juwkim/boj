# [Silver I] Preventing Paradoxes - 5130 

[문제 링크](https://www.acmicpc.net/problem/5130) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

기하학

### 제출 일자

2025년 5월 25일 02:24:47

### 문제 설명

<p>Time traveling runs the risk of causing all sorts of problems and paradoxes, like duplicate people, parallel universes, and black holes, to name a few. Tim is well aware of what’s at stake, but he continues to time travel because he knows the secret: you have to properly close your tears in the space-time continuum! This can be done by simply visiting each space-time destination in a right-handed orientation. Easy!</p>

<p>Specifically, Tim has a list of points in the space-time plane which represent his trip, and he has to start and end at the same point. But there are two possible ways of traversing the list: forwards and backwards. One way leads to prosperity, and the other to paradoxes and total ruin. Tim has been verifying his trips by hand, but realizing how dangerous this is, Tim has decided he wants a program that can verify his trips for him.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line of each data set contains the number 3 ≤ N ≤ 100 of space-time points in Tim’s trip. The next N lines each contain two integers s and t, a space-time coordinate, where s is plotted on the x-axis, t on the y-axis, and −100 ≤ s, t ≤ 100. Taken in order, the N points will always form a closed, non-overlapping polygon, where no three consecutive space-time points are collinear.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. On the next line, output “RIGHT” if, when looking down on the space-time plane, Tim would have his right hand touching the interior of the polygon as he traverses its points in the input order. Otherwise, output “LEFT”. Each data set should be followed by a blank line.</p>

