# [Bronze II] Richard Hamming - 13456 

[문제 링크](https://www.acmicpc.net/problem/13456) 

### 성능 요약

메모리: 28776 KB, 시간: 80 ms

### 분류

구현(implementation)

### 문제 설명

<p>The Hamming distance dH( ⃗v, ⃗u) between two n-dimensional vectors ⃗v = (v<sub>1</sub>, . . . , v<sub>n</sub>) and ⃗u =(u<sub>1</sub>, . . . , u<sub>n</sub>) is defined as dH( ⃗v, ⃗u) = |{i : v<sub>i ≠</sub> u<sub>i</sub> and i ∈ {1, . . . , n}}|, i.e., the number of positions at which the corresponding entries are different. For example, the Hamming distance between (1, 2, 3, 4, 5) and (1, 0, 0, 4, 5) is 2, since these two vectors differ only at the second and the third positions. Please write a program to compute the Hamming distance between two n-dimensional vectors.</p>

### 입력 

 <p>On the first line there is a single integer T (T ≤ 100) indicating the number of test cases. Each test case consists of three lines. The first line of each test case contains an integer n (0 < n ≤ 50) indicating the dimension of the vectors. The second line contains n integers v<sub>1</sub>, . . . , v<sub>n</sub>, and the third line contains n integers u<sub>1</sub>, . . . , u<sub>n</sub>. You may assume that v<sub>1</sub>, . . . , v<sub>n</sub>, u<sub>1</sub>, . . . , u<sub>n</sub> ∈ {0, 1, . . . , 99}.</p>

### 출력 

 <p>For each test case, output the Hamming distance between (v<sub>1</sub>, . . . , v<sub>n</sub>) and (u<sub>1</sub>, . . . , u<sub>n</sub>).</p>

