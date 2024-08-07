# [Silver III] Letter Sequence Analysis - 4695 

[문제 링크](https://www.acmicpc.net/problem/4695) 

### 성능 요약

메모리: 114176 KB, 시간: 168 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 정렬, 문자열, 트리를 사용한 집합과 맵

### 제출 일자

2024년 4월 10일 18:01:07

### 문제 설명

<p>Cryptographic analysis makes extensive use of the frequency with which letters and letter sequences occur in a language. If an encrypted text is known to be in english, for example, a great deal can be learned from the fact that the letters E, L, N, R, S, and T are the most common ones used in written english. Even more can be learned if common letter pairs, triplets, etc. are known.</p>

<p>For this problem you are to write a program which accepts as input a text file of unspecified length and performs letter sequence analysis on the text. The program will report the five most frequent letter sequences for each set of sequences from one to five letters. That is it will report the individual characters which occur with the five highest frequencies, the pairs of characters which occur with the five highest frequencies, and so on up to the letter sequences of five characters which occur with the five highest frequencies.</p>

<p>The program should consider contiguous sequences of alphabetic characters only, and case should be ignored (e.g. an 'a' is the same as an 'A'). A report should be produced using the format shown in the example at the end of this problem description. For each sequence length from one to five, the report should list the sequences in descending order of frequency. If there are several sequences with the same frequency then all sequences should be listed in alphabetical order as shown (list all sequences in upper case). Finally, if there are less than five distinct frequencies for a particular sequence length, simply report as many distinct frequency lists as possible.</p>

### 입력 

 Empty

### 출력 

 Empty

