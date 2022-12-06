# [Bronze II] Zombie Invasion - 9433 

[문제 링크](https://www.acmicpc.net/problem/9433) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>A group of survivors has arrived by helicopter to an isolated island. The island is made up of a long narrow strip of villages. The infected survivors arrived in the village to the far east and accidentally infected the native population. The islanders are now attempting to escape the zombies that have appeared on the east coast.</p>

<p>You are given N cases with 20 non-negative integers that represent the number of islanders at a given village. The villages are represented from west to east (left to right, respectively), with the zombies moving in from the east. The islanders have peculiar customs for traveling and will only move between villages in pairs. Curiously, for every pair that travels between two villages, only one of them ever survives the trip. As the zombies move west, islanders will travel to the village immediately west of their current village as long as there are at least two islanders there. If there are an odd number people in a village then one stays in the village and the rest move to the next village in pairs. Once the islanders reach the village on the west coast, they will stop traveling.</p>

<p>Determine how many islanders remain at each village and the number that make it safely to the village on the west coast (far left).</p>

### 입력 

 <p>The first line of data represents the number of data sets you will read in, N (1 <= N <= 50).</p>

<p>There will then be N lines of twenty 20 non-negative integers each. Each integer (<= 1000) represents the number of islanders who reside in a village. The leftmost integer represents the village on the west coast, and the rightmost integer represents the village on the east coast.</p>

### 출력 

 <p>Your output will be N lines of twenty 20 non-negative integers. The left most number will represent the number of islanders that reached the west. Each number to the right will represent the number of people that stayed behind in each village.</p>

