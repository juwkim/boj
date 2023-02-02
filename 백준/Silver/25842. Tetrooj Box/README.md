# [Silver IV] Tetrooj Box - 25842 

[문제 링크](https://www.acmicpc.net/problem/25842) 

### 성능 요약

메모리: 114328 KB, 시간: 120 ms

### 분류

애드 혹(ad_hoc), 브루트포스 알고리즘(bruteforcing), 구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Dr. Orooji’s children have played Tetris but are not willing to help Dr. O with a related problem. Dr. O’s children don’t realize that Dr. O is lucky to have access to 100+ great problem solvers and great programmers today!</p>

<p>Dr. O knows the length of the base for a 2D box and wants to figure out the needed height for the box. Dr. O will drop some 2D blocks (rectangles) on the base. A block will go down until it lands on the base or is stopped by an already-dropped block (i.e., it lands on that block). After all the blocks have been dropped, we can determine the needed height for the box – the tallest column is the needed height (please see pictures on the next page corresponding to Sample Input/Output).</p>

### 입력 

 <p>The first input line contains two integers: b (1 ≤ b ≤ 100), indicating the length of the base and r (1 ≤ r ≤ 50), indicating the number of blocks (rectangular pieces) to be dropped. Each of the next r input lines contains three integers: a block’s horizontal length h (1 ≤ h ≤ 100), the block’s vertical length v (1 ≤ v ≤ 100), and c (c ≥ 1), the leftmost column the block is dropped into. Assume that the h and c values will be such that the block will not go beyond the box base, i.e., (c + h – 1) ≤ b.</p>

### 출력 

 <p>Print the needed height for the box (the tallest column is the height).</p>

