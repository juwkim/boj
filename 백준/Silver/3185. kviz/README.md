# [Silver III] kviz - 3185 

[문제 링크](https://www.acmicpc.net/problem/3185) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

많은 조건 분기, 구현, 문자열

### 제출 일자

2024년 2월 15일 06:38:13

### 문제 설명

<p>In one very popular internet quiz, player has to give the answer to one very hard question. If player does not give the answer after some period of time, the quiz software will give him the first hint, after that the second hint, and in the end the third hint.</p>

<p>The only characters that appear in the answer are letters and the following characters: '.' (dot), ',' (comma), ':' (colon), ';' (semi-colon), '!' (exclamation mark), '?' (question mark), '-' (dash) and space (there will be no leading or trailing spaces however). By LETTERS, we mean all letters of English alphabet 'a'-'z' and 'A'-'Z', and by VOWELS we mean letters 'aeiouAEIOU'.</p>

<p>How do we generate hints?</p>

<ul>
	<li>First hint is generated from the correct answer - we simply replace the letters with the character '.' (dot).</li>
	<li>Second hint is generated from the first hint - we reveal the first third of all the letters (if the number of letters is not divisible by 3, quotient should be rounded to the nearest integer).</li>
	<li>Third hint is generated from the second hint - we reveal all the remaining vowels. If there are no unrevealed vowels, then the third hint is generated from the first hint - we reveal first two-thirds of all the letters (if number of letters is not divisible by 3, quotient should be rounded to the nearest integer).</li>
</ul>

<p>Write a program that will generate all three hints from the given answer.</p>

### 입력 

 <p>First and only line of input contains the correct answer from which we have to generate hints. The total number of characters will be at most 50.</p>

### 출력 

 <p>First line of output should contain the first hint, second line should contain the second hint, and the third line should contain the third hint.</p>

