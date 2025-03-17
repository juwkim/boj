# [Silver II] Extra Krunch - 27082 

[문제 링크](https://www.acmicpc.net/problem/27082) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

자료 구조, 구현, 스택, 문자열

### 제출 일자

2025년 3월 18일 05:50:31

### 문제 설명

<p> </p>

<p>A krunched word has no vowels ("A", "E", "I", "O", and "U") and no repeated letters. Removing vowels and letters that appear twice or more from MISSISSIPPI yields MSP. In a krunched word, a letter appears only once, the first time it would appear in the unkrunched word. Vowels never appear.</p>

<p>Krunched phrases similarly have no vowels and no repeated letters. Consider this phrase:</p>

<pre>RAILROAD CROSSING</pre>

<p>and its krunched version:</p>

<pre>RLD CSNG</pre>

<p>Blanks are krunched differently. Blanks are removed so that a krunched phrase has no blanks on its beginning or end, never has two blanks in a row, and has no blanks before punctuation. Otherwise, blanks not removed. If we represent blanks by "_",</p>

<pre>MADAM_I_SAY_I_AM_ADAM__</pre>

<p>krunches to:</p>

<pre>MD_SY</pre>

<p>where the single remaining blank is shown by "_".</p>

<p>Write a program that reads a line of input (whose length ranges from 2 to 70 characters), and krunches it. Put the krunched word or phrase in the output file. The input line has only capital letters, blanks, and the standard punctuation marks: period, comma, and question mark.</p>

### 입력 

 <p>A single line to be krunched.</p>

### 출력 

 <p>A single krunched line that follows the rules above.</p>

