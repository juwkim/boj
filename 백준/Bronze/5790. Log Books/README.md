# [Bronze II] Log Books - 5790 

[문제 링크](https://www.acmicpc.net/problem/5790) 

### 성능 요약

메모리: 110712 KB, 시간: 108 ms

### 분류

수학, 문자열

### 제출 일자

2025년 1월 8일 17:37:35

### 문제 설명

<p>Learner drivers need to complete 50 hours of supervised driving with at least 10 hours, or more, of night driving included in the total amount. Each learner must keep a log book of their supervised driving experience with each entry containing the starting and finishing time for each driving experience.</p>

<p>Poirot-the-inspector has been given the duty of checking the log books and verifying that the driving times add up to the required values and that no single driving experience exceeds 2 hours. If more than, or equal to, half the length of one driving experience occurs during the night (before sunrise or after sunset), then the whole time counts towards night driving. For example, driving from 04:50 to 06:10 on a day when sunrise is at 05:30 counts as night driving. </p>

<p>However, Poirot has never been good with numbers and he is requesting assistance with this duty. Your task is to write a program that reads a learner's log book and checks that the required driving times have been completed without violating the 2 hour length rule.</p>

### 입력 

 <p>The input consists of a number of test cases. The description for each test case starts with an integer N, on a line by itself, that represents the number of entries in one log book. 25 < N < 300. Each of the following N lines contains a record of one driving experience with four times representing sunrise, sunset, and the starting and finishing time in that order. The starting time is strictly smaller than the finishing time. A single space separates the times and each time has a value between 00:00 (midnight) and 23:59 (one minute to midnight), inclusive. A line with a zero by itself terminates the input and is not to be processed.</p>

### 출력 

 <p>The output for each log book consists of the string PASS if the required driving times have been completed without violating the 2 hour length rule. Otherwise, print the string NON.</p>

