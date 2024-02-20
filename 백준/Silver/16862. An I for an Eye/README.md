# [Silver III] An I for an Eye - 16862 

[문제 링크](https://www.acmicpc.net/problem/16862) 

### 성능 요약

메모리: 110736 KB, 시간: 124 ms

### 분류

구현

### 제출 일자

2024년 2월 21일 03:02:15

### 문제 설명

<p>Ken has been having trouble lately staying under the word limit in Twitter, so he’s decided to write a little front-end program which will take in text and shorten it using a fixed set of abbreviations for commonly used letter sequences. Those abbreviations are shown in the table below:</p>

<table class="table table-bordered" style="width: 30%;">
	<thead>
		<tr>
			<th>The character ...</th>
			<th>... substitutes for the letter sequence</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>@</code></td>
			<td>at</td>
		</tr>
		<tr>
			<td><code>&</code></td>
			<td>and</td>
		</tr>
		<tr>
			<td><code>1</code></td>
			<td>one, won</td>
		</tr>
		<tr>
			<td><code>2</code></td>
			<td>to, too, two</td>
		</tr>
		<tr>
			<td><code>4</code></td>
			<td>for, four</td>
		</tr>
		<tr>
			<td><code>b</code></td>
			<td>bea, be, bee</td>
		</tr>
		<tr>
			<td><code>c</code></td>
			<td>sea, see</td>
		</tr>
		<tr>
			<td><code>i</code></td>
			<td>eye</td>
		</tr>
		<tr>
			<td><code>o</code></td>
			<td>oh, owe</td>
		</tr>
		<tr>
			<td><code>r</code></td>
			<td>are</td>
		</tr>
		<tr>
			<td><code>u</code></td>
			<td>you</td>
		</tr>
		<tr>
			<td><code>y</code></td>
			<td>why</td>
		</tr>
	</tbody>
</table>

<p>Ken is about to start writing this program when he realizes that the extent of his computer knowledge is ... well ... using Twitter. He’s looking for someone to help him – <code>r u th@ some1</code>?</p>

### 입력 

 <p>Input starts with a single integer n indicating the number of lines of text to process. Following this are n lines of text. Each line will contain only alphanumeric characters and spaces, and each line will have at least one non-space character. Each line has at most 200 characters.</p>

### 출력 

 <p>Display each line with the appropriate substitutions made. Substitutions should also be made inside words, e.g., the word <code>that</code> should be changed to <code>th@</code>. If two letter sequences overlap (like <code>at</code> and <code>to</code> in the word <code>baton</code>) just replace the first one (in this case resulting in <code>b@on</code>). If two letter sequences start at the same location (like <code>be</code> and <code>bee</code> in <code>been</code>) replace the longer one (in this case resulting in <code>bn</code>). If the letter sequence starts with an upper-case letter, then the abbreviation should also be in upper-case (if appropriate). Finally, no substituted letter should later be part of another substitution. For example, if the input is <code>oweh</code>, you would first replace the <code>owe</code> with an <code>o</code> to get <code>oh</code>. At this point you do NOT replace the <code>oh</code> with an <code>o</code> since the <code>oh</code> contains a substituted letter.</p>

