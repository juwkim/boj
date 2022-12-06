# [Bronze I] Aligned Typesetting - 16612 

[문제 링크](https://www.acmicpc.net/problem/16612) 

### 성능 요약

메모리: 32796 KB, 시간: 512 ms

### 분류

구현(implementation)

### 문제 설명

<p>For this problem, a sentence with n words is a sequence of n non-empty strings [w<sub>1</sub>, w<sub>2</sub>, . . . , w<sub>n</sub>]. Given a sentence, a valid typesetting of length L is a string of length exactly L which is formed by concatenating all the words in the sentence and inserting a positive number of spaces between each adjacent pair of words.</p>

<p>An aligned typesetting is a valid typesetting such that the number of spaces in between each adjacent pair of words is equal.</p>

<p>For example, given the sentence [<code>harry</code>, <code>ron</code>, <code>hermione</code>] and using <code>_</code> to indicate a space:</p>

<ul>
	<li>the string <code>__harry_ronhermione</code> is not a valid typesetting;</li>
	<li>the string <code>harry_ron_____hermione</code> is a valid typesetting of length 22 but it is not an aligned typesetting;</li>
	<li>the string <code>harry___ron___hermione</code> is an aligned typesetting of length 22.</li>
</ul>

<p>Darcy was given a sentence of n words and the desired length of typesetting L. Can you help him to figure out whether it is possible to construct an aligned typesetting of the desired length?</p>

### 입력 

 <p>The first line contains two integers n (1 ≤ n ≤ 10<sup>6</sup>), which is the number of words, and L (0 ≤ L ≤ 10<sup>6</sup>), which is the desired length of typesetting.</p>

<p>The next n lines describe the words. Each of these lines contains a single string w<sub>i</sub>, representing the i<sup>th</sup> word in the sentence. The word contains only lowercase letters and consists of at least 1 and at most 10<sup>6</sup> characters.</p>

<p>The total length of all the words in the sentence is guaranteed to be at most 10<sup>6</sup>.</p>

### 출력 

 <p>Display if there is an aligned typesetting of the sentence with the given length.</p>

