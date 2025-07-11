# [Silver I] spam - 3218 

[문제 링크](https://www.acmicpc.net/problem/3218) 

### 성능 요약

메모리: 112640 KB, 시간: 144 ms

### 분류

브루트포스 알고리즘, 많은 조건 분기, 파싱, 문자열

### 제출 일자

2025년 7월 12일 06:51:56

### 문제 설명

<p>Unfortunately , junk messages are very widespread today.</p>

<p>One method of protecting ourselves from spam is to scramble our address when publishing it on the web (or anywhere else) so that programs that automatically search for e-mail addresses won't notice ours.</p>

<p>For this problem, the following holds for valid e-mail addresses:</p>

<ol>
	<li>an e-mail adrress is a string of lowercase letters of the English alphabet ('a'...'z'), as well as a number of full stop characters ('.') and exactly one character '@'.</li>
	<li>there has to be a letter to the immediate left and the immediate right of the '@' character, and the first and last characters in the address may not be a full stop.</li>
</ol>

<p>For example, the addresses 'mama@ta..ta', 'm.am.a@t..a.t..a' and 'm@t' are all valid, while 'ma@', '.@ma.ma', '.mama@tata' i 'ma.ma@tata.tata.' aren't.</p>

<p>We will scramble our address as follows:</p>

<ol>
	<li>we will first replace the '@' character with the string 'at'</li>
	<li>we will then add the string 'nospam' exactly once or zero times anywhere in the address (the beginning and the end included)</li>
</ol>

<p>Write a program that will, given a scrambled e-mail address, determine all different valid addresses it could have originated from. </p>

### 입력 

 <p>The only line of the input will contain a string of at most 100 characters, the scrambled address.</p>

### 출력 

 <p>You should write all different valid e-mail address (in any order) that, when scrambled, can give the given scrambled address. Write every address in a separate line.</p>

