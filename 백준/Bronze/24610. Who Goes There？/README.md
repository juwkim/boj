# [Bronze II] Who Goes There? - 24610 

[문제 링크](https://www.acmicpc.net/problem/24610) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>What happens when more teams want to go to an ICPC regional site than the site has capacity for? Who goes there?</p>

<p>One possible policy is the following: Every school is allowed to register as many teams as they wish. Accept every school's first team, then accept every school's second team (for schools with more than one team), then third, and so on, until all teams are accepted, or there isn't enough capacity for the next wave. Then, if there are extra spots available, the spots are given to schools, one by one, in the order that the schools registered.</p>

<p>Given the capacity of a site, the number of teams registered by each school and the order that they registered, determine how many teams from each school are accepted.</p>

### 입력 

 <p>The first line of input contains two integers $n$ ($1 \le n \le 100$) and $m$ ($1 \le m \le 100$), where $n$ is the capacity of the site and $m$ is the number of schools that wish to compete there.</p>

<p>Each of the next $m$ lines contains an integer $t$ ($1 \le t \le 100$), which is the number of teams that a school has registered. The schools are listed in the order that they registered.</p>

### 출력 

 <p>Output $m$ lines, one for each school. Each line must contain a single integer indicating the number of teams accepted from that school. Output them in the same order as they appear in the input.</p>

