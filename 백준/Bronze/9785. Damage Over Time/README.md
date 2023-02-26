# [Bronze I] Damage Over Time - 9785 

[문제 링크](https://www.acmicpc.net/problem/9785) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting)

### 문제 설명

<p>In many MMORPGs (Massively Multiplayer Online Role-Playing Games), damage over time (DoT) is one of the good ways for the attacker to deal damage on enemies. For example, a rogue in World of Warcraft (WoW) may apply a poison to his knife and then stab it on an enemy using “Garrote” ability. Both poison and garrote offer the damage over time. For example, poison deals 10 damages per second for 10 seconds and garrote deals 20 damages per second for 5 seconds. That is, “stacking” as many DoT as possible on enemy certainly results in great total damages.</p>

<p>Here is the problem. You are required to write a program, for a set of provided DoT abilities, to calculate the possible maximum DoT and the maximum length of time of such DoT to be hold. In the example above, the possible maximum DoT is 30 damages for 5 seconds.</p>

### 입력 

 <p>The first line of the input includes integer N (0 < N < 100) indicating the number of abilities and integer M (0 < M < 100, M ≤ N) indicating how many abilities can be “stacked up” at one time. Then, each ability is input by its damage per seconds and its length (seconds), one ability per one line.</p>

### 출력 

 <p>Print out the maximum DoT being possible to apply to an enemy using the provided set of abilities and the length of time such maximum DoT hold.</p>

