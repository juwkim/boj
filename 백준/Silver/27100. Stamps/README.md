# [Silver V] Stamps - 27100 

[문제 링크](https://www.acmicpc.net/problem/27100) 

### 성능 요약

메모리: 115916 KB, 시간: 3356 ms

### 분류

너비 우선 탐색(bfs), 다이나믹 프로그래밍(dp), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>You are supplied a set of values for stamps (e.g., {1, 3, 5}) and the maximum number of stamps that can be applied to an envelope (e.g., five stamps). Your goal is to calculate the largest contiguous set of postage that can be accommodated.  For the set of {1, 3, 5} with five maximum stamps, one can build:</p>

<ul>
	<li>1: 1</li>
	<li>2: 1+1</li>
	<li>3: 3</li>
	<li>4: 1+3</li>
	<li>5: 5</li>
	<li>6: 1+5</li>
	<li>7: 5+1+1</li>
	<li>8: 5+3</li>
	<li>9: 5+3+1</li>
	<li>10: 5+5</li>
	<li>11: 5+5+1</li>
	<li>12: 5+5+1+1</li>
	<li>13: 5+5+3</li>
	<li>14: 5+5+3+1</li>
	<li>15: 5+5+5</li>
	<li>16: 5+5+3+3</li>
	<li>17: 5+5+5+1+1</li>
	<li>18: 5+5+5+3</li>
	<li>19: 5+5+5+3+1</li>
	<li>20: 5+5+5+5</li>
	<li>21: 5+5+5+3+3</li>
	<li>22: ????</li>
</ul>

<p>There appears to be no way to build 22 cents with no more than five members of this set of stamps.  Thus, one can build values in the ragen [1..21,] a total of 21 contiguous stamp values.  There is no reason to believe that the largest contiguous set will start with the value '1'.</p>

### 입력 

 <ul>
	<li>Line 1: Two space separated integers, S (1 ≤ S ≤ 20), the number of stamp types, and E (1 ≤ E ≤ 10), the maximum number of stamps that can fit on an envelope.</li>
	<li>Line 2: S different space-separated positive integers representing the values of the stamps (1 ≤ stampval ≤ 1000)</li>
</ul>

### 출력 

 <p>The maximum number of contiguous values that can be created by combining the stamps.</p>

