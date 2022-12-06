# [Bronze III] Scavenger Hunt - 6030 

[문제 링크](https://www.acmicpc.net/problem/6030) 

### 성능 요약

메모리: 29028 KB, 시간: 68 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math), 정수론(number_theory)

### 문제 설명

<p>Farmer John has scattered treats for Bessie at special places in the pasture.  Since everyone knows that smart cows make tasty milk, FJ has placed the treats at locations that require Bessie to think. He has given her two numbers, P and Q (1 <= P <= 6,000; 1 <= Q <= 6,000), and she has to check every point in the pasture whose x-coordinate is a factor of P and whose y-coordinate is a factor of Q to find her treat.</p>

<p>Suppose FJ gives Bessie P = 24 and Q = 2. Here are all of their respective factors:</p>

<ul>
	<li>P = 24 => 1, 2, 3, 4, 6, 8, 12, 24</li>
	<li>Q = 2 => 1, 2</li>
</ul>

<p>Bessie would thus check grid locations: (1, 1), (1, 2), (2, 1), (2, 2), (3, 1)...</p>

<p>Help Bessie by printing all of the points she ought to check.</p>

### 입력 

 <ul>
	<li>Line 1: Two space separated integers: P and Q</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..?: A complete list of unique pairs of space-separated integers sorted by the first number and, if tied, the second number: a factor of P followed by a factor of Q</li>
</ul>

<p> </p>

