# [Silver I] Pond Cascade - 14978 

[문제 링크](https://www.acmicpc.net/problem/14978) 

### 성능 요약

메모리: 214520 KB, 시간: 3480 ms

### 분류

이분 탐색, 매개 변수 탐색

### 제출 일자

2025년 6월 30일 01:47:34

### 문제 설명

<p>The cascade of water slides has been installed in the park recently and it has to be tested. The cascade consists of some number of reservoirs, or “ponds” for short, which are linked into a single sequence connected by water slides. Visitors are expected to start the journey in the topmost pond, then to be washed into subsequent lower ponds, and finally end the journey in the last pond of the cascade, which is also the lowest pond of the cascade. The journey spans all ponds in the cascade.</p>

<p>To test the cascade, each pond has to be completely filled with water. Each pond is attached to a pipe with a valve which, when opened, pours water into the pond. The sizes and capacities of different ponds are different. Fortunately, at least the pipes and the valves are standardized. Therefore, the rate at which water is poured through the valve into a pond is the same for all ponds.</p>

<p>When a pond is filled, water overflows and continues to flow into the next pond. If that pond is also filled, water continues to the next subsequent pond, and so on, until it either reaches some pond which has not been completely filled yet, or it overflows the lowest pond and sinks in the drain at the bottom of the cascade. The time in which the overflowing water reaches the next pond is considered to be negligible. The test starts at time 0 with all ponds being empty. Then, all valves are opened simultaneously. The test stops and the valves are closed when all ponds are filled by water.</p>

<p>The pond capacities and valves flow rate are known, you have to determine the moment when the lowest pond starts to overflow and the first moment when all ponds are filled.</p>

### 입력 

 <p>There are more test cases. Each test case consists of two lines. The first line contains two integers N (1 ≤ N ≤ 10<sup>5</sup> , 1 ≤ F ≤ 10<sup>9</sup>) separated by space. N is the number of ponds, F is the rate of water flow through each valve. We consider the flow to be expressed in litres per second. The second line contains a sequence of N integers C<sub>i</sub> (1 ≤ C<sub>i</sub> ≤ 10<sup>9</sup>) separated by spaces and representing the pond capacities expressed in litres. The sequence reflects the order of ponds from the topmost one to the lowest one.</p>

### 출력 

 <p>For each test case, print a single line with two numbers separated by space. The first number represents the time in which the lowest pond in the cascade starts to overflow. The second number represents the duration of the test. Both times should be printed in seconds and should be accurate within an absolute or relative error of 10<sup>−6</sup>.</p>

