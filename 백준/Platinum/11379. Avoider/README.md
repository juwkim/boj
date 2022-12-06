# [Platinum II] Avoider - 11379 

[문제 링크](https://www.acmicpc.net/problem/11379) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

다이나믹 프로그래밍(dp), 런타임 전의 전처리(precomputation)

### 문제 설명

<p>Consider points with integer coordinates in the plane. We start from the origin, make a first step towards the point (1, 0) and then every next step is a move to one of the four neighboring integer points (up, down, left or right) so that we are always at a point with nonnegative coordinates. Moreover, it is not allowed to visit twice a point. Let us count how many different routes of the described kind we may obtain using n steps. For example, when n = 2, 3 and 4, counting the routes gives 2, 5 and 12, respectively.</p>

<p style="text-align: center;"><img alt="" src="" style="height:348px; width:527px"></p>

<p>Write program avoider that inputs two positive integers a and b (0 < a < b < 29) and displays the sum of counting the number of routes for values of n = a, a + 1, ..., b.</p>

### 입력 

 <p>Two positive integers a and b (0 < a < b < 29)</p>

### 출력 

 <p>The sum of counting the number of routes for values of n = a, a + 1, ..., b.</p>

