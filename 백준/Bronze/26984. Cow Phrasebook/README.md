# [Bronze I] Cow Phrasebook - 26984 

[문제 링크](https://www.acmicpc.net/problem/26984) 

### 성능 요약

메모리: 116336 KB, 시간: 580 ms

### 분류

브루트포스 알고리즘(bruteforcing), 문자열(string)

### 문제 설명

<p>Ever the innovator, Farmer John is teaching cows to speak some phrases in human language. He writes each new phrase the cows learn in his phrase book, a total of M (1 ≤ M ≤ 1,000) so far.</p>

<p>When Farmer John is on a vacation, he can only communicate with his cows by telephone. Being an active vacationer, FJ visits beaches and fine restaurants when away from the farm. When he returns, his answering machine is full of N (1 ≤ N ≤ 10,000) messages, many potentially from the cows.</p>

<p>FJ vacations frugally and thus gets poor telephone service. Many of the recorded messages cut off before they are complete. Help FJ determine whether the recorded messages are from the phrasebook by determining if the message begins a phrase.</p>

<p>You will be given the phrasebook and a set of texts of the recorded messages. Count the number of recorded messages that are the beginning (prefix) of a phrase from the phrase book.</p>

<p>Complete phrases are from 1 to 60 characters in length, each of which is either a letter (upper or lower case), a period (.), comma (,), question mark (?) or space. There are no leading spaces, trailing spaces, or double spaces in a phrase. Comparisons are case-sensitive, and a phrase is in fact, considered to be prefix of itself.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers, M and N</li>
	<li>Lines 2..M+1: Phrases from the phrase book, one per line.</li>
	<li>Lines M+2..M+N+1: Phrases spoken by cows, one per line.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the count of the number of messages that were proper prefixes of the phrasebook.</li>
</ul>

