# [Bronze III] Walktober - 26432 

[문제 링크](https://www.acmicpc.net/problem/26432) 

### 성능 요약

메모리: 132876 KB, 시간: 488 ms

### 분류

구현(implementation)

### 문제 설명

<p>John participates in an annual walking competition called <i>Walktober</i>. The competition runs for a total of $\mathbf{N}$ days and tracks the daily steps of the participants for all the $\mathbf{N}$ days. Each participant will be assigned a unique ID ranging from $1$ to $\mathbf{M}$ where $\mathbf{M}$ is the total number of registered participants. A global scoreboard is maintained tracking the daily steps of each participant.</p>

<p>John is determined to win Walktober this year and his goal is to score the maximum daily steps on each of the $\mathbf{N}$ days among all the participants. Having participated in Walktober last year as well, he wanted to know how many steps he fell short of in achieving his goal. Given the previous year scoreboard, calculate the minimum additional steps he needed over his last year score in order to achieve his goal of scoring the maximum daily steps every day.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, $\mathbf{T}$. $\mathbf{T}$ test cases follow.</p>

<p>The first line of each test case contains three integers $\mathbf{M}$, $\mathbf{N}$, and $\mathbf{P}$ denoting the total number of participants, the total number of days the competition runs, and the last year participant ID of John.</p>

<p>The next $\mathbf{M}$ lines describe the scoreboard of the previous year and contains $\mathbf{N}$ integers each. The $j$-th integer of the $i$-th line denotes the step count $\mathbf{S_{i,j}}$ of the participant with ID $i$ on the $j$-th day of the competition.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where $x$ is the test case number (starting from 1) and $y$ is the minimum total additional steps needed by John to achieve his goal.</p>

