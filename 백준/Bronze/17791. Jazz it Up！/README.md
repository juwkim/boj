# [Bronze I] Jazz it Up! - 17791 

[문제 링크](https://www.acmicpc.net/problem/17791) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

수학(math), 정수론(number_theory)

### 문제 설명

<p>.lilypond.org Along with some friends you formed the Band of Atonal Percussionists and Cellists. You have been playing for some years together, but you feel unsatisfied with the current level of play. Doing research into some interesting new styles, you are gripped by the intricate details of the world of jazz.</p>

<p>While of course you cannot apply all the new things you have learned immediately, you want to start with improvising some nice new rhythmic figures in the music your band plays. You will play a rhythm where every bar has n beats in it, but then you split up every beat into m notes. In total, you will have nm notes per bar.</p>

<p>Everyone in the band knows that there is no room for squares in jazz. So the number of notes in a bar should be squarefree. That is, there is no number k > 1 such that k<sup>2</sup> divides the number of notes in a bar.</p>

<p>The percussionist has already suggested a number of beats per bar n; now it is up to you to find a number of notes per beat that does not leave any room for squares.</p>

<p>In the second sample we have n = 30 and m = 7. This works because 2 ≤ m < n and m × n = 210 has no divisor k<sup>2</sup> for any k > 1.</p>

### 입력 

 <ul>
	<li>The input is a single squarefree integer 3 ≤ n ≤ 10<sup>5</sup>.</li>
</ul>

### 출력 

 <ul>
	<li>Output an integer 2 ≤ m < n such that m × n is still squarefree.</li>
</ul>

<p>If there are multiple possible solutions, you may output any one of them.</p>

