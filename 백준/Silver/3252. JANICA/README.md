# [Silver II] JANICA - 3252 

[문제 링크](https://www.acmicpc.net/problem/3252) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

사칙연산, 구현, 수학, 시뮬레이션, 정렬

### 제출 일자

2025년 1월 13일 10:48:58

### 문제 설명

<p>Watching alpine skiing on TV can be really boring sometimes. Fortunately, it can happen that your TV operator doesn’t show all the information about the race and then you have to do some computation to determine the winner yourself.</p>

<p>Here are some details about a race: Each race consists of two rounds. In first round, N skiers numbered from 1 to N, race starting in that order.</p>

<p>When the first skier in the first round (numbered with 1) finishes the race we are given the time he/she needed to complete the course. For every following skier we are given time difference between his/her time and the time of the skier currently leading the race.</p>

<p>Only the best M skiers qualify for the second round and they start the second round ordered by time from the first round decreasingly (last skier qualified for the second round starts first and the leader after the first round start last).</p>

<p>In the second round we are given the total time (first and second round added) of the first skier racing, and then for every following skier we are given the time difference between his/her total time and the total time of the skier currently leading the race.</p>

<p>Write a program that will determine medal winners after the race has finished. You can assume that it can never happen that two skiers have same time (after the first round or after both rounds).</p>

<p>Time for any race will be between 10 and 300 seconds. All times will be real numbers with at most two decimal digits. </p>

### 입력 

 <p>The first line of the input file contains two integers N and M, separated by a single blank character, 3 ≤ M ≤ N ≤ 100.</p>

<p>The following line contains the time for the first skier in the first round, and the following N-1 lines contain the described time differences.</p>

<p>The following line contains the time for the first skier in the second round, and the following M-1 lines contain the described time differences. </p>

### 출력 

 <p>The first line of the output file should contain the number of the skier winning the gold medal, second line the number of skier winning the silver medal, and the third line the number of skier winning the bronze medal.</p>

