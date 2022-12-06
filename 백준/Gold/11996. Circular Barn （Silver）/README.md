# [Gold IV] Circular Barn (Silver) - 11996 

[문제 링크](https://www.acmicpc.net/problem/11996) 

### 성능 요약

메모리: 32452 KB, 시간: 88 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>Being a fan of contemporary architecture, Farmer John has built a new barn in the shape of a perfect circle. Inside, the barn consists of a ring of \(n\) rooms, numbered clockwise from \(1 \ldots n\) around the perimeter of the barn (\(3 \leq n \leq 1000\)). Each room has doors to its two neighboring rooms, and also a door opening to the exterior of the barn.</p>

<p>Farmer John owns \(n\) cows, and he wants exactly one cow to end up in each room in the barn. However, the cows, being slightly confused, line up at haphazard doors, with possibly multiple cows lining up at the same door. Precisely \(c_i\) cows line up outside the door to room \(i\), so \(\sum c_i = n\).</p>

<p>To manage the process of herding the cows so that one cow ends up in each room, Farmer John wants to use the following approach: each cow enters at the door at which she initially lined up, then walks clockwise through the rooms until she reaches a suitable destination. Given that a cow walking through \(d\) doors consumes \(d^2\) energy, please determine the minimum amount of energy needed to distribute the cows so one ends up in each room.</p>

### 입력 

 <p>The first line of input contains \(n\). Each of the remaining \(n\) lines contain \(c_1 \ldots c_n\).</p>

### 출력 

 <p>Please write out the minimum amount of energy consumed by the cows.</p>

