# [Silver IV] gGames (Small) - 12062 

[문제 링크](https://www.acmicpc.net/problem/12062) 

### 성능 요약

메모리: 110404 KB, 시간: 132 ms

### 분류

브루트포스 알고리즘, 구현, 시뮬레이션

### 제출 일자

2023년 12월 27일 01:38:11

### 문제 설명

<p>The country of elves is planning to hold an elimination tournament, and there are 2<sup><strong>N</strong></sup> elves who would like to take part. At the start of the tournament, they will be given unique ID numbers from 1 to 2<sup><strong>N</strong></sup>, and the Elf President will line them up in some order.</p>

<p>The tournament is a series of matches between two elves, and every match has one winner and one loser (there are no ties). In the first round, the first elf in the line competes against the second elf in the line, the third elf competes against the fourth elf, and so on. After the first round, the 2<sup><strong>N-1</strong></sup> elves who lost leave the line, and the 2<sup><strong>N-1</strong></sup> elves who won remain where they are. Then, the remaining elves play the second round in the same way: the first remaining elf in the line competes against the second remaining elf in the line, the third remaining elf competes against the fourth remaining elf, and so on. After <strong>N</strong> rounds, there will be only one elf remaining, and that elf is the winner.</p>

<p><strong>M</strong> of the elves are sensitive, which means that they will be very sad if they have to compete in matches against their friends during the games. Specifically, the ith elf will be sad if they have to compete with their friends in the first <strong>K<sub>i</sub></strong> rounds. (Note that friendship is not necessarily mutual: if one elf considers another elf to be a friend, the other elf does not necessarily consider that elf to be a friend.) </p>

<p>The Elf President wants to know: is there a way to specify the initial positions of all 2<sup><strong>N</strong></sup>elves to guarantee that no elf will be sad, no matter what happens in the tournament?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case consists of one line with two integers <strong>N</strong> and <strong>M</strong>, then <strong>M</strong> sets of two lines each, in which the first line has integers <strong>E<sub>i</sub></strong>, <strong>K<sub>i</sub></strong>, and <strong>B<sub>i</sub></strong> for one elf, and the second has <strong>B<sub>i</sub></strong> integer ID numbers of that elf's friends.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 200.</li>
	<li>0 ≤ <strong>M</strong> ≤ 2<sup><strong>N</strong></sup>.</li>
	<li>1 ≤ <strong>E<sub>i</sub></strong> ≤ 2<sup><strong>N</strong></sup>.</li>
	<li>1 ≤ <strong>K<sub>i</sub></strong> ≤ <strong>N</strong>.</li>
	<li><strong>M</strong> ≤ sum(<strong>B<sub>i</sub></strong>) ≤ min(2 * <strong>M</strong>, 2<sup><strong>N</strong></sup>).</li>
	<li>1 ≤ <strong>N</strong> ≤ 3.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: ", where x is the case number (starting from 1), followed by <code>YES</code> or <code>NO</code>.</p>

