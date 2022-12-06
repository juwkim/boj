# [Silver V] Easy Problemset - 11739 

[문제 링크](https://www.acmicpc.net/problem/11739) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Perhaps one of the hardest problems of any ACM ICPC contest is to create a problemset with a reasonable number of easy problems. On Not Easy European Regional Contest this problem is solved as follows.</p>

<p>There are n jury members (judges). They are numbered from 1 to n. Judge number i had prepared p<sub>i</sub> easy problems before the jury meeting. Each of these problems has a hardness between 0 and 49 (the higher the harder). Each judge also knows a very large (say infinite) number of hard problems (their hardness is 50). Judges need to select k problems to be used on the contest during this meeting.</p>

<p>They start to propose problems in the ascending order of judges numbers. The first judge takes the first problem from his list of remaining easy problems (or a hard problem, if he has already proposed all his easy problems) and proposes it. The proposed problem is selected for the contest <strong>if its hardness is greater than or equal to the total hardness of the problems selected so far</strong>, otherwise it is considered too easy. Then the second judge does the same etc.; after the n-th judge, the first one proposes his next problem, and so on. This procedure is stopped immediately when k problems are selected.</p>

<p>If all judges have proposed all their easy problems, but they still have selected less than k problems, then they take some hard problems to complete the problemset regardless of the total hardness.</p>

<p>Your task is to calculate the total hardness of the problemset created by the judges.</p>

### 입력 

 <p>The first line of the input file contains the number of judges n (2 ≤ n ≤ 10) and the number of problems k (8 ≤ k ≤ 14). The i-th of the following n lines contains the description of the problems prepared by the i-th judge. It starts with p<sub>i</sub> (1 ≤ p<sub>i</sub> ≤ 10) followed by p<sub>i</sub> non negative integers between 0 and 49 — the hardnesses of the problems prepared by the i-th judge in the order they will be proposed.</p>

### 출력 

 <p>Output the only integer — the total hardness of the selected problems.</p>

