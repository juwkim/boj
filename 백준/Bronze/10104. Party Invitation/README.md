# [Bronze II] Party Invitation - 10104 

[문제 링크](https://www.acmicpc.net/problem/10104) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

자료 구조(data_structures), 구현(implementation), 연결 리스트(linked_list), 시뮬레이션(simulation)

### 문제 설명

<p>You are hosting a party and do not have room to invite all of your friends. You use the following unemotional mathematical method to determine which friends to invite.</p>

<p>Number your friends 1, 2, . . . , K and place them in a list in this order. Then perform m rounds. In each round, use a number to determine which friends to remove from the ordered list.</p>

<p>The rounds will use numbers r<sub>1</sub>, r<sub>2</sub>, . . . , r<sub>m</sub>. In round i remove all the remaining people in positions that are multiples of r<sub>i</sub> (that is, r<sub>i</sub>, 2r<sub>i</sub>, 3r<sub>i</sub>, . . .) The beginning of the list is position 1.</p>

<p>Output the numbers of the friends that remain after this removal process.</p>

### 입력 

 <p>The first line of input contains the integer K (1 ≤ K ≤ 100). The second line of input contains the integer m (1 ≤ m ≤ 10), which is the number of rounds of removal. The next m lines each contain one integer. The ith of these lines (1 ≤ i ≤ m) contains r<sub>i</sub> (2 ≤ r<sub>i</sub> ≤ 100) indicating that every person at a position which is multiple of r<sub>i</sub> should be removed.</p>

### 출력 

 <p>The output is the integers assigned to friends who were not removed. One integer is printed per line in increasing sorted order.</p>

