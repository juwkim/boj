# [Gold V] Safety in Numbers (Large) - 12389 

[문제 링크](https://www.acmicpc.net/problem/12389) 

### 성능 요약

메모리: 113220 KB, 시간: 1116 ms

### 분류

이분 탐색, 매개 변수 탐색

### 제출 일자

2025년 5월 26일 00:07:22

### 문제 설명

<p>There are <strong>N</strong> contestants in a reality TV show. Each contestant is assigned a point value by the judges and receives votes from the audience. The point value given by the judges and the audience's votes are combined to form a <em>final score</em> for the contestant, in the following way:</p>

<p>Let <code>X</code> be the sum of the judge-assigned point values of all contestants. Now suppose a contestant got <code>J</code> points from the judges, and that she received a fraction <code>Y</code> (between 0 and 1, inclusive) of the audience's votes (<code>Y</code> might be, for example, 0.3). Then that contestant's final score is <code>J+X*Y</code>. Note that the sum of all contestants' audience vote fractions must be 1.</p>

<p>The contestant with the lowest score is eliminated. </p>

<p>Given the points contestants got from judges, your job is to find out, for each contestant, the minimum percentage of audience votes he/she must receive in order for him/her to be guaranteed <strong>not to be eliminated</strong>, no matter how the rest of the audience's votes are distributed.</p>

<p>If the lowest score is shared by multiple contestants, no contestants will be eliminated.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> test cases follow, one per line. Each line starts with an integer <strong>N</strong>, the number of contestants, followed by a space, followed by <strong>N</strong> integers <strong>s</strong><sub>0</sub>, <strong>s</strong><sub>1</sub>, ..., <strong>s</strong><sub>N-1</sub>, separated by single spaces. The integer <strong>s</strong><sub>i</sub> is the point value assigned to contestant <code>i</code> by the judges.</p>

<h3>Limits</h3>

<ul>
	<li>0 ≤ <strong>s</strong><sub>i</sub> ≤ 100.</li>
	<li><strong>s</strong><sub>i</sub> > 0 for some i. This means at least one contestant will have a point value greater than 0.</li>
	<li>1 ≤ <strong>T</strong> ≤ 50.</li>
	<li>2 ≤ <strong>N</strong> ≤ 200.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: " followed by <strong>N</strong> real numbers: <strong>m</strong><sub>i</sub>s. The value x is the case number (starting from 1). The value <strong>m</strong><sub>i</sub> is the smallest percentage of audience votes required for contestant <code>i</code> to definitely avoid elimination.</p>

<p>Answers within an absolute or relative error of 10<sup>-5</sup> of the correct answer will be accepted.</p>

