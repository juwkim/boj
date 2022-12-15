# [Silver IV] The Last Word (Small) - 14375 

[문제 링크](https://www.acmicpc.net/problem/14375) 

### 성능 요약

메모리: 114964 KB, 시간: 148 ms

### 분류

브루트포스 알고리즘(bruteforcing), 그리디 알고리즘(greedy), 문자열(string)

### 문제 설명

<p>On the game show The Last Word, the host begins a round by showing the contestant a string S of uppercase English letters. The contestant has a whiteboard which is initially blank. The host will then present the contestant with the letters of S, one by one, in the order in which they appear in S. When the host presents the first letter, the contestant writes it on the whiteboard; this counts as the first word in the game (even though it is only one letter long). After that, each time the host presents a letter, the contestant must write it at the beginning or the end of the word on the whiteboard before the host moves on to the next letter (or to the end of the game, if there are no more letters).</p>

<p>For example, for S = <code>CAB</code>, after writing the word <code>C</code> on the whiteboard, the contestant could make one of the following four sets of choices:</p>

<ul>
	<li>put the <code>A</code> before <code>C</code> to form <code>AC</code>, then put the <code>B</code> before <code>AC</code> to form <code>BAC</code></li>
	<li>put the <code>A</code> before <code>C</code> to form <code>AC</code>, then put the <code>B</code> after <code>AC</code> to form <code>ACB</code></li>
	<li>put the <code>A</code> after <code>C</code> to form <code>CA</code>, then put the <code>B</code> before <code>CA</code> to form <code>BCA</code></li>
	<li>put the <code>A</code> after <code>C</code> to form <code>CA</code>, then put the <code>B</code> after <code>CA</code> to form <code>CAB</code></li>
</ul>

<p>The word is called the last word when the contestant finishes writing all of the letters from S, under the given rules. The contestant wins the game if their last word is the last of an alphabetically sorted list of all of the possible last words that could have been produced. For the example above, the winning last word is <code>CAB</code> (which happens to be the same as the original word). For a game with S = <code>JAM</code>, the winning last word is <code>MJA</code>.</p>

<p>You are the next contestant on this show, and the host has just showed you the string S. What's the winning last word that you should produce?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ T ≤ 100.</li>
	<li>1 ≤ length of S ≤ 15.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the winning last word, as described in the statement.</p>

