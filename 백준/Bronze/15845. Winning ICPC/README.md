# [Bronze II] Winning ICPC - 15845 

[문제 링크](https://www.acmicpc.net/problem/15845) 

### 성능 요약

메모리: 28776 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>There are N teams (numbered from 1 to N) and M problems (numbered from 1 to M) in this year's ICPC. The j-th problem has T<sub>j</sub> testcases. Surprisingly, every team submitted exactly one solution to every problem. The i-th team managed to solve S<sub>i,j</sub> testcases on the j-th problem.</p>

<p>A team solved a problem only if the team managed to solve ALL testcases on that problem. The winning team is the team with the most number of problems solved. If there are more than one team with the most number of problems solved, then the winning team is the team with the smallest index among those teams.</p>

<p>Determine the index of the winning team.</p>

### 입력 

 <p>The first line contains two integers: N M (1 ≤ N, M ≤ 100) in a line denoting the number of teams and the number of problems. The second line contains M integers: T<sub>1</sub> T<sub>2</sub> ... T<sub>M</sub> (0 ≤ T<sub>i</sub> ≤ 100) in a line denoting the number of testcases. The next N following lines, each contains M integers; the j-th integer on the i-th line is S<sub>i,j</sub> (0 ≤ S<sub>i,j</sub> ≤ T<sub>j</sub>) denoting the number of solved testcases by the i-th team for the j-th problem.</p>

### 출력 

 <p>The output contains the index of the winning team, in a line.</p>

