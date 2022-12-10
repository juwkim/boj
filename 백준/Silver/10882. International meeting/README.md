# [Silver IV] International meeting - 10882 

[문제 링크](https://www.acmicpc.net/problem/10882) 

### 성능 요약

메모리: 113248 KB, 시간: 120 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Zoyi Corporation, an international company, has several branches all over the world. YJ, as a project leader in the company, needs to cooperate with lots of people overseas. However, he is notoriously unkind, not careful enough to let co-workers to know the meeting time in their own local time. Surprised at his lack of consideration, his secretary MH rewrote the mail to present the meeting time as each recipient’ s time zone. MH was capable to have written down every co-workers’ time zone in Coordinated Universal Time, or UTC, which is the basis for the world’ s civil time. Time zones can be defined as the difference from UTC by an integer number of hours D (−12 ≤ D ≤ 12) like below.</p>

<ul>
	<li>Korea: UTC+9,</li>
	<li>New Jersey: UTC-5</li>
</ul>

<p>However, Zoyi Corp. also has a branch in Pyongyang, who recently changed their time zone to UTC+8.5. Consequently, not only an integer part but also an additional fractional part (plus 0.5) might appear in the MH’ s note, for example, UTC-3.5.</p>

<p>Given the meeting time in YJ’ s time zone and the time zone of every co-workers including YJ, calculate the meeting time for each co-worker.</p>

### 입력 

 <p>The first line of the input contains an integer N (1 ≤ N ≤ 50) — the number of co-workers. The next line contains the meeting time in YJ’ s time zone in UTC notation, HH : MM UTC+D (−12 ≤ D ≤ 12). The time and the text UTC are separated by a single whitespace.</p>

<p>Each of the next N line contains the time zone for a co-worker. Times are represented as HH : MM, in the standard 24-hour clock convention which makes noon as 12:00, and 12 midnight as 00:00. The last minute of the day is 23:59, and you may not write 12 midnight as 24:00.</p>

### 출력 

 <p>Print exactly N lines — each line should contain the converted time in each co-worker’s time zone.</p>

