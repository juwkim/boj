# [Silver I] Frugal Search - 4617 

[문제 링크](https://www.acmicpc.net/problem/4617) 

### 성능 요약

메모리: 110760 KB, 시간: 100 ms

### 분류

파싱, 정렬, 문자열

### 제출 일자

2025년 8월 16일 03:45:16

### 문제 설명

<p>For this problem you will write a search engine that takes a query, searches a collection of words, and finds the lexicographically smallest word that matches the query (i.e., the matching word that would appear first in an English dictionary). A query is a sequence of one or more terms separated by single vertical bars ("|"). A term is one or more letters followed by zero or more signed letters. A signed letter is either +s ("positive" s) or -s ("negative" s), where s is a single letter. All letters are lowercase, and no letter will appear more than once within a term. A query will not contain spaces. A term matches a word if the word contains at least one of the unsigned letters, all of the positive letters, and none of the negative letters; a query matches a word if at least one of its terms matches the word.</p>

### 입력 

 <p>The input consists of one or more test cases followed by a line containing only "#" that signals the end of the input. Each test case consists of 1–100 words, each on a line by itself, followed by a line containing only "*" that marks the end of the word list, followed by one or more queries, each on a line by itself, followed by a line containing only "**" that marks the end of the test case. Each word will consist of 1–20 lowercase letters. All words within a test case will be unique. Each query will be as defined above and will be 1–79 characters long.</p>

### 출력 

 <p>For each query, output a single line containing the lexicographically smallest word within that test case that matches the query, or the word NONE if there is no matching word. At the end of each test case, output a dollar sign on a line by itself.</p>

