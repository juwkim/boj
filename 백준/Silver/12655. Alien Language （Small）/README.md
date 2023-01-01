# [Silver IV] Alien Language (Small) - 12655 

[문제 링크](https://www.acmicpc.net/problem/12655) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

브루트포스 알고리즘(bruteforcing), 자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 파싱(parsing), 문자열(string)

### 문제 설명

<p>After years of study, scientists at Google Labs have discovered an alien language transmitted from a faraway planet. The alien language is very unique in that every word consists of exactly <strong>L</strong> lowercase letters. Also, there are exactly <strong>D</strong> words in this language.</p>

<p>Once the dictionary of all the words in the alien language was built, the next breakthrough was to discover that the aliens have been transmitting messages to Earth for the past decade. Unfortunately, these signals are weakened due to the distance between our two planets and some of the words may be misinterpreted. In order to help them decipher these messages, the scientists have asked you to devise an algorithm that will determine the number of possible interpretations for a given pattern.</p>

<p>A pattern consists of exactly <strong>L</strong> tokens. Each token is either a single lowercase letter (the scientists are very sure that this is the letter) or a group of unique lowercase letters surrounded by parenthesis ( and ). For example: (ab)d(dc) means the first letter is either a or b, the second letter is definitely d and the last letter is either d or c. Therefore, the pattern (ab)d(dc) can stand for either one of these 4 possibilities: add, adc, bdd, bdc.</p>

### 입력 

 <p>The first line of input contains 3 integers, <strong>L</strong>, <strong>D</strong> and <strong>N</strong> separated by a space. <strong>D</strong> lines follow, each containing one word of length <strong>L</strong>. These are the words that are known to exist in the alien language. <strong>N</strong> test cases then follow, each on its own line and each consisting of a pattern as described above. You may assume that all known words provided are unique.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>L</strong> ≤ 10</li>
	<li>1 ≤ <strong>D</strong> ≤ 25</li>
	<li>1 ≤ <strong>N</strong> ≤ 10</li>
</ul>

### 출력 

 <p>For each test case, output </p>

<pre>Case #<strong>X</strong>: <strong>K</strong></pre>

<p>where <strong>X</strong> is the test case number, starting from 1, and <strong>K</strong> indicates how many words in the alien language match the pattern.</p>

