# [Silver IV] Automatic Poetry - 7564 

[문제 링크](https://www.acmicpc.net/problem/7564) 

### 성능 요약

메모리: 112896 KB, 시간: 184 ms

### 분류

구현, 시뮬레이션, 문자열

### 제출 일자

2023년 10월 26일 01:33:59

### 문제 설명

<p>“Oh God”, Lara Croft exclaims, “it’s one of these dumb riddles again!”</p>

<p>In Tomb Raider XIV, Lara is, as ever, gunning her way through ancient Egyptian pyramids, prehistoric caves and medival hallways. Now she is standing in front of some important Germanic looking doorway and has to solve a linguistic riddle to pass. As usual, the riddle is not very intellectually challenging.</p>

<p>This time, the riddle involves poems containing a “Schüttelreim”. An example of a Schüttelreim is the following short poem:</p>

<pre>Ein Kind hält seinen Schnabel nur,
wenn es hängt an der Nabelschnur.</pre>

<p>A Schüttelreim seems to be a typical German invention. The funny thing about this strange type of poetry is that if somebody gives you the first line and the beginning of the second one, you can complete the poem yourself. Well, even a computer can do that, and your task is to write a program which completes them automatically. This will help Lara concentrate on the “action” part of Tomb Raider and not on the “intellectual” part.</p>

### 입력 

 <p>The input will begin with a line containing a single number n. After this line follow n pairs of lines containing Schüttelreims. The first line of each pair will be of the form</p>

<pre>s1<s2>s3<s4>s5</pre>

<p>where the si are possibly empty strings of lowercase characters or blanks. The second line will be a string of lowercase characters or blanks ending with three dots “...”. Lines will we at most 100 characters long.</p>

### 출력 

 <p>For each pair of Schüttelreim lines l1 and l2 you are to output two lines c1 and c2 in the following way: c1 is the same as l1 only that the bracket marks “<” and “>” are removed. Line c2 is the same as l2, except that instead of the three dots the string</p>

<pre>s4s3s2s5</pre>

<p>should appear.</p>

