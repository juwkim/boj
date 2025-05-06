# [Gold III] Parenting Partnering (Large) - 14812 

[문제 링크](https://www.acmicpc.net/problem/14812) 

### 성능 요약

메모리: 214616 KB, 시간: 2448 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 5월 6일 18:19:00

### 문제 설명

<p>Cameron and Jamie are longtime life partners and have recently become parents! Being in charge of a baby, exciting as it is, is not without challenges. Given that both parents have a scientific mind, they have decided to take a scientific approach to baby care.</p>

<p>Cameron and Jamie are establishing a daily routine and need to decide who will be the main person in charge of the baby at each given time. They have been equal partners their whole relationship, and they do not want to stop now, so they decided that each of them will be in charge for exactly 12 hours (720 minutes) per day.</p>

<p>Cameron and Jamie have other activities that they either need or want to do on their own. Cameron has <strong>A<sub>C</sub></strong> of these and Jamie has <strong>A<sub>J</sub></strong>. These activities always take place at the same times each day. None of Cameron's activities overlap with Jamie's activities, so at least one of the parents will always be free to take care of the baby.</p>

<p>Cameron and Jamie want to come up with a daily baby care schedule such that:</p>

<ul>
	<li>Scheduled baby time must not interfere with a scheduled activity. That is, during Cameron's activities, Jamie has to be in charge of the baby, and vice versa.</li>
	<li>Each of Cameron and Jamie must have exactly 720 minutes assigned to them.</li>
	<li>The number of exchanges — that is, the number of times the person in charge of the baby changes from one partner to the other — must be as small as possible.</li>
</ul>

<p>For example, suppose that Jamie and Cameron have a single activity each: Jamie has a morning activity from 9 am to 10 am, and Cameron has an afternoon activity from 2 pm to 3 pm. One possible but suboptimal schedule would be for Jamie to take care of the baby from midnight to 6 am and from noon to 6 pm, and for Cameron to take care of the baby from 6 am to noon and 6 pm to midnight. That fulfills the first two conditions, and requires a total of 4 exchanges, which happen at midnight, 6 am, noon and 6 pm. If there is an exchange happening at midnight, it is counted exactly once, not zero or two times.</p>

<p>A better option would be for Cameron to take care of the baby from midnight to noon, and Jamie to take care of the baby from noon to midnight. This schedule also fulfills the first two conditions, but it uses only 2 exchanges, which is the minimum possible.</p>

<p>Given Cameron's and Jamie's lists of activities, and the restrictions above, what is the minimum possible number of exchanges in a daily schedule?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case starts with a line containing two integers <strong>A<sub>C</sub></strong> and <strong>A<sub>J</sub></strong>, the number of activities that Cameron and Jamie have, respectively. Then, <strong>A<sub>C</sub></strong> + <strong>A<sub>J</sub></strong> lines follow. The first <strong>A<sub>C</sub></strong> of these lines contain two integers <strong>C<sub>i</sub></strong> and <strong>D<sub>i</sub></strong> each. The i-th of Cameron's activities starts exactly <strong>C<sub>i</sub></strong>minutes after the start of the day at midnight and ends exactly <strong>D<sub>i</sub></strong> minutes after the start of the day at midnight (taking exactly <strong>D<sub>i</sub></strong> - <strong>C<sub>i</sub></strong> minutes). The last <strong>A<sub>J</sub></strong> of these lines contain two integers <strong>J<sub>i</sub></strong> and <strong>K<sub>i</sub></strong> each, representing the starting and ending time of one of Jamie's activities, in minutes counting from the start of the day at midnight (same format as Cameron's). No activity spans two days, and no two activities overlap (except that one might end exactly as another starts, but an exchange can still occur at that time).</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>0 ≤ <strong>C<sub>i</sub></strong> < <strong>D<sub>i</sub></strong> ≤ 24 × 60, for all i.</li>
	<li>0 ≤ <strong>J<sub>i</sub></strong> < <strong>K<sub>i</sub></strong> ≤ 24 × 60, for all i.</li>
	<li>Any two of the intervals of {[<strong>C<sub>i</sub></strong>, <strong>D<sub>i</sub></strong>) for all i} union {[<strong>J<sub>i</sub></strong>, <strong>K<sub>i</sub></strong>) for all i} have an empty intersection. (The intervals are closed on the left and open on the right, which ensures that two exactly consecutive intervals have nothing in between but do not overlap.)</li>
	<li>sum of {<strong>D<sub>i</sub></strong> - <strong>C<sub>i</sub></strong> for all i} ≤ 720.</li>
	<li>sum of {<strong>K<sub>i</sub></strong> - <strong>J<sub>i</sub></strong> for all i} ≤ 720.</li>
	<li>0 ≤ <strong>A<sub>C</sub></strong> ≤ 100.</li>
	<li>0 ≤ <strong>A<sub>J</sub></strong> ≤ 100.</li>
	<li>1 ≤ <strong>A<sub>C</sub></strong> + <strong>A<sub>J</sub></strong> ≤ 200.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> the minimum possible number of exchanges, as described in the statement.</p>

