# [Bronze II] Angry Grammar Nazi - 11158 

[문제 링크](https://www.acmicpc.net/problem/11158) 

### 성능 요약

메모리: 30860 KB, 시간: 72 ms

### 분류

문자열(string)

### 문제 설명

<p>Your friend is what we can call a grammar nazi. He spends a lot of time on popular internet discussion forums. Unfortunately, he has a bad temper and loses his mind whenever someone incorrigibly befouls the English language, with unrelenting violations of grammatical and ortographic rules.</p>

<p>In order to avoid smashed keyboards, monitors and coffee-cup holders, you advice your friend to momentarily stop reading and count to ten each time he becomes angry, instead of smashing something.</p>

<p>Your friend becomes angry whenever he reads the following words or sequences of words:</p>

<ul>
	<li>“u”, “ur” instead of “you”, “your”.</li>
	<li>“would of”, “should of” instead of “would have”, “should have”.</li>
	<li>“lol” instead of “haha”. In fact he becomes angry even when a word contains “lol” as a substring.</li>
</ul>

<p>You decide to write a computer program that reads sentences one by one, and for each sentence calculates how many times your friend will have uttered a number after reading said sentence. Your friend does not read out loud, so numbers that are part of the input-sentences should not be counted.</p>

### 입력 

 <p>The first line of the input consists of a single integer T, the number of test cases. The following T lines each contain one sentence; that is, one or more words separated by space.</p>

<ul>
	<li>0 < T ≤ 50</li>
	<li>A sentence consists of at most 100 characters, including spaces.</li>
	<li>A word consists only of lower case letters between a and z, inclusively.</li>
	<li>Two adjacent words are separated by exactly one space, and a sentence never has leading or trailing spaces.</li>
</ul>

### 출력 

 <p>For each test case, output how many times your friend have said a number after reading the sentence.</p>

