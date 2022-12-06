# [Bronze II] English or French? - 6783 

[문제 링크](https://www.acmicpc.net/problem/6783) 

### 성능 요약

메모리: 29676 KB, 시간: 72 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>You would like to do some experiments in <em>natural language processing</em>. Natural language processing (NLP) involves using machines to recognize human languages.</p>

<p>Your first idea is to write a program that can distinguish English text from French text.</p>

<p>After some analysis, you have concluded that a very reasonable way of distinguishing these two languages is to compare the occurrences of the letters “t” and “T” to the occurrences of the letters “s” and “S”. Specifically:</p>

<ul>
	<li>if the given text has more “t” and “T” characters than “s” and “S” characters, we will say that it is (probably) English text;</li>
	<li>if the given text has more “s” and ”S” characters than “t” and “T” characters, we will say that it is (probably) French text;</li>
	<li>if the number of “t” and “T” characters is the same as the number of “s” and “S” characters, we will say that it is (probably) French text.</li>
</ul>

### 입력 

 <p>The input will contain the number N (0 < N < 10000) followed by N lines of text, where each line has at least one character and no more than 100 characters.</p>

### 출력 

 <p>Your output will be one line. This line will either consist of the word <code>English</code> (indicating the text is probably English) or <code>French</code> (indicating the text is probably French).</p>

