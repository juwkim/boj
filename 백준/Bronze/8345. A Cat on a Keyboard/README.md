# [Bronze I] A Cat on a Keyboard - 8345 

[문제 링크](https://www.acmicpc.net/problem/8345) 

### 성능 요약

메모리: 39328 KB, 시간: 236 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>A cat is walking on Ann's computer's keyboard. Ann's keyboard looks as follows:<sup>1</sup></p>

<p style="text-align: center;"><img alt="" src=""></p>

<p>Ann is quite sure that the text created by the cat contains a deeper meaning, so she is willing to decode it in order to understand this meaning. She is got an idea to number the rows of the keys on the keyboard with digits from 1 to 5 (the topmost row gets number 1 and the bottommost - number 5) and to change each character in the cat's text with the number of row of the key corresponding to it. There is a chance that some interesting number will be a result of such transformation and that Ann's mathematical skills will help her understand the text's meaning more easily.</p>

<p>Write a program that:</p>

<ul>
	<li>reads the cat's text from the standard input,</li>
	<li>transforms the cat's text to the digital form,</li>
	<li>writes the result to the standard output.</li>
</ul>

<p><sup>1</sup>A picture taken from <code>http://acm.uva.es/p</code>.</p>

### 입력 

 <p>The first and only line of input contains one sequence of at least 1 and at most 500 000 characters. You can assume that the cat did not step on any of the keys: Alt, BackSpace, Control, Enter, Tab.</p>

### 출력 

 <p>The first and only line of output should contain a sequence consisting of digits 1, 2, 3, 4, 5, representing the decoded version of the cat's text.</p>

