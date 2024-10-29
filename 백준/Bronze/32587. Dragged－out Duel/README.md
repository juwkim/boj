# [Bronze III] Dragged-out Duel - 32587 

[문제 링크](https://www.acmicpc.net/problem/32587) 

### 성능 요약

메모리: 111332 KB, 시간: 124 ms

### 분류

분류 없음

### 제출 일자

2024년 10월 29일 16:32:20

### 문제 설명

<p>Your friend Guile and you have decided to spend an afternoon playing the new Street Fighter game, but you both want to start on the left, because you have both only practiced all your combos starting from the left. You decide to determine who starts on the left like true men -- with an intense grueling, and exhausting duel of rock-paper-scissors.</p>

<p>The duel will be a best-of-$n$, consisting of $n$ single rounds of rock-paper-scissors (yes, you may have to play rock-paper-scissors <em>ten thousand times</em>, truly a war of attrition), and whoever wins more rounds, gets to start on the left. If you both pick the same option in an individual game, it is not replayed. To keep track of who wins, you decide to write a program, that determines whether you beat Guile in this great duel.</p>

<p>As a reminder: rock beats scissors, scissors beats paper, paper beats rock. If you both make the same choice, the round is a draw.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with a single integer $n$ ($1\leq n\leq 10\,000$), the number of individual games.</li>
	<li>Two lines with $n$ characters, each character being either '<code>R</code>' for rock, '<code>P</code>' for paper, or '<code>S</code>' for scissors. The first line represents your choices in each round, and the second line represents Guile's choices in each round.</li>
</ul>

### 출력 

 <p>If you have won the most rounds of rock-paper-scissors, output "<code>victory</code>". If Guile has won the most rounds of rock-paper-scissors, output "<code>defeat</code>".</p>

<p>It is guaranteed that the both of you will not have the same number of wins.</p>

