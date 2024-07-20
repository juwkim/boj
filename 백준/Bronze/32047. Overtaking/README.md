# [Bronze I] Overtaking - 32047 

[문제 링크](https://www.acmicpc.net/problem/32047) 

### 성능 요약

메모리: 110784 KB, 시간: 144 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 7월 21일 00:35:08

### 문제 설명

<p>Two athletes run a long-distance race, but the race is different from usual athletics events. They run for a predetermined duration, and the one who runs longer will be the winner. At every minute after the start, the distances both runners ran in the previous one minute are recorded. You are expected to write a program that, given the record of a race, counts the number of overtakings by either runner during the race. You should assume that both runners keep constant paces for every one minute before their distances are recorded.</p>

<p>Here, the term <em>overtaking</em> stands for the event where the runner previously behind takes the lead. Note that, before overtaking, the two runners may run side by side for a while, during which neither takes the lead. Figure B-1 shows the times and the positions of two runners for the third dataset of Sample Input. The number of overtakings in this case is two.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 500px; height: 800px;"></p>

<p style="text-align: center;">Figure B-1: The third dataset of Sample Input</p>

### 입력 

 <p>The input consists of multiple datasets, each in the following format.</p>

<blockquote>
<p><i>n</i></p>

<p><i>a</i><sub>1</sub> ⋯ <i>a<sub>n</sub></i></p>

<p><i>b</i><sub>1</sub> ⋯ <i>b<sub>n</sub></i></p>
</blockquote>

<p><i>n</i> is an integer between 2 and 1000, inclusive. It represents the duration of the race in minutes. Each of <i>a<sub>k</sub></i> (<i>k</i> = 1, …, <i>n</i>) is an integer between 1 and 1000, inclusive. It represents the distance the first runner ran between <i>k</i> − 1 minutes and <i>k</i> minutes after the start of the race, in meters. Similarly, <i>b<sub>k</sub></i> (<i>k</i> = 1, …, <i>n</i>) represent the distances the second runner ran.</p>

<p>The end of the input is indicated by a line consisting of a zero. The number of datasets does not exceed 100.</p>

### 출력 

 <p>For each dataset, output the number of overtakings on a line.</p>

