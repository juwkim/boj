# [Bronze I] Spaceship - 16244 

[문제 링크](https://www.acmicpc.net/problem/16244) 

### 성능 요약

메모리: 41620 KB, 시간: 132 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Space Ranger is caught at an alien spaceship. He is surrounded by enemies. To break free he needs to destroy all enemies in some particular order.</p>

<p>There are n enemies around Space Ranger, the i-th of them has power fi. To break free Space Ranger needs to destroy all enemies in such order, that the power of the last destroyed enemy is equal to the sum of powers of all other enemies.</p>

<p>Space Ranger is short of time, so he has failed to find the required order. Help him! Find the way to destroy all enemies and break free.</p>

### 입력 

 <p>The first line of input contains n — the number of enemies (2 ≤ n ≤ 10<sup>5</sup>).</p>

<p>The second line contains n integers f<sub>i</sub> — powers of the enemies (-10<sup>9</sup> ≤ f<sub>i</sub> ≤ 10<sup>9</sup>).</p>

### 출력 

 <p>Output values f<sub>i</sub> in order in which the enemies must be destroyed. If there are several ways to destroy all enemies and break free, print any one. It is guaranteed that there is at least one way to do it.</p>

