# [Silver I] Code Formatting - 7399 

[문제 링크](https://www.acmicpc.net/problem/7399) 

### 성능 요약

메모리: 111456 KB, 시간: 108 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2025년 8월 3일 13:06:55

### 문제 설명

<p>Programmers are known to wage religious wars when issues of proper code formatting are discussed. When new team of programmers starts working on a project, it often brings slightly different code formatting style and wants to reformat old source code according to their own style. Moreover, inexperienced programmers often neglect the importance of good and consistent code style, thus complicating the work of their teammates and themselves. This situation creates thriving market for code formatting tools. </p>

<p>You are taking part in a proof-of-concept project for a new code formatting tool code named Salvation. This is only a pilot project aimed not for a practical usefulness, but to demonstrate your ability to parse and format code of a high-level language. Your task is to write code formatter for a language called TRIVIAL (The Rival Implementation-Agnostic Language). This language has trivial lexical and grammatical structures. It does not have any keywords and control structures, because all constructs of the language are represented as function calls and closures.</p>

<p>The lexical structure consists of identifiers, opening and closing parenthesis and curly braces, commas, and semi-colons. Identifiers consist only of digits '0'--'9' and Latin letters 'a'--'z', 'A'--'Z'. Lexical terms may be separated by whitespaces, leading and trailing whitespaces in the file are also allowed. Whitespace may consist of spaces, tab characters (ASCII code 9), and line separators (a pair of ASCII 13, 10). </p>

<p>The structure of the valid trivial program is derived from the following productions:</p>

<ul>
	<li>Program ::= Block</li>
	<li>Block ::= '{' Statements '}'</li>
	<li>Statements ::= Statement <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$|$</span></mjx-container> Statement Statements</li>
	<li>Statement ::= Expression ';'</li>
	<li>Expression ::= <em>identifier</em> ['(' Arguments ')'] [Block]</li>
	<li>Arguments ::= Expression <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$|$</span></mjx-container> Expression ',' Arguments</li>
</ul>

<p>Properly formatted trivial program additionally conforms to the following rules:</p>

<ul>
	<li>There are no empty lines.</li>
	<li>Tab characters are not used.</li>
	<li>The first character of the file is opening curly brace '{' (no preceding whitespaces), and the last character of the file is closing curly brace '}' (no trailing whitespaces).</li>
	<li>Each line is preceded by <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4N$</span></mjx-container> space characters, where <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> is called <em>indentation level</em>.</li>
	<li>The first and the last lines of the program have zero indentation level.</li>
	<li>Lines that constitute block body and are enclosed in curly braces '{'...'}' have one more indentation level.</li>
	<li>No whitespace is allowed inside the line with the exception of the following two cases where a single space character is mandatory: before opening curly brace character '{' and after comma ','.</li>
	<li>Lines (with the only exception of the last line) end with semicolon ';' or opening curly brace '{' characters. These characters cannot appear in the middle or at the beginning of any line (including the last one).</li>
	<li>Closing curly brace '}' characters appear only at the beginning of lines after indentation spaces.</li>
</ul>

<p>See sample output section for an example of properly formatted trivial program.</p>

### 입력 

 <p>The input file contains valid trivial program. Size of the input file does not exceed 2000 bytes.</p>

### 출력 

 <p>Write to the output file properly formatted trivial code for the program given in the input file.</p>

