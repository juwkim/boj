# [Silver II] Ignore all my comments (Large) - 12275 

[문제 링크](https://www.acmicpc.net/problem/12275) 

### 성능 요약

메모리: 109300 KB, 시간: 116 ms

### 분류

자료 구조, 구현, 스택

### 제출 일자

2024년 2월 15일 04:48:57

### 문제 설명

<p>Good programmers write fabulous comments. Igor is a programmer and he likes the old C-style comments in <b><code>/* ... */</code></b> blocks. For him, it would be ideal if he could use this style as a uniform comment format for all programming languages or even documents, for example Python, Haskell or HTML/XML documents.</p>

<p>Making this happen doesn't seem too difficult to Igor. What he will need is a comment pre-processor that removes all the comment blocks in <b><code>/*</code></b>, followed by comment text, and by another <b><code>*/</code></b>. Then the processed text can be handed over to the compiler/document renderer to which it belongs—whatever it is.</p>

<p>Igor's pre-processor isn't quite that simple, though. Here are some cool things it does:</p>

<ul>
	<li>The comments the pre-processor reads can be nested the same way brackets are nested in most programming languages. It's possible to have comments inside comments. For example, the following code block has an outer level of comments that should be removed by the comment pre-processor. The block contains two inner comments.
	<pre>printf("Hello /* a comment /* a comment inside comment */ 
        inside /* another comment inside comment */ 
        string */ world");
</pre>
	After the pre-process step, it becomes:

	<pre>printf("Hello  world");
</pre>
	</li>
	<li>Igor recognizes comments can appear anywhere in the text, including inside a string <code>"/*...*/"</code>, a constant number <code>12/*...*/34</code> or even in a character escape <code>\/*...*/n</code>
	<p>Or more formally:</p>

	<pre>text:
  text-piece
  text-piece remaining-text
text-piece:
  char-sequence-without-/*
  empty-string
remaining-text:
  comment-block text

comment-block:
  /* comment-content */
comment-content:
  comment-piece
  comment-piece remaining-comment
comment-piece:
  char-sequence-without-/*-or-*/
  empty-string
remaining-comment:
  comment-block comment-content

char:
  letters
  digits
  punctuations
  whitespaces
</pre>
	</li>
</ul>

<p>Our pre-processor, given a <code><b>text</b></code>, removes all <code><b>comment-block</b></code> instances as specified.</p>

### 입력 

 <p>A text document with comment blocks in <b><code>/*</code></b> and <b><code>*/</code></b>. The input file is valid. It follows the specification of <b><code>text</code></b> in the problem statement. The input file always terminates with a newline symbol.</p>

### 출력 

 <p>We only have one test case for this problem. First we need to output the following line.</p>

<pre>Case #1:
</pre>

<p>Then, print the document with all comments removed, in the way specified in the problem statements. Don't remove any spaces or empty lines outside comments.</p>

