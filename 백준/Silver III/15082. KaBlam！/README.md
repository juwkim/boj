# [Silver III] KaBlam! - 15082 

[문제 링크](https://www.acmicpc.net/problem/15082) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

기하학, 구현, 물리학

### 제출 일자

2024년 2월 16일 05:10:51

### 문제 설명

<p>You’ve been asked to write software to help launch anti-missile rockets in order to take out missiles shot by the enemy. You’ve decided to use a simple 2-dimensional model, with the launch site of the missile located on the x axis at (x<sub>m</sub>, 0) and your anti-missile launch site at (x<sub>a</sub>, 0) (all values in feet). You also know the initial x and y velocities of the missile at the moment of launch: v<sub>x</sub> and v<sub>y</sub> (in feet per second). Given this information, you know that if the missile is launched at time 0 then the location of the missile at any later time t is given by</p>

<p style="text-align:center">(x<sub>m</sub> + v<sub>x</sub>t, v<sub>y</sub>t − 16t<sup>2</sup>)</p>

<p>The image below shows one possible trajectory for the missile and the anti-missile. Note that the missile’s trajectory is a parabola while the anti-missile’s trajectory is a straight line. Also note in this scenario that v<sub>x</sub> is negative (v<sub>y</sub> will always be positive).</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15082/1.png" style="height:295px; width:556px"></p>

<p>Your higher-ups want to be able to destroy the missile at a specific time t<sub>K</sub>. Your job is to decide when to shoot your anti-missle and at what angle α so that you intercept the enemy’s missile at that time. To aid in your calculations you also know the velocity of your anti-missile along its trajectory, v<sub>a</sub>. Note that it might be impossible to destroy the missile at time t<sub>K</sub>, either because you would have had to shoot your anti-missile before the enemy’s missile is launched, or because the missile would have already landed (and blown up) prior to or at time t<sub>K</sub>. If that’s the case, your software should sound an alarm so that everyone can start running.</p>

### 입력 

 <p>Input consists of a single line containing six integers: x<sub>m</sub> v<sub>x</sub> v<sub>y</sub> x<sub>a</sub> v<sub>a</sub> t<sub>K</sub>, where 0 < v<sub>y</sub>, v<sub>a</sub>, t<sub>K</sub> ≤ 10000, −10000 ≤ x<sub>m</sub>, v<sub>x</sub>, x<sub>a</sub> ≤ 10000 and x<sub>m</sub> ≠ x<sub>a</sub>.</p>

### 출력 

 <p>If it is impossible to destroy the missile at the requested time, display the phrase start running. Otherwise, display two values t<sub>L</sub> α, where t<sub>L</sub> is the time to launch your anti-missile and α is the launch angle (in degrees). Both values should have a maximum relative or absolute error of 10<sup>−4</sup>.</p>

