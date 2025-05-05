# [Silver I] Patkice - 20195 

[문제 링크](https://www.acmicpc.net/problem/20195) 

### 성능 요약

메모리: 109544 KB, 시간: 88 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 5월 5일 22:49:44

### 문제 설명

<p>Not so long ago, in a distant tropical land, there lived three rubber ducks. One hot summer day while they were lying on the beach, the ducks decided to travel to a nearby island. Since the ducks like adventures, they decided to travel carried by ocean currents in an old black umbrella.</p>

<p>Since the ducks are experienced ocean explorers, before the voyage they will check out a map of ocean currents. On the map, the island where the ducks live is marked by a letter 'o'. The ducks can start their voyage in any of the four directions: north – N, east – E, west – W and south – S.</p>

<p>Ocean currents in these seas move in one of the four directions, and are marked on the map in the following way: west-east '<', east-west '>', north-south 'v' and south-north '^'. When the ducks are located on a cell with a current, they will move one cell in the direction of the current. Ocean currents in these seas are special, as they never lead outside of the map and they don’t form vortexes (places where the ducks would move in circles if they followed the current).</p>

<p>Calm sea is marked by a dot '.'. If the currents bring the ducks to a cell with calm sea or back to the starting island, they won’t be able to continue the voyage. The island that the ducks want to visit is marked by a letter 'x'.</p>

<p>The ducks don’t want to stop their beach party. They kindly ask you to tell them if it’s possible for them to get to the other island, and if it is, in which direction should they start their voyage. Since one of the ducks gets very seasick, they ask you to choose the direction that will make the voyage as short as possible. If there are multiple directions that yield the same minimal travel time, you should choose the one that is alphabetically first.</p>

### 입력 

 <p>The first line contains integers r and s (3 ≤ r, s ≤ 100), the number of rows and columns of the map.</p>

<p>Each of the next r lines contains s characters from the set 'o<>v^.x', that represent the map of ocean currents. There will always be exactly one character 'o' and exactly one character 'x' on the map. The character 'o' will never be located in the first or last row nor column.</p>

### 출력 

 <p>If the ducks can’t reach the other island, print :(.</p>

<p>Otherwise, print :) in the first line. In the second line, print the start direction (N for north, E for east, W for west or S for south).</p>

