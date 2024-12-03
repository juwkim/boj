# [Bronze I] Alternative Encryption - 32886 

[문제 링크](https://www.acmicpc.net/problem/32886) 

### 성능 요약

메모리: 220832 KB, 시간: 216 ms

### 분류

해 구성하기, 문자열

### 제출 일자

2024년 12월 3일 16:44:14

### 문제 설명

<p>In the fight against theft of intellectual property by rivalling universities, TU Delft has decided to implement a system of secure communication, to be called New Well-Encrypted Remote Communication. All internal communication will be encrypted before being sent over the network, and then decrypted upon arrival. They have already set up the infra-structure, they have come to you for the encryption.</p>

<p>You are tasked to design an algorithm for both encryption and decryption of text consisting of only English lowercase letters. You do not need to tell them how you do it, in fact, they encourage you to keep it a secret, to improve security. Your algorithm only needs to meet the following criteria:</p>

<ul>
	<li>No matter what the text is, encrypting it and then decrypting the result should obviously yield the original text.</li>
	<li>To make sure there are no issues with the transmission, the encrypted text should also consist of only English lowercase letters and should have the same number of letters as the original text.</li>
	<li>To make sure the code cannot be broken easily, for all <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>, the <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>th letter of the encrypted text should differ from the <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>th letter of the original text.</li>
</ul>

<p>The word "<code>nwercjury</code>" for example may not be encrypted as "<code>irritating</code>", because the number of letters does not match. Nor may you encrypt it as "<code>imbecilic</code>", since the fifth letter is a '<code>c</code>' in both. An example of an acceptable encryption is "<code>fantastic</code>" (both have an '<code>n</code>' and a '<code>c</code>', but in different positions).</p>

<p>Your program will be run twice for each test case. In the first pass, your program will be given a number of strings to encrypt. In the second pass, your program will be given the strings as encrypted by the first pass, which it should then decrypt to retrieve the original input.</p>

<p>A testing tool is provided to help you develop your solution.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with either "<code>encrypt</code>" or "<code>decrypt</code>", indicating the action your program has to perform.</li>
	<li>One line with an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 1000$</span></mjx-container>), the number of strings.</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> lines, each with a string <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-texatom space="4" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mi>s</mi><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le |s| \le 100$</span></mjx-container>), the text to encrypt or decrypt. All input strings consist of only English lowercase letters (<code>a-z</code>).</li>
</ul>

### 출력 

 <p>For each string, output its encryption or decryption, as required.</p>

