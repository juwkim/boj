# [Bronze I] Moo Operations - 27563 

[문제 링크](https://www.acmicpc.net/problem/27563) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

그리디 알고리즘(greedy), 문자열(string)

### 문제 설명

<p>Because Bessie is bored of playing with her usual text string where the only characters are 'C,' 'O,' and 'W,' Farmer John gave her $Q$ new strings ($1 \leq Q \leq 100$), where the only characters are 'M' and 'O.' Bessie's favorite word out of the characters 'M' and 'O' is obviously "MOO," so she wants to turn each of the $Q$ strings into "MOO" using the following operations:</p>

<ol>
	<li>Replace either the first or last character with its opposite (so that 'M' becomes 'O' and 'O' becomes 'M').</li>
	<li>Delete either the first or last character.</li>
</ol>

<p>Unfortunately, Bessie is lazy and does not want to perform more operations than absolutely necessary. For each string, please help her determine the minimum number of operations necessary to form "MOO" or output $-1$ if this is impossible.</p>

### 입력 

 <p>The first line of input contains the value of $Q$.</p>

<p>The next $Q$ lines of input each consist of a string, each of its characters either 'M' or 'O'. Each string has at least 1 and at most 100 characters.</p>

### 출력 

 <p>Output the answer for each input string on a separate line.</p>

