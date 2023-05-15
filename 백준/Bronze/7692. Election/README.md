# [Bronze II] Election - 7692 

[문제 링크](https://www.acmicpc.net/problem/7692) 

### 성능 요약

메모리: 116248 KB, 시간: 192 ms

### 분류

구현

### 문제 설명

<p>Given the voting preferences of a population of M people, you are to determine the winner of an election among N candidates, numbered 1, . . . , N. For this problem, the M people are partitioned into G “groups” where all members within a group have the same voting preferences. The candidate preferences for a group are specified by listing candidates from most preferred to least preferred. Election results are determined by an instant-runoff voting procedure.</p>

<p>In this method, the first choices of the M people in the population are counted and the least popular candidate is eliminated. In the event of a tie, the highest-numbered candidate is eliminated. Then, the eliminated candidate is removed from the preference list of all M individuals in the population, and again the least popular candidate is eliminated. This process repeats until only a single candidate is left.</p>

### 입력 

 <p>The input test file will contain multiple test cases. Each input test case begins with a single line containing the integers G and N where 2 ≤ N ≤ 5 and 1 ≤ G ≤ 20. The next G lines are of the format “Mi a<sub>i1</sub> a<sub>i2</sub> . . . a<sub>iN</sub> ” where 1 ≤ M<sub>i</sub> ≤ 20 and a<sub>i1</sub>, . . . , a<sub>iN</sub> is a permutation of the integers 1, . . . , N. M<sub>i</sub> is the number of individuals in the ith group, and a<sub>i1</sub>, . . . , a<sub>iN</sub> is the ordering of the N candidates from most preferred to least preferred for the ith group. The end-of-file is marked by a test case with G = N = 0 and should not be processed.</p>

### 출력 

 <p>For each input case, the program should print the winner of the election on a single line.</p>

