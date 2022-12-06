# [Bronze I] Arabic and English - 9557 

[문제 링크](https://www.acmicpc.net/problem/9557) 

### 성능 요약

메모리: 114488 KB, 시간: 132 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Some computer programs have problems in displaying Arabic text, especially when mixed with English words in the same line, because Arabic is written from right to left and English is written from left to right. In this problem we will try to fix a text with some corrupted lines which consist of a mixture of Arabic and English words. For simplicity, all Arabic letters will be replaced with the letter '#'.</p>

<p>Each line will contain at most one English word. For a line containing an English word, the program that will fix the text will swap the words before the English word with the words after the English word. The words before the English word will remain in the same order. The words after the English word will also remain in the same order. For example, if the line is "# #### ### abc ##", it will be fixed to become "## abc # #### ###".</p>

<p>Please note that a line that contains words only of the same language is not corrupt.</p>

### 입력 

 <p>Your program will be tested on one or more test cases. The first line of the input will be a single integer T, the number of test cases (1 ≤ T ≤ 100). Next 2T lines contain the test cases, each on a pair of lines.</p>

<p>The first line of each case contains a single integer N, the number of words in the line to fix (1 ≤ N ≤ 100). The second line contains N words, separated by single spaces, with no leading or trailing spaces, and each word will be at least 1 character and at most 10 characters long.</p>

<p>Each word will be either Arabic or English. Arabic words will consist of one to ten '#' letters, and English words will consist of one to ten English lower case letters. Each line contains at most one English word.</p>

### 출력 

 <p>For each test case, output, on a single line, the fixed line of input text.</p>

