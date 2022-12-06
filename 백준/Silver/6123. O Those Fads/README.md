# [Silver V] O Those Fads - 6123 

[문제 링크](https://www.acmicpc.net/problem/6123) 

### 성능 요약

메모리: 117832 KB, 시간: 200 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting)

### 문제 설명

<p>Like any other teenager, teen cows are occasionally overtaken by fads. Sometimes it's a hula hoop or a pet rock, other times it's Counterstrike, Pokemon, Rick Astley, or tribal tattoos on their udders.</p>

<p>Mathematically, we know that a fad has an initial attractiveness level L (1 <= L <= 50,000). Cow i has a resistance (0 <= R_i <= 1,000,000) that tells how long she can avoid a fad before having no alternative but to participate. When a fad's attractiveness level meets or exceeds a cow's fad resistance, then the cow will want to participate in the fad.</p>

<p>Each cow who participates in a fad increases (through peer pressure) that fad's attractiveness by some value K (1 <= K <= 2,500).</p>

<p>Given a population of N (1 <= N <= 100,000) cows, determine how many will participate in a fad.</p>

### 입력 

 <ul>
	<li>Line 1: Three space-separated integers: N, L, and K</li>
	<li>Lines 2..N+1: Line i+1 contains cow i's a single integer that is fad resistance: R_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the number of cows how ultimately participate in the fad.</li>
</ul>

<p> </p>

