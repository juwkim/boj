# [Bronze II] Letter Cookies - 11117 

[문제 링크](https://www.acmicpc.net/problem/11117) 

### 성능 요약

메모리: 32004 KB, 시간: 604 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Sætre has finally decided to put their famous Letter Cookies back on market again. Of course they are just as interesting to play with as to eat. Your little sister is trying to make words out of the letters she found in the box, but you want to be faster than her to decide whether it is possible to make the word or not.</p>

<p>Given the letters in the cookie box, is it possible to spell out the words your little sister knows how to spell? (After creating a word, she scrambles the cookies again and can reuse the letters for later words.)</p>

### 입력 

 <p>The first line of the input consists of a single number T, the number of letter cookie boxes your sister has. Each test case starts with a line describing all the letters in this box, in no particular order. Then follows a line with W, the number of words she would like to spell, and then follow the W words to write on a single line each.</p>

<ul>
	<li>0 < T ≤ 100</li>
	<li>0 < W ≤ 100</li>
	<li>All letters are uppercase letters from the english alphabet (A-Z).</li>
	<li>There are at most 1000 letters in each cookie box.</li>
	<li>Each word has at most 100 letters (but is not necessarily an actual English word).</li>
</ul>

### 출력 

 <p>For each word, output a line containing YES if it is possible to spell the word, or NO if it is not possible.</p>

