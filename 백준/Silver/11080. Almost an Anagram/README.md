# [Silver IV] Almost an Anagram - 11080 

[문제 링크](https://www.acmicpc.net/problem/11080) 

### 성능 요약

메모리: 116024 KB, 시간: 144 ms

### 분류

많은 조건 분기(case_work), 문자열(string)

### 문제 설명

<p>Andy loves anagrams. For the uninitiated, an anagram is a word formed by rearranging the letters of another word, for example rasp can be rearranged to form spar. Andy is interested to know if two words are almost anagrams. A word is almost an anagram of another word if:</p>

<ul>
	<li>one word is shorter than the other by one letter but otherwise contains the same letters in any order; or</li>
	<li>the two words are the same length and their character multisets differ by one character only e.g. “aaa” and “aab”</li>
</ul>

<p>Your job is to help Andy to determine if two words are identical, anagrams, almost anagrams or nothing like each other.</p>

### 입력 

 <p>The input contains a single test case.</p>

<p>The input will be a single line of text containing a pair of words separated by a single space. The words will be in lower case and will contain alphabetic characters only. Words will contain between 1 and 1000 letters inclusive.</p>

### 출력 

 <p>Your program should produce one line of output as follows:</p>

<p>If the words are identical, output: word<sub>a</sub> is identical to word<sub>b</sub><br>
If the words are anagrams, output: word<sub>a</sub> is an anagram of word<sub>b</sub><br>
If the words are almost anagrams, output: word<sub>a</sub> is almost an anagram of word<sub>b</sub><br>
Otherwise, output: word<sub>a</sub> is nothing like word<sub>b</sub></p>

<p>In all cases the first word in the output sentence must be the shorter word or if the words are the same length the first word must be the lexicographically least.</p>

