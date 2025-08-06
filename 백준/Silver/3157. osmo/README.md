# [Silver I] osmo - 3157 

[문제 링크](https://www.acmicpc.net/problem/3157) 

### 성능 요약

메모리: 111668 KB, 시간: 152 ms

### 분류

구현, 브루트포스 알고리즘

### 제출 일자

2025년 8월 7일 01:51:06

### 문제 설명

<p>Word search is a very popular enigmatic game that consists of a table with letters arranged in N rows and N columns and a list of words we have to search for. </p>

<p>To solve an instance of word search we, for each word from the list, find all appearances of that word in the table and cross out all the letters forming that particular appearance. The word can start anywhere and lay in any of the eight directions (up, down, left, right and the four diagonal directions). </p>

<p>Reading all non-crossed letters in row-major order (up to down and in each row from left to right) gives the solution of the word search puzzle. </p>

<p>Write a program that will find the solution of the given puzzle. </p>

### 입력 

 <p>The first line of input contains an integer N, 1 ≤ N ≤ 10, the size of the table. </p>

<p>Each of the next N lines contains a sequence of N characters representing one row of the table. </p>

<p>The next line contains an integer R, 1 ≤ R ≤ 100, the number of words in the list. </p>

<p>Each of the next R lines contains one word from the list, at most 10 characters long. </p>

<p>All of the letters in the word search and all the words in the list will consist of lowercase letters of the English alphabet ('a'-'z'). </p>

### 출력 

 <p>The first and only line of output should contain the solution of the puzzle. </p>

<p>Note: the test data will be such that a solution of at least one letter will always exists. </p>

