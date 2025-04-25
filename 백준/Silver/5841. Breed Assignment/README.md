# [Silver I] Breed Assignment - 5841 

[문제 링크](https://www.acmicpc.net/problem/5841) 

### 성능 요약

메모리: 111412 KB, 시간: 4016 ms

### 분류

백트래킹, 브루트포스 알고리즘

### 제출 일자

2025년 4월 25일 21:18:28

### 문제 설명

<p>Farmer John has N cows (2 <= N <= 15) that are each one of three different breeds: Holsteins, Jerseys, or Guernseys.</p><p>Unfortunately, FJ cannot remember the exact breeds of his cows!  He does, however, remember a list of K (1 <= K <= 50) relationships between pairs of cows; for example, he might remember that cows 1 and 2 have the same breed, or that cows 1 and 5 have different breeds.</p><p>Give FJ's list of relationships between pairs of cows, please help him compute the number of different possible assignments of breeds to his cows (this number could be zero if his list contains contradictory information).</p>

### 입력 

 <ul><li>Line 1: Two space-separated integers: N and K.</li><li>Lines 2..1+K: Each line describes the relationship between a pair of cows x and y (1 <= x,y <= N, x != y).  It is either of the form "S x y", meaning that x and y have the same breed, or "D x y", meaning that x and y have different breeds.</li></ul>

### 출력 

 <ul><li>Line 1: The number of possible breed assignments.</li></ul>

