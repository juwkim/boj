# [Silver V] Watchdog - 7378 

[문제 링크](https://www.acmicpc.net/problem/7378) 

### 성능 요약

메모리: 116612 KB, 시간: 264 ms

### 분류

브루트포스 알고리즘(bruteforcing), 기하학(geometry), 구현(implementation), 피타고라스 정리(pythagoras)

### 문제 설명

<p>A company (name withheld) has an office building in the center of Lund. The building has a perfectly square roof with a number of hatches. Because of a series of burglaries where the perpetrators have entered through these hatches, it was decided to use a watchdog to guard the hatches. A particularly vicious but rather stupid breed of dog was chosen, and unfortunately the dog fell off the roof on its third watch.</p>

<p>A new dog has been procured and it has been decided to attach a leash to its collar and attach the other end at some point on the roof. However, if the leash is too short the dog cannot reach all hatches, but if it is too long then the dog will fall off the building again. The leash has hooks at both ends, so no part of it is used to tie knots. The company wants the dog to reach the center of each hatch (the dog can reach exactly as far as the leash could reach if it were lying flat on the roof), but it does not want the leash to extend beyond the edge of the roof (to the edge is OK). They hope that by carefully choosing the length of the leash and where to attach it, the dog will be able to reach all hatches without risking falling off the building. A leash can only be attached at a point with integer coordinates (if the building is 10 by 10 meters, then the south-west corner of the building has coordinates (0, 0) and the north-east corner has coordinates (10, 10)). A leash cannot be attached at a point where there is a hatch.</p>

<p>If there is no place where you can attach a leash, reach all hatches but not reach beyond the edge of the roof, it is impossible to use this breed of dog, and the company will instead use a poodle (which is a less vicious type of dog, but also less prone to falling off buildings).</p>

### 입력 

 <p>On the first line of the input is a single positive integer N, telling the number of test cases to follow. Each case starts with one line with two integers S H, where S is even, 2 ≤ S ≤ 40, and 1 ≤ H ≤ 50. S is the side of the square roof in meters and H is the number of hatches. The following H lines each contain two integers X and Y . These are the coordinates of the hatches. Hatches will never lie outside the roof or on the roof‘s perimeter. No two hatches will occupy the same position</p>

### 출력 

 <p>For each test case, output one line containing the coordinates X Y at which to fasten the leash (if there are several possible points, output the one with smallest X, and if there are still several possibilities select the one with smallest Y among those with smallest X) such that a leash of suitable length allows access to all hatches without extending beyond the edge of the roof. If there is no such point, output “poodle” for that test case.</p>

