# [Bronze II] Beautiful Music - 15181 

[문제 링크](https://www.acmicpc.net/problem/15181) 

### 성능 요약

메모리: 29200 KB, 시간: 68 ms

### 분류

구현(implementation)

### 문제 설명

<p>Recently discovered on a distant planet, a race of aliens has music a bit like ours (notes A, B, C, D, E, F and G) but without any sharps or flats. Like our music, after G they start again at A. </p>

<p>To these aliens, beautiful music is any sequence of notes where the difference between 1 note and the next is 2, 4 or 6 notes above the previous note. Anything else is discordant and causes them discomfort.</p>

### 입력 

 <p>Each line of input contains a set of N notes with no spaces between them (0 < N <= 21). Each note will be one of the upper case letters between A and G inclusive. The final line of input will be a # symbol on its own. Do not process this line. </p>

<p>You must assume that a note is the next note of that letter above the previous note. </p>

### 출력 

 <p>For each line of input, if the notes follow the rule for being beautiful music, your output should be</p>

<pre>That music is beautiful.</pre>

<p>Otherwise, the output should be</p>

<pre>Ouch! That hurts my ears. </pre>

