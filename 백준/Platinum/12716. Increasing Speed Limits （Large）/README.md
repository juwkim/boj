# [Platinum V] Increasing Speed Limits (Large) - 12716 

[문제 링크](https://www.acmicpc.net/problem/12716) 

### 성능 요약

메모리: 283280 KB, 시간: 4816 ms

### 분류

값 / 좌표 압축, 자료 구조, 다이나믹 프로그래밍, 세그먼트 트리

### 제출 일자

2024년 2월 15일 08:15:44

### 문제 설명

<p>You were driving along a highway when you got caught by the road police for speeding. It turns out that they've been following you, and they were amazed by the fact that you were accelerating the whole time without using the brakes! And now you desperately need an excuse to explain that.</p>

<p>You've decided that it would be reasonable to say "all the speed limit signs I saw were in increasing order, that's why I've been accelerating". The police officer laughs in reply, and tells you all the signs that are placed along the segment of highway you drove, and says that's unlikely that you were so lucky just to see some part of these signs that were in increasing order.</p>

<p>Now you need to estimate that likelihood, or, in other words, find out how many different subsequences of the given sequence are strictly increasing. The empty subsequence does not count since that would imply you didn't look at any speed limits signs at all!</p>

<p>For example, (1, 2, 5) is an increasing subsequence of (1, 4, 2, 3, 5, 5), and we count it twice because there are two ways to select (1, 2, 5) from the list.</p>

### 입력 

 <p>The first line of input gives the number of cases, <strong>N</strong>. <strong>N</strong> test cases follow. The first line of each case contains <strong>n</strong>, <strong>m</strong>, <strong>X</strong>, <strong>Y</strong> and <strong>Z</strong> each separated by a space.  <strong>n</strong> will be the length of the sequence of speed limits. <strong>m</strong> will be the length of the generating array A. The next <strong>m</strong>lines will contain the <strong>m</strong> elements of A, one integer per line (from A[0] to A[<strong>m</strong>-1]).</p>

<p>Using A, <strong>X</strong>, <strong>Y</strong> and <strong>Z</strong>, the following pseudocode will <em>print</em> the speed limit sequence in order. mod indicates the remainder operation.</p>

<pre><code>for i = 0 to n-1
  <em>print</em> A[i mod <strong>m</strong>]
  A[i mod <strong>m</strong>] = (<strong>X</strong> * A[i mod <strong>m</strong>] + <strong>Y</strong> * (i + 1)) mod <strong>Z</strong>
</code></pre>

<p> </p>

<p>Note: The way that the input is generated has nothing to do with the intended solution and exists solely to keep the size of the input files low.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>N</strong> ≤ 20</li>
	<li>1 ≤ <strong>m</strong> ≤ 100</li>
	<li>0 ≤ <strong>X</strong> ≤ 10<sup>9</sup></li>
	<li>0 ≤ <strong>Y</strong> ≤ 10<sup>9</sup></li>
	<li>1 ≤ <strong>Z</strong> ≤ 10<sup>9</sup></li>
	<li>0 ≤ <strong>A[i]</strong> < <strong>Z</strong></li>
	<li>1 ≤ <strong>m</strong> ≤ <strong>n</strong> ≤ 500 000</li>
</ul>

### 출력 

 <p>For each test case you should output one line containing "Case #<strong>T</strong>: <strong>S</strong>" (quotes for clarity) where <strong>T</strong> is the number of the test case and <strong>S</strong> is the number of non-empty increasing subsequences mod 1<sub> </sub>000<sub> </sub>000<sub> </sub>007.</p>

