# [Gold IV] The Repeater (Large) - 12249 

[문제 링크](https://www.acmicpc.net/problem/12249) 

### 성능 요약

메모리: 112396 KB, 시간: 220 ms

### 분류

수학

### 제출 일자

2023년 10월 11일 14:56:14

### 문제 설명

<p>Fegla and Omar like to play games every day. But now they are bored of all games, and they would like to play a new game. So they decided to invent their own game called "The Repeater".</p>

<p>They invented a 2 player game. Fegla writes down <strong>N</strong> strings. Omar's task is to make all the strings identical, if possible, using the minimum number of actions (possibly 0 actions) of the following two types:</p>

<ul>
	<li>Select any character in any of the strings and repeat it (add another instance of this character exactly after it). For example, in a single move Omar can change "abc" to "abbc" (by repeating the character 'b').</li>
	<li>Select any two adjacent and identical characters in any of the strings, and delete one of them. For example, in a single move Omar can change "abbc" to "abc" (delete one of the 'b' characters), but can't convert it to "bbc".</li>
</ul>

<p>The 2 actions are independent; it's not necessary that an action of the first type should be followed by an action of the second type (or vice versa).</p>

<p>Help Omar to win this game by writing a program to find if it is possible to make the given strings identical, and to find the minimum number of moves if it is possible.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case starts with a line containing an integer <strong>N</strong> which is the number of strings. Followed by <strong>N</strong> lines, each line contains a non-empty string (each string will consist of lower case English characters only, from 'a' to 'z').</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ length of each string ≤ 100.</li>
	<li><span style="line-height:1.6em">2 ≤ </span><strong style="line-height:1.6em">N</strong><span style="line-height:1.6em"> ≤ 100.</span></li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of moves to make the strings identical. If there is no possible way to make all strings identical, print "Fegla Won" (quotes for clarity).</p>

