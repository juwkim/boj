# [Silver IV] New Time - 26876 

[문제 링크](https://www.acmicpc.net/problem/26876) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

너비 우선 탐색(bfs), 다이나믹 프로그래밍(dp), 그래프 이론(graphs), 그래프 탐색(graph_traversal), 그리디 알고리즘(greedy)

### 문제 설명

<p>Nikolay has a digital clock that displays time in 24-hour format, showing two integers: hours (from $00$ to $23$) and minutes (from $00$ to $59$). For example, the clock can show <code>00:00</code>, <code>18:42</code>, or <code>23:59</code>.</p>

<p>The clock has two buttons that can be used for manual adjustment:</p>

<ul>
	<li>Button A sets the clock forward by $1$ minute. For example, <code>05:33</code> becomes <code>05:34</code>, <code>16:59</code> becomes <code>17:00</code>, and <code>23:59</code> becomes <code>00:00</code>.</li>
	<li>Button B sets the clock forward by $1$ hour. For example, <code>01:42</code> becomes <code>02:42</code>, and <code>23:14</code> becomes <code>00:14</code>.</li>
</ul>

<p>Nikolay has noticed that the time on his clock does not look right. He wants to adjust the clock to the correct time by pressing the buttons as few times as possible.</p>

<p>Find the smallest number of button presses needed to adjust the clock.</p>

### 입력 

 <p>The first line contains the time shown on the clock in the <code>hh:mm</code> format ($00 \le \mathtt{hh} \le 23$; $00 \le \mathtt{mm} \le 59$).</p>

<p>The second line contains the correct time in the same format.</p>

### 출력 

 <p>Print a single integer --- the smallest number of button presses Nikolay needs to adjust the time on his clock.</p>

