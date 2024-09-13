# [Silver III] Meganominoes - 4129 

[문제 링크](https://www.acmicpc.net/problem/4129) 

### 성능 요약

메모리: 119572 KB, 시간: 160 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵

### 제출 일자

2024년 9월 14일 02:27:06

### 문제 설명

<p>A meganomino is a tile with two ends and a number of dots on each end. Each end can have as few as 0 and as many as 1000000000 dots. In this puzzle, you must place two meganominoes next to each other so that one end of one meganomino touches one end of the other meganomino. The number of dots on the touching ends must be the same on both meganominoes. In addition, the sum of the number of dots on the opposite (non-touching) ends of the meganominoes must be equal to a given number i.</p>

### 입력 

 <p>The first line of input contains two integers 0 < n < 10000 and 0 < m <= 100, the number of meganominoes and the number of queries. The next n lines each contain two integers, the number of dots on each end of a meganomino tile. No two meganomino tiles are the same. The next m lines each contain one of the given sums i.</p>

### 출력 

 <p>Output a total of m lines, one for each given sum i. On each such line, output a single integer, the number of (unordered) pairs of meganomino tiles that satisfy the constraints. The two tiles in a given pair must be distinct (i.e. a single tile cannot be used twice within a single pair).</p>

