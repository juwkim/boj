# [Bronze I] Speaking in Tongues (Small) - 12400 

[문제 링크](https://www.acmicpc.net/problem/12400) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

애드 혹(ad_hoc), 구현(implementation), 문자열(string)

### 문제 설명

<p>We have come up with the best possible language here at Google, called Googlerese. To translate text into Googlerese, we take any message and replace each English letter with another English letter. This mapping is <em>one-to-one</em> and <em>onto</em>, which means that the same input letter always gets replaced with the same output letter, and different input letters always get replaced with different output letters. A letter may be replaced by itself. Spaces are left as-is.</p>

<p>For example (and here is a hint!), our awesome translation algorithm includes the following three mappings: 'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'. This means that "a zoo" will become "y qee".</p>

<p>Googlerese is based on the best possible replacement mapping, and we will never change it. It will always be the same. In every test case. We will not tell you the rest of our mapping because that would make the problem too easy, but there are a few examples below that may help.</p>

<p>Given some text in Googlerese, can you translate it to back to normal text?</p>

<h3>Solving this problem</h3>

<p>Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has only <strong>1 Small input</strong>. Once you have solved the Small input, you have finished solving this problem.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow, one per line.</p>

<p>Each line consists of a string <strong>G</strong> in Googlerese, made up of one or more words containing the letters 'a' - 'z'. There will be exactly one space (' ') character between consecutive words and no spaces at the beginning or at the end of any line.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 30.</li>
	<li><strong>G</strong> contains at most 100 characters.</li>
	<li>None of the text is guaranteed to be valid English.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>X</strong>: <strong>S</strong>" where <strong>X</strong> is the case number and <strong>S</strong> is the string that becomes <strong>G</strong> in Googlerese.</p>

