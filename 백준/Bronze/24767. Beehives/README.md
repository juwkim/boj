# [Bronze II] Beehives - 24767 

[문제 링크](https://www.acmicpc.net/problem/24767) 

### 성능 요약

메모리: 30840 KB, 시간: 80 ms

### 분류

브루트포스 알고리즘(bruteforcing), 기하학(geometry), 피타고라스 정리(pythagoras)

### 문제 설명

<p>Bill the beekeeper has a problem! His bees like to fight with each other instead of producing honey. If the bees fight each other, then the honey turns out sour. The only way to stop the bees from fighting and keep the honey sweet is to ensure that the hives are not too close together. Help Bill figure out how many of this season's hives will produce sour honey.</p>

<p>Bill's hives all exist on a plane, and he knows some distance d such that two hives within d of each other will fight, and both will produce sour honey. If a hive does not fight with any other hives, it produces sweet honey. Given d and the positions of N beehives, output how many hives will produce sweet honey and how many hives will produce sour honey.</p>

### 입력 

 <p>Input will be provided on multiple lines. Each case will begin with a floating point number d (0 < d < 1000.0), the distance within which hives will fight. On the next line will be N (1 ≤ N ≤ 100), the number of hives in that case. The next N lines will contain two floating point numbers separated by a single space, x and y (-1000.0 ≤ x,y ≤ 1000.0), which give the position of each hive. No two hives will be at the exact same location. Input will be terminated by a line containing the string <code>0.0 0</code>.</p>

### 출력 

 <p>For each case output a line of the following form: <code>a sour, b sweet</code> where <code>a</code> and <code>b</code> are the number of hives producing sour and sweet honey, respectively.</p>

