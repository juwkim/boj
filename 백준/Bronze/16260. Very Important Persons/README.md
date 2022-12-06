# [Bronze I] Very Important Persons - 16260 

[문제 링크](https://www.acmicpc.net/problem/16260) 

### 성능 요약

메모리: 30840 KB, 시간: 144 ms

### 분류

구성적(constructive), 구현(implementation)

### 문제 설명

<p>Opening ceremony of the new campus of N State University will be visited by nm very important persons. The ceremony will take place in a hall that has the form of a rectangle, seats in the hall are arranged in n rows, m seats in each row. Rows are numbered from 1 to n, seats in each row are numbered from 1 to m, the j-th seat of the i-th row is denoted as (i, j).</p>

<p>The organizers of the ceremony have numbered the guests from 1 to nm in accordance with their importance — the greater, the more important. The most important guest, the mayor of the city, gets the number nm. The mayor is planning to take seat (1, 1). Now the other guests must be assigned seats. The guests must be arranged according to their importance, there must be no situation that a guest with greater number is seating further from the mayor than a guest with smaller number. The distance between two seats (r<sub>1</sub>, s<sub>1</sub>) and (r<sub>2</sub>, s<sub>2</sub>) is measured as |r<sub>1</sub> - r<sub>2</sub>| + |s<sub>1</sub> - s<sub>2</sub>|.</p>

<p>Help the organizers to assign guests to seats.</p>

### 입력 

 <p>Input contains several test cases. The first line contains the number of test cases t (1 ≤ t ≤ 400).</p>

<p>Each test case is specified with a line that contains two integers: n and m (1 ≤ n, m ≤ 20).</p>

### 출력 

 <p>For each test case output the hall plan after the seats are assigned to guests.</p>

<p>Output n lines, each line must contain m integers, the j-th integer of the i-th line must be equal to the importance of the guest that will be assigned the seat (i, j).</p>

<p>If there are several valid ways to assign seats to guests, output any of them.</p>

