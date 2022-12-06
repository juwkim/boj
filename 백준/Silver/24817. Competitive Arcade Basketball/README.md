# [Silver V] Competitive Arcade Basketball - 24817 

[문제 링크](https://www.acmicpc.net/problem/24817) 

### 성능 요약

메모리: 140472 KB, 시간: 424 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 시뮬레이션(simulation), 문자열(string), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>You're attending a arcade basketball competition, where the objective is to score as many points as possible until the time runs out. The announcer has informed the crowd that their scoreboard is broken, so they don't have a way to keep track of all the scores. As a seasoned programmer, you feel you can whip up a program that can keep track of the names of the players and the amount of points they've scored, announcing the winner(s) at the end of the contest. </p>

### 입력 

 <p>The first line contains three integers: the number of participants $n$ ($1 \le n \le 100\,000$); the minimum number $p$ of points required to win the contest ($10 \le p \le 10\,001$); and $m$, the number of lines with player names and points ($1 \le m \le 200\,000$). The next $n$ lines contain the names of the participants, each mentioned exactly once. Each name consist of no more than $20$ alphanumerical characters. The remaining $m$ lines each contain the name of a participant, followed by how many points they scored ($1$, $2$, or $3$).</p>

### 출력 

 <p>Output the names of those participants who reached the minimum required score, one per line! Output "<code><Winner> wins!</code>" for each winner. Output the winners in the order in which they've reached the required score. If no one reaches the minimum required score, output "<code>No winner!</code>" (including the exclamation mark!).</p>

