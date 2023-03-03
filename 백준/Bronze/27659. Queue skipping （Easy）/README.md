# [Bronze II] Queue skipping (Easy) - 27659 

[문제 링크](https://www.acmicpc.net/problem/27659) 

### 성능 요약

메모리: 115100 KB, 시간: 168 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Recently there was a rumor that on Monday the meat store will actually have some meat. It’s Monday, half past one in the morning. The entire town is already waiting for the store to open. More precisely, there are <em>n</em> people waiting in a line. The people are numbered 1 through <em>n</em> in line order, with person 1 being the one currently closest to the door of the store.</p>

<p>During the next few hours, at some moments one of the people will use some trick in order to skip to the beginning of the queue. Examples of such tricks include:</p>

<ul>
	<li>Look over there, isn’t that <em>[famous TV show host]</em>?</li>
	<li>Please let me through, I’m with a small child!</li>
	<li>I stood here before, I just went to the bathroom.</li>
	<li>Hey, look at that guy trying to skip the queue, I’ll go and throw him out!</li>
</ul>

<p>You are given the sequence of people skipping to the front of the queue. After all those events, the meat store will open. People will enter the store one at a time. Inside, they will learn that the meat didn’t arrive (again!), so they will go home empty-handed.</p>

<p>Find out who will waste the most time waiting for nothing. In other words, find out who will be the last person in the queue after all the skipping to the front is over.</p>

### 입력 

 <p>The first line of the input file contains an integer <em>t</em> specifying the number of test cases. Each test case is preceded by a blank line.</p>

<p>Each test case starts with a line containing two positive integers <em>n</em> and <em>e</em>: the number of people and the number of events. The rest of the test case consists of <em>e</em> lines, each containing a single positive integer: the number of a person who just moved to the front of the queue.</p>

<p>You may assume that <em>t</em> = 100 and 1 ≤ <em>n</em>, <em>e</em> ≤ 100.</p>

### 출력 

 <p>For each test case output a single line with a single positive integer: the number of the last person in the queue when the meat store opened.</p>

