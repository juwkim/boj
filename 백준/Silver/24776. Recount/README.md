# [Silver V] Recount - 24776 

[문제 링크](https://www.acmicpc.net/problem/24776) 

### 성능 요약

메모리: 144080 KB, 시간: 300 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 문자열(string), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p><img alt="" src="" style="width: 150px; height: 135px; float: right;">The recent schoolboard elections were hotly contested: a proposal to swap school start times for elementary and high school students, a controversial new dress code proposal that bans athletic clothes in school, and a proposal to raise real-estate taxes to pay for a new football practice facility, and the list goes on and on. It is now hours after the polls have closed and a winner has yet to emerge! </p>

<p>In their desperation, the election officials turn to you and ask you to write a program to count the vote!</p>

### 입력 

 <p>The input consists of a single test case, which is a list of votes cast. Each line in the input contains the name of a candidate for whom a vote was cast.  A name may consist of multiple words, separated by spaces. Words contain letters or hyphens, but no other punctuation characters.  There will be at least 2 votes on the list. The list of votes ends with a single line containing the characters <code>***</code>. This line should not be counted.  There can be up to $100,000$ valid votes.</p>

### 출력 

 <p>If a candidate obtained a simple or absolute majority of all votes cast (that is, more than any other candidate), output the name of this candidate! If no candidate obtained a simple majority, output: "<code>Runoff!</code>" (don't forget to include the exclamation mark!)</p>

