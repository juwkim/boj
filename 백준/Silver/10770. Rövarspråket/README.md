# [Silver V] Rövarspråket - 10770 

[문제 링크](https://www.acmicpc.net/problem/10770) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>In Sweden, there is a simple child’s game similar to Pig Latin called Rövarspråket (Robbers Language).</p>

<p>In the CCC version of Rovarspr ¨ aket, every consonant is replaced by three letters, in the following order:</p>

<ul>
	<li>the consonant itself;</li>
	<li>the vowel closest to the consonant in the alphabet (e.g., if the consonant is d, then the closest vowel is e), with the rule that if the consonant falls exactly between two vowels, then the vowel closer to the start of the alphabet will be chosen (e.g., if the consonant is c, then the closest vowel is a);</li>
	<li>the next consonant in the alphabet following the original consonant (e.g., if the consonant is d, then the next consonant is f) except if the original consonant is z, in which case the next consonant is z as well.</li>
</ul>

<p>Vowels in the word remain the same. (Vowels are a, e, i, o, u and all other letters are consonants.)</p>

<p>Write a program that translates a word from English into Rövarspråket.</p>

### 입력 

 <p>The input consists of one word entirely composed of lower-case letters. There will be at least one letter and no more than 30 letters in this word.</p>

### 출력 

 <p>Output the word as it would be translated into Rövarspråket on one line.</p>

