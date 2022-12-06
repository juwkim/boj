# [Gold I] Bathroom Stalls (Large) - 14794 

[문제 링크](https://www.acmicpc.net/problem/14794) 

### 성능 요약

메모리: 28776 KB, 시간: 84 ms

### 분류

자료 구조(data_structures), 다이나믹 프로그래밍(dp), 수학(math), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>A certain bathroom has <strong>N</strong> + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other <strong>N</strong> stalls are for users.</p>

<p>Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values L<sub>S</sub> and R<sub>S</sub>, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(L<sub>S</sub>, R<sub>S</sub>) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(L<sub>S</sub>, R<sub>S</sub>) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.</p>

<p><strong>K</strong> people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.</p>

<p>When the last person chooses their stall S, what will the values of max(L<sub>S</sub>, R<sub>S</sub>) and min(L<sub>S</sub>, R<sub>S</sub>) be?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> lines follow. Each line describes a test case with two integers <strong>N</strong> and <strong>K</strong>, as described above.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>K</strong> ≤ <strong>N</strong>.</li>
	<li>1 ≤ <strong>N</strong> ≤ 10<sup>18</sup>.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y z</code>, where <code>x</code> is the test case number (starting from 1), <code>y</code> is max(L<sub>S</sub>, R<sub>S</sub>), and <code>z</code> is min(L<sub>S</sub>, R<sub>S</sub>) as calculated by the last person to enter the bathroom for their chosen stall S.</p>

