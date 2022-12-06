# [Silver V] Jarvis - 17048 

[문제 링크](https://www.acmicpc.net/problem/17048) 

### 성능 요약

메모리: 140688 KB, 시간: 212 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 정렬(sorting), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>Ivan sent N drone warriors to the final battle against Tony Stark, also known as Iron Man. Each drone has a defined frequency, expressed as an integer number, on which it receives commands from Ivan during the fight. Jarvis, the artificial intelligence developed by Toni, has to determine which frequencies those are and thereby take control over as many drones as possible.</p>

<p>Jarvis knows the original factory values of the frequency for each drone, but the frequencies required for each drone, unfortunately, have been changed in the meantime.</p>

<p>Jarvis has only one attempt. He can choose an integer number X and increase each of the factory frequencies by X (X may be negative as well). After that, Jarvis will take over control of each drone whose modified factory frequencies and the one required by the specific drone is equal.</p>

<p>Write a program that will determine how much drone warriors Jarvis can take control over.</p>

### 입력 

 <p>The first line contains the integer number N (1 ≤ N ≤ 100 000), the number of drones from the task statement.</p>

<p>In the second line there are N integers A<sub>i</sub> (-1 000 000 ≤ A<sub>i</sub> ≤ 1 000 000) representing the factory frequency values of the drone warrior.</p>

<p>In the third line there are N integers B<sub>i</sub> (-1 000 000 ≤ B<sub>i</sub> ≤ 1 000 000) representing the required frequency values of the drone warriors.</p>

### 출력 

 <p>In the only line, print out the largest number of drone warriors Jarvis can take control over.</p>

