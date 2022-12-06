# [Silver V] And the Winner Is... Ourselves! - 17509 

[문제 링크](https://www.acmicpc.net/problem/17509) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting)

### 문제 설명

<p>Let us remind you about how the total penalties are calculated for this contest:</p>

<ul>
	<li>When you solve a problem at $T$ minutes, $T+20V$ is added to your penalty, where $V$ is the number of incorrect verdicts (except compile errors) received on that problem.</li>
	<li>If you do not solve a problem before the contest ends, the incorrect verdicts on that problem are not counted as penalties.</li>
</ul>

<p>Here is a bad news for all of you: we, the problem setters, are planning to join the competition and solve our own problems!</p>

<p>We know our problems really well, so we can solve all the problems before the contest ends. Furthermore, we can precisely predict how long it takes to solve each problem, and how many incorrect verdicts (except compile errors) we get in each problem. Depending on the order of the problems we solve, our total penalty might differ. What is the minimum penalty if we solve all problems?</p>

### 입력 

 <p>11 lines are given as the input. The $i$-th line contains two space-separated integers, $D_i$ and $V_i$, where $D_i$ is the amount of minutes required to solve the $i$-th problem, and $V_i$ is the number of incorrect verdicts on the $i$-th problem.</p>

<p>For each $i$, $1 \leq D_i$ and $0 \leq V_i \leq 1\ 000$. Also, $\sum_{i=1}^{11} D_i \leq 300$.</p>

### 출력 

 <p>Output the minimum penalty if we solve all problems.</p>

