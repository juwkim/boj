# [Silver IV] Rasvjeta - 15360 

[문제 링크](https://www.acmicpc.net/problem/15360) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

Empty

### 문제 설명

<p>It is Advent season. There are M street lights in a street N metres long (the meters of the street are denoted with numbers from 1 to N). Each of the lights lights up the meter of the street it’s located in and K meters to the left and to the right of that location. In other words, if the light is located at meter X, it lights up all metres of the street from X - K to X + K, inclusively. Of course, it is possible for a meter of the street to be lit up by multiple street lights. All lights have distinct locations.</p>

<p>The problem is that there is a possibility that the lights don’t light up all N metres of the street. It is your task to determine the minimal amount of additional lights needed to be put up (at position from 1 to N) so that the entire street is lit up.</p>

### 입력 

 <p>The first line of input contains the number N (1 ≤ N ≤ 1000).</p>

<p>The second line of input contains the number M (1 ≤ M ≤ N).</p>

<p>The third line contains the number K (0 ≤ K ≤ N).</p>

<p>Each of the following M lines contains a number. The numbers are sorted in ascending order and represent the positions of each of the M street lights.</p>

<p>The positions will be distinct and from the interval [1, N].</p>

### 출력 

 <p>You must output the required number from the task.</p>

