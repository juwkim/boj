# [Silver IV] Dial Key - 22637 

[문제 링크](https://www.acmicpc.net/problem/22637) 

### 성능 요약

메모리: 125672 KB, 시간: 152 ms

### 분류

유클리드 호제법, 수학, 정수론

### 제출 일자

2023년 12월 8일 03:25:14

### 문제 설명

<p>You are a secret agent from the Intelligence Center of Peacemaking Committee. You've just sneaked into a secret laboratory of an evil company, Automated Crime Machines.</p>

<p>Your mission is to get a confidential document kept in the laboratory. To reach the document, you need to unlock the door to the safe where it is kept. You have to unlock the door in a correct way and with a great care; otherwise an alarm would ring and you would be caught by the secret police.</p>

<p>The lock has a circular dial with <i>N</i> lights around it and a hand pointing to one of them. The lock also has <i>M</i> buttons to control the hand. Each button has a number <i>L<sub>i</sub></i> printed on it.</p>

<p>Initially, all the lights around the dial are turned off. When the <i>i</i>-th button is pressed, the hand revolves clockwise by <i>L<sub>i</sub></i> lights, and the pointed light is turned on. You are allowed to press the buttons exactly <i>N</i> times. The lock opens only when you make all the lights turned on.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/7e043edb-e4f1-42a9-8663-8e2722e54c55/-/preview/" style="width: 446px; height: 340px;"></p>

<p>For example, in the case with <i>N</i> = 6, <i>M</i> = 2, <i>L</i><sub>1</sub> = 2 and <i>L</i><sub>2</sub> = 5, you can unlock the door by pressing buttons 2, 2, 2, 5, 2 and 2 in this order.</p>

<p>There are a number of doors in the laboratory, and some of them don’t seem to be unlockable. Figure out which lock can be opened, given the values <i>N</i>, <i>M</i>, and <i>L<sub>i</sub></i>'s.</p>

### 입력 

 <p>The input starts with a line containing two integers, which represent <i>N</i> and <i>M</i> respectively. <i>M</i> lines follow, each of which contains an integer representing <i>L<sub>i</sub></i>.</p>

<p>It is guaranteed that 1 ≤ <i>N</i> ≤ 10<sup>9</sup>, 1 ≤ <i>M</i> ≤ 10<sup>5</sup>, and 1 ≤ <i>L<sub>i</sub></i> ≤ <i>N</i> for each <i>i</i> = 1, 2, ... <i>N</i>.</p>

### 출력 

 <p>Output a line with "Yes" (without quotes) if the lock can be opened, and "No" otherwise.</p>

