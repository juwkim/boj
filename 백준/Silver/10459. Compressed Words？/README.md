# [Silver V] Compressed Words? - 10459 

[문제 링크](https://www.acmicpc.net/problem/10459) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

구현(implementation), 파싱(parsing), 문자열(string)

### 문제 설명

<p>Steve has come up with a way to compress text, though it may not actually compress the text. Steve considers only individual words, and uses the following rules to define a "compressed word":</p>

<ol>
	<li>a single, lower-case letter is a compressed word</li>
	<li><em>(e<sub>1</sub> e<sub>2</sub> ... e<sub>t</sub> n)</em> where <em>t</em> and <em>n</em> are non-negative integers and <em>e<sub>i</sub></em> is a compressed word.</li>
</ol>

<p>You should observe that a compressed word of one character is the same as an uncompressed word. To uncompress the compressed word <em>(e<sub>1</sub> e<sub>2</sub> ... e<sub>t</sub> n)</em> we uncompress each <em>e<sub>i</sub></em>, concatenate those uncompressed words into a new word, and repeatedly concatenate that word <em>n</em> times. For example:</p>

<ul>
	<li><code>x</code> would be uncompressed as <code>x</code>,</li>
	<li><code>(t 3)</code> would be uncompressed as <code>ttt</code>,</li>
	<li><code>(a (b c 2) 3)</code> would be uncompressed as <code>abcbcabcbcabcbc</code>.</li>
</ul>

<p>Write a program to uncompress a compressed word.</p>

### 입력 

 <p>Your program will be tested on one or more test cases. Each test case is made of one correctly formed compressed word on a separate line. A <code>$</code> character identifies the end of line. The last line of the input, which is not part of the test cases, contains a <code>$</code> by itself (possibly with leading and/or trailing white spaces). Every compressed word in the input is correct according to the rules specified above. Note that a compressed word may contain leading, trailing, and/or embedded spaces. Such spaces should be ignored. Letters and numbers are separated from each other by at least one space character.</p>

### 출력 

 <p>For each test case (i.e., each compressed word), write the uncompressed word on a separate line. There should be no spaces (other than newlines) in the output.</p>

