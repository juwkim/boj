# [Silver III] PASTE - 3294 

[문제 링크](https://www.acmicpc.net/problem/3294) 

### 성능 요약

메모리: 217612 KB, 시간: 840 ms

### 분류

자료 구조, 연결 리스트

### 제출 일자

2024년 5월 2일 03:09:30

### 문제 설명

<p>A document processed by a text processor consists of N lines of text. The first line contains number 1, the second line contains number 2 and so on till the Nth line which contains number N.</p>

<p>Exactly M operations 'cut and paste' have been performed in that document. It operates on a selected group of consecutive lines; 'cut' removes selected text from the document and 'paste' inserts removed text elsewhere in the rest of the document.</p>

<p>Write a program that will for given sequence of  'cut and paste' operations determine the contents of the first ten lines of final document after all operations have been performed.</p>

### 입력 

 <p>The first line of input file contains two natural numbers N, number of lines in a document (10 ≤ N ≤ 100,000) and K, number of operations 'cut and paste' performed on a document (1 ≤ K ≤ 1000), separated by a space character.</p>

<p>Next K lines contain information of 'cut and paste' operations in the order of their execution. </p>

<p>Each line contain three natural numbers A, B and C, 1 ≤ A ≤ B ≤ N, 0 ≤ C ≤ N-(B-A+1), separated by a space character. Numbers A and B determine first and last line of selected text, and number C determines the line after which the removed text should be inserted. If C equals 0 then removed test should be inserted at the beginning of the document.</p>

### 출력 

 <p>The output file should consist of 10 lines containing the numbers written in the first 10 lines of final document after all operations have been performed.</p>

