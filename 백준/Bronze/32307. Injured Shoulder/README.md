# [Bronze II] Injured Shoulder - 32307 

[문제 링크](https://www.acmicpc.net/problem/32307) 

### 성능 요약

메모리: 108080 KB, 시간: 92 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 문자열

### 제출 일자

2024년 9월 16일 23:20:01

### 문제 설명

<p>Dr. Orooji injured his right shoulder a few months ago and could type with only one hand for a while. For some reasons, Dr. O missed the space character (blank) often and two words would be next to each other without the space (i.e., words concatenated) and the spell-checker would complain.</p>

<p>Given the words in a dictionary and a word Dr. O has typed, determine the status of the typed word.</p>

### 입력 

 <p>The first input line contains an integer, n (2 ≤ n ≤ 20), indicating the number of words in the dictionary. Each of the next n input lines contains a dictionary word. Each word starts in column 1, contains at least one lowercase letter, at most 20 lowercase letters, and no other characters. Assume that the dictionary words are unique, i.e., no duplicates.</p>

<p>The next input line contains an integer, m (1 ≤ m ≤ 100), indicating the number of words Dr. O has typed. Each of the next m input lines contains a typed word. Each typed word starts in column 1, contains at least one lowercase letter, at most 40 lowercase letters, and no other characters.</p>

### 출력 

 <p>For each typed word, output one line as follows:</p>

<ul>
	<li>1 – If the typed word is in the dictionary.</li>
	<li>2 – If the typed word is a concatenation of two words in the dictionary, i.e., Dr. O missed typing the space character (blank).</li>
	<li>0 (zero) – Otherwise.</li>
</ul>

<p>Note that if a typed word is in the dictionary and it is also a concatenation of two words in the dictionary, output should be 1.</p>

