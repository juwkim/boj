# [Silver V] VLAK - 8978 

[문제 링크](https://www.acmicpc.net/problem/8978) 

### 성능 요약

메모리: 113248 KB, 시간: 112 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p>An empty train on a train station is waiting for passengers to board. The train consists of N cars and each car can accommodate K passengers. </p>

<p>The train station is swamped with strange demands. Passengers board the train one by one and go to one of the cars in which there are free seats left. Each passenger chooses a car to board according to the following rules: </p>

<ol>
	<li>Of all the cars which are not full, the passenger chooses the one which has the fewest passengers whose names start with the same letter as his. </li>
	<li>If there are multiple cars which have the same fewest number of such passengers, the passenger chooses the one with the smallest total number of passengers. </li>
	<li>If there are still multiple cars, the passenger boards the first of these. </li>
</ol>

<p>Write a program that, given the list of passengers which are boarding the train, determines the number of passengers in each car after boarding has completed. </p>

### 입력 

 <p>The first line contains two integers N and K, 1 ≤ N ≤ 10, 1 ≤ K ≤ 10, the number of cars and the number of passengers each car can accomodate. </p>

<p>The second line contains an integer P, 1 ≤ P ≤ N·K, the number of passengers waiting to board. </p>

<p>The next P lines contain the names of all passengers, in order in which they will board. The name of each passenger is a string of at most 10 lowercase letters of the English alphabet. No two passengers will have the same name. </p>

### 출력 

 <p>Output N integers separated by single spaces on a single line, the number of passengers in each car, in order from first car to last. </p>

