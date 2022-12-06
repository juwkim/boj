# [Silver V] Infected Computer - 22614 

[문제 링크](https://www.acmicpc.net/problem/22614) 

### 성능 요약

메모리: 118160 KB, 시간: 196 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 정렬(sorting)

### 문제 설명

<p>Adam Ivan is working as a system administrator at Soy Group, Inc. He is now facing at a big trouble: a number of computers under his management have been infected by a computer virus. Unfortunately, anti-virus system in his company failed to detect this virus because it was very new.</p>

<p>Adam has identified the first computer infected by the virus and collected the records of all data packets sent within his network. He is now trying to identify which computers have been infected. A computer is infected when receiving any data packet from any infected computer. The computer is not infected, on the other hand, just by sending data packets to infected computers.</p>

<p>It seems almost impossible for him to list all infected computers by hand, because the size of the packet records is fairly large. So he asked you for help: write a program that can identify infected computers.</p>

### 입력 

 <p>The input consists of multiple datasets. Each dataset has the following format:</p>

<pre><i>N M</i>
<i>t</i><sub>1</sub> <i>s</i><sub>1</sub> <i>d</i><sub>1</sub>
<i>t</i><sub>2</sub> <i>s</i><sub>2</sub> <i>d</i><sub>2</sub>
...
<i>t<sub>M</sub> s<sub>M</sub> d<sub>M</sub></i></pre>

<p><i>N</i> is the number of computers; <i>M</i> is the number of data packets; <i>t<sub>i</sub></i> (1 ≤ <i>i</i> ≤ <i>M</i>) is the time when the <i>i</i>-th data packet is sent; <i>s<sub>i</sub></i> and <i>d<sub>i</sub></i> (1 ≤ <i>i</i> ≤ <i>M</i>) are the source and destination computers of the <i>i</i>-th data packet respectively. The first infected computer is indicated by the number 1; the other computers are indicated by unique numbers between 2 and <i>N</i>.</p>

<p>The input meets the following constraints: 0 < <i>N</i> ≤ 20000, 0 ≤ <i>M</i> ≤ 20000, and 0 ≤ <i>t<sub>i</sub></i> ≤ 10<sup>9</sup> for 1 ≤ <i>i</i> ≤ <i>N</i>; all <i>t<sub>i</sub></i> 's are different; and the source and destination of each packet are always different.</p>

<p>The last dataset is followed by a line containing two zeros. This line is not a part of any dataset and should not be processed.</p>

### 출력 

 <p>For each dataset, print the number of computers infected by the computer virus.</p>

