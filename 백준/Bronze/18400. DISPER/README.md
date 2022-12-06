# [Bronze I] DISPER - 18400 

[문제 링크](https://www.acmicpc.net/problem/18400) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

구현(implementation), 수학(math), 통계학(statistics)

### 문제 설명

<p>The university of “AAA” is interested to investigate and evaluate their performance of professors. They are interested to know who has the less consistency. For this purpose, the university needs to find an approach so that it considers the contribution of all marks of students over a single mark. The University found that the variance of the marks can help them find who has the less consistency. In general, the less consistency has the high dispersion. The highest mark a student can have is limited to 100, moreover, all students have exactly the same number of curses. Additionally, for any students who have missed the course the mark considered to be the lowest possible mark. Variance Formula:</p>

<p>In this formula x shows different mark, represents the mean value of mark. N stands for number of marks.</p>

<p style="text-align: center;">σ = Σ(x - μ)<sup>2</sup> / N</p>

### 입력 

 <p>First line contains the number of test cases (T): 1 ≤ T ≤ 100</p>

<p>Second line indicates the number of professors to be evaluated. P ranges 1 ≤ P ≤ 30 Therefore, next P lines contain the marks for each professor separated by ", ".</p>

<p>Each mark M is an integer (0 ≤ M ≤ 100)</p>

### 출력 

 <p>The Pth professor with less consistency and its dispersion score with accuracy of 2 decimal points separated by tab.</p>

