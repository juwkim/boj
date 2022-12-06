# [Silver V] Recess Rocks - 20568 

[문제 링크](https://www.acmicpc.net/problem/20568) 

### 성능 요약

메모리: 140580 KB, 시간: 192 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting)

### 문제 설명

<p>As one gets older, it becomes harder to keep track of the latest fads and trends. The latest mind-boggling trend is actually sweeping through elementary schools: young children love rocks, even more than they love paper or scissors. As recess ends, Ms. Frizz needs to round up her class. Before going back to the classroom, the students all get in a line, holding bags full of rocks that they've mined from the playground.</p>

<p>The kids in this class are a dangerous combination of personality traits: they are jealous, smart, eagle-eyed, and good at counting. Each child knows how many rocks every child in front of them has. That is, the line leader knows their own rock total, the second kid in line knows the amount of rocks they have and the line leader has, the third student knows the rock totals of the first three students in line, and so on.</p>

<p>If a kid knows about another kid in front of them that has the same or more rocks than them, they begin crying. The line-leader never cries, as they have to set a mature, stoic example for their classmates.</p>

<p>If Ms. Frizz arranges the students optimally, what is the minimum number of students that are crying after recess?</p>

### 입력 

 <p>The first line of input is an integer $N$ ($1 \leq N \leq 10^5$. Class sizes are getting large due to budget cuts). The next line has $N$ space-separated integers; the $i$-th is the number of rocks child $i$ has. Each child has at least $1$ and at most $10^9$ rocks.</p>

### 출력 

 <p>Output a single integer: the minimum number of children who are crying if the students are arranged optimally.</p>

