# [Silver III] Help cupid - 10402 

[문제 링크](https://www.acmicpc.net/problem/10402) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2024년 2월 10일 01:49:52

### 문제 설명

<p>Cupid’s job is getting harder, so he is adopting new technologies to help him with his difficult task of matching people into happy couples. He appointed the best programmers in his staff to a new project called Advanced Couples Matching (ACM). For this project, the programmers need to produce an algorithm that takes a set of an even number of N lonely persons and matches them into N/2 couples, such that each person is in exactly one couple.</p>

<p>Sadly, the data available about each person is limited. In this modern world, using gender, ethnicity, age or nationality as criteria to form couples is not a sensible option, so the programmers can only use data about the internet connection of each candidate. They decided to focus this stage on time zones. People living in closer time zones are more likely to find time to interact with each other. Thus, the programmers decided to create couples so as to minimize the total time difference.</p>

<p>Each time zone is identified by an integer between −11 and 12, inclusive, representing its difference in hours from a particular time zone called Coordinated Universal Time (or UTC). The time difference of two people living in time zones represented by integers i and j is the minimum between |i − j| and 24 − |i − j|. Given a partition of a set of an even number N of candidates into N/2 couples, its total time difference is the sum of the time difference of each couple.</p>

<p>You are asked to write a program that receives as input the time zones of a set of N candidates. The output of the program must be the minimum total time difference among all possible partitions of the set into couples.</p>

### 입력 

 <p>The first line contains an even integer N (2 ≤ N ≤ 1000) representing the number of candidates to be coupled. The second line contains N integers T<sub>1</sub>, T<sub>2</sub>, . . . , T<sub>N</sub> (−11 ≤ T<sub>i</sub> ≤ 12 for i = 1, 2, . . . , N) indicating the time zones of the candidates.</p>

### 출력 

 <p>Output a line with an integer representing the minimum total time difference among all possible partitions of the set of candidates into couples.</p>

