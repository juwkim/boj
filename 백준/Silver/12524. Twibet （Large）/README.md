# [Silver III] Twibet (Large) - 12524 

[문제 링크](https://www.acmicpc.net/problem/12524) 

### 성능 요약

메모리: 115024 KB, 시간: 216 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 6월 7일 12:09:40

### 문제 설명

<p>The holy country of Twibet has <strong>N</strong> monks. Each monk has a unique number, from 1 to <strong>N</strong>. They do not use names for religious reasons. The monks are constantly on the move, slowly walking around Twibet. Each monk follows exactly one other monk.</p>

<p>Most of the time, every monk is silent, but on day K, monk number K stops, turns around and whispers the 140 Words of Wisdom. The whisper is quiet, so only the monk's immediate followers can hear it. At that point, each of his followers stops, turns around and whispers the same words to each of his own followers. This chain continues -- each follower who has just heard the Words, but has not yet whispered the Words today, stops and whispers to his followers.</p>

<p>After all of the monks who could have heard the words have whispered them, they all turn back around and continue walking as usual... until the next day, when this all starts again, but this time starting with a different monk.</p>

<p>How many monks will whisper the 140 Words of Wisdom on day K, for each K between 1 and <strong>N</strong>?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> test cases follow. Each one starts with a line containing a single integer <strong>N</strong>. The next line contains <strong>N</strong> space-separated integers <strong>F<sub>1</sub></strong>, <strong>F<sub>2</sub></strong>, ..., <strong>F<sub>N</sub></strong>. Monk 1 follows monk <strong>F<sub>1</sub></strong>. Monk 2 follows monk <strong>F<sub>2</sub></strong>, etc.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>No monk will immediately follow himself (<strong>F<sub>k</sub></strong> is never equal to <strong>k</strong>).</li>
	<li>2 ≤ <strong>N</strong> ≤ 1000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x:", where x is the case number (starting from 1). Then output <strong>N</strong> lines, one for each day. The first line should contain the number of monks who will whisper the Words on day 1. The next line -- on day 2, etc.</p>

