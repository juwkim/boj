# [Bronze I] Is the Name of This Problem - 4566 

[문제 링크](https://www.acmicpc.net/problem/4566) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 파싱(parsing), 정규 표현식(regex), 문자열(string)

### 문제 설명

<p>The philosopher Willard Van Orman Quine (1908–2000) described a novel method of constructing a sentence in order to illustrate the contradictions that can arise from self-reference. This operation takes as input a single phrase and produces a sentence from that phrase. (The author Douglas R. Hofstadter refers to this process as to Quine a phrase.) We can define the Quine operation like so:</p>

<pre>Quine(A) = "A" A
</pre>

<p>In other words, if A is a phrase, then Quine(A) is A enclosed in quotes ("), followed by a space, followed by A. For example:</p>

<pre>Quine(HELLO WORLD) = "HELLO WORLD" HELLO WORLD
</pre>

<p>Below are some other examples of sentences that can be created by the Quine operation. Note that Quining allows sentences to be indirectly self-referential, such as the last sentence below.</p>

<pre>"IS A SENTENCE FRAGMENT" IS A SENTENCE FRAGMENT
"IS THE NAME OF THIS PROBLEM" IS THE NAME OF THIS PROBLEM
"YIELDS FALSEHOOD WHEN QUINED" YIELDS FALSEHOOD WHEN QUINED
</pre>

<p>Your goal for this problem is to take a sentence and decide whether the sentence is the result of a Quine operation.</p>

### 입력 

 <p>The input will consist of a sequence of sentences, one sentence per line, ending with a line that has the single word, <strong><code>END</code></strong>. Each sentence will contain only uppercase letters, spaces, and quotation marks. Each sentence will contain between 1 and 80 characters and will not have any leading, trailing, or consecutive spaces.</p>

<p>You must decide whether each sentence is the result of a Quine operation. To be a Quine, a sentence must match the following pattern <em>exactly</em>:</p>

<ol>
	<li>A quotation mark</li>
	<li>Any nonempty sequence of letters and spaces (call this phrase <var>A</var>)</li>
	<li>A quotation mark</li>
	<li>A space</li>
	<li>Phrase <var>A</var>—exactly as it appeared in (2)</li>
</ol>

<p>If it matches this pattern, the sentence is a Quine of the phrase <var>A</var>. Note that phrase A must contain the exact same sequence of characters both times it appears.</p>

### 출력 

 <p>There will be one line of output for each sentence in the data set. If the sentence is the result of a Quine operation, your output should be of the form, <code>Quine(<var>A</var>)</code>, where <var>A</var> is the phrase to Quine to create the sentence.</p>

<p>If the sentence is not the result of a Quine operation, your output should be the phrase, <strong><code>not a quine</code></strong>.</p>

