# [Bronze II] On the Bus - 7582 

[문제 링크](https://www.acmicpc.net/problem/7582) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>A bus leaves the bus depot with 4 passengers aboard. At the first stop, 3 more passengers get on. At the next stop, 1 passenger gets off and 2 get on. How many passengers are now on the bus?</p>

<p>This problem presents you with a number of scenarios of this nature. All you have to do is state how many passengers are on board the bus at the end of the scenario.</p>

### 입력 

 <p>Each scenario begins with a route number (up to 5 numbers or letters with no spaces) and Z, the size of the bus (maximum number of passengers, 10 <= Z <= 100) separated by a space. Input is terminated by a line containing just # 0 – this line should not be processed. The 2nd line of the scenario gives P, the initial number of passengers on the bus (0 <= P <=Z). The 3rd line of the scenario gives S, the number of stops that are to be considered (1 <= S <= 100). There then follow S lines each containing 2 integers separated by spaces. The first number represents the number of passengers getting off at the stop, the second the number of passengers waiting to board. If the number of passengers waiting to get on is greater than the number of available seats, after the alighting passengers have got off, then the excess passengers are left behind. Health and Safety regulations prohibit the carrying of standing passengers. </p>

### 출력 

 <p>Output consists of 1 line of text per scenario. It should show the route number exactly as input, followed by a space, followed by the number of passengers aboard the bus at the end of the scenario. </p>

