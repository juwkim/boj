# [Silver IV] Short Phrase - 11039 

[문제 링크](https://www.acmicpc.net/problem/11039) 

### 성능 요약

메모리: 115552 KB, 시간: 140 ms

### 분류

구현(implementation)

### 문제 설명

<p>A Short Phrase (aka. Tanku) is a fixed verse, inspired by Japanese poetry Tanka and Haiku. It is a sequence of words, each consisting of lowercase letters 'a' to 'z', and must satisfy the following condition:</p>

<blockquote>
<p>(The Condition for a Short Phrase)<br>
The sequence of words can be divided into five sections such that the total number of the letters in the word(s) of the first section is five, that of the second is seven, and those of the rest are five, seven, and seven, respectively.</p>
</blockquote>

<p>The following is an example of a Short Phrase.</p>

<pre>do the best
and enjoy today
at acm icpc</pre>

<p>In this example, the sequence of the nine words can be divided into five sections (1) "do" and "the", (2) "best" and "and", (3) "enjoy", (4) "today" and "at", and (5) "acm" and "icpc" such that they have 5, 7, 5, 7, and 7 letters in this order, respectively. This surely satisfies the condition of a Short Phrase.</p>

<p>Now, Short Phrase Parnassus published by your company has received a lot of contributions. By an unfortunate accident, however, some irrelevant texts seem to be added at beginnings and ends of contributed Short Phrases. Your mission is to write a program that finds the Short Phrase from a sequence of words that may have an irrelevant prefix and/or a suffix.</p>

### 입력 

 <p>The input consists of multiple datasets, each in the following format.</p>

<pre>n
w<sub>1</sub>
... 
w<sub>n</sub></pre>

<p>Here, n is the number of words, which is a positive integer not exceeding 40; w<sub>i</sub> is the i-th word, consisting solely of lowercase letters from 'a' to 'z'. The length of each word is between 1 and 10, inclusive. You can assume that every dataset includes a Short Phrase.</p>

<p>The end of the input is indicated by a line with a single zero.</p>

### 출력 

 <p>For each dataset, output a single line containing i where the first word of the Short Phrase is w<sub>i</sub>. When multiple Short Phrases occur in the dataset, you should output the first one.</p>

