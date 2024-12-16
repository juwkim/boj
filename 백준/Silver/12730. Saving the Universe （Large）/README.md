# [Silver II] Saving the Universe (Large) - 12730 

[문제 링크](https://www.acmicpc.net/problem/12730) 

### 성능 요약

메모리: 110576 KB, 시간: 96 ms

### 분류

자료 구조, 다이나믹 프로그래밍, 그리디 알고리즘, 해시를 사용한 집합과 맵, 문자열

### 제출 일자

2024년 12월 16일 12:53:04

### 문제 설명

<p>The urban legend goes that if you go to the Google homepage and search for "Google", the universe will implode. We have a secret to share... It is true! Please don't try it, or tell anyone. All right, maybe not. We are just kidding.</p>

<p>The same is not true for a universe far far away. In that universe, if you search on any search engine for that search engine's name, the universe does implode!</p>

<p>To combat this, people came up with an interesting solution. All queries are pooled together. They are passed to a central system that decides which query goes to which search engine. The central system sends a series of queries to one search engine, and can switch to another at any time. Queries must be processed in the order they're received. The central system must never send a query to a search engine whose name matches the query. In order to reduce costs, the number of switches should be minimized.</p>

<p>Your task is to tell us how many times the central system will have to switch between search engines, assuming that we program it optimally.</p>

### 입력 

 <p>The first line of the input file contains the number of cases, <strong>N</strong>. <strong>N</strong> test cases follow.</p>

<p>Each case starts with the number <strong>S</strong> -- the number of search engines. The next <strong>S</strong> lines each contain the name of a search engine. Each search engine name is no more than one hundred characters long and contains only uppercase letters, lowercase letters, spaces, and numbers. There will not be two search engines with the same name.</p>

<p>The following line contains a number <strong>Q</strong> -- the number of incoming queries. The next <strong>Q</strong>lines will each contain a query. Each query will be the name of a search engine in the case.</p>

<p>Limits</p>

<ul>
	<li>0 < <strong>N</strong> ≤ 20</li>
	<li>2 ≤ <strong>S</strong> ≤ 100</li>
	<li>0 ≤ <strong>Q</strong> ≤ 1000</li>
</ul>

### 출력 

 <p>For each input case, you should output:</p>

<pre>Case #<strong>X</strong>: <strong>Y</strong></pre>

<p>where <strong>X</strong> is the number of the test case and <strong>Y</strong> is the number of search engine switches. Do not count the initial choice of a search engine as a switch.</p>

