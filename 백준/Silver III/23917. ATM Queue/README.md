# [Silver III] ATM Queue - 23917 

[문제 링크](https://www.acmicpc.net/problem/23917) 

### 성능 요약

메모리: 225220 KB, 시간: 1272 ms

### 분류

애드 혹, 수학, 정렬

### 제출 일자

2024년 2월 15일 09:06:10

### 문제 설명

<p>There are <b>N</b> people numbered from 1 to <b>N</b>, standing in a queue to withdraw money from an ATM. The queue is formed in ascending order of their number. The person numbered <b>i</b> wants to withdraw amount <b>A<sub>i</sub></b>. The maximum amount a person can withdraw at a time is <b>X</b>. If they need more money than <b>X</b>, they need to go stand at the end of the queue and wait for their turn in line. A person leaves the queue once they have withdrawn the required amount.</p>

<p>You need to find the order in which all the people leave the queue.</p>

### 입력 

 <p>The first line of the input gives the number of test cases <b>T</b>. <b>T</b> test cases follow.</p>

<p>The first line of each test case gives two space separated integers: the number of people standing in the queue, <b>N</b> and the maximum amount <b>X</b> that can be withdrawn in one turn.</p>

<p>The next line contains <b>N</b> space separated integers <b>A<sub>i</sub></b>.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the space separated list of integers that denote the order in which the people leave the queue.</p>

