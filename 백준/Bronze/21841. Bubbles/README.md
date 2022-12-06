# [Bronze I] Bubbles - 21841 

[문제 링크](https://www.acmicpc.net/problem/21841) 

### 성능 요약

메모리: 30840 KB, 시간: 452 ms

### 분류

조합론(combinatorics), 수학(math)

### 문제 설명

<p>One popular method of controlling the spread of disease are Bubbles. Each person chooses a bubble of other people to associate with and avoids contact with others. Infection in one bubble should not spread to people in other bubbles.</p>

<p>The concept fails, however, when a person belongs to multiple bubbles. For example, a person might have a personal bubble of family and friends and a work bubble of colleagues. In this problem, we will make the following simplifying assumptions:</p>

<ul>
	<li>Each personal bubble contains the same number of people, P.</li>
	<li>Each work bubble contains the same number of people, W.</li>
	<li>Each person is in exactly one personal bubble and one work bubble.</li>
	<li>Each pair of personal bubble and work bubble has exactly one person in common.</li>
</ul>

<p>Given a list of the bubbles that have been infected, determine how many people have been infected.</p>

### 입력 

 <p>First line: three integers P, W, N, the number of people in each personal and work bubble and the number of infected bubbles. These numbers satisfy the constraints 1 ≤ P, W ≤ 200, 000 and 0 ≤ N ≤ min(P + W, 10 000). Next N lines: the letter <code>P</code> or <code>W</code>, a space, and an integer B, indicating that personal or work bubble number B is infected. When the letter is <code>P</code>, B satisfies the constraint 0 ≤ B < W. When the letter is <code>W</code>, B satisfies the constraint 0 ≤ B < P. Each infected bubble is listed only once.</p>

### 출력 

 <p>A single integer I, the total number of people infected.</p>

