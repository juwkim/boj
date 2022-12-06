# [Silver V] Passport Checking - 13211 

[문제 링크](https://www.acmicpc.net/problem/13211) 

### 성능 요약

메모리: 125876 KB, 시간: 372 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 정렬(sorting), 문자열(string)

### 문제 설명

<p>This task is inspired by the recent MH370 stolen passport incident.</p>

<p>The Interpol database contains a list of N stolen passport numbers. We have another list of M passport numbers to check if they are stolen or not.</p>

### 입력 

 <ul>
	<li>The first line of the input contains an integer N. (1 ≤ N ≤ 100,000)</li>
	<li>The next N lines contains the list of N stolen passport numbers, one passport number per line.</li>
	<li>The next line of the input contains an integer M. (1 ≤ M ≤ 100,000)</li>
	<li>The next M lines contains the list of M passport numbers, one passport number per line.</li>
</ul>

<p>Passport numbers are alphanumeric (combination of alphabetic and numeric characters) and are of length at most 15</p>

### 출력 

 <p>Output the total number of stolen passports in the list of M passports.</p>

