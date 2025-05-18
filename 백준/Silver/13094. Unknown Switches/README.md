# [Silver I] Unknown Switches - 13094 

[문제 링크](https://www.acmicpc.net/problem/13094) 

### 성능 요약

메모리: 186848 KB, 시간: 580 ms

### 분류

비트마스킹, 구현, 수학, 시뮬레이션

### 제출 일자

2025년 5월 18일 15:36:06

### 문제 설명

<p>In the headquarter building of ICPC (International Company of Plugs & Connectors), there are M light bulbs and they are controlled by N switches. Each light bulb can be turned on or off by exactly one switch. Each switch may control multiple light bulbs. When you operate a switch, all the light bulbs controlled by the switch change their states. You lost the table that recorded the correspondence between the switches and the light bulbs, and want to restore it.</p>

<p>You decided to restore the correspondence by the following procedure.</p>

<ul>
	<li>At first, every switch is off and every light bulb is off.</li>
	<li>You operate some switches represented by S<sub>1</sub>.</li>
	<li>You check the states of the light bulbs represented by B<sub>1</sub>.</li>
	<li>You operate some switches represented by S<sub>2</sub>.</li>
	<li>You check the states of the light bulbs represented by B<sub>2</sub>.</li>
	<li>...</li>
	<li>You operate some switches represented by S<sub>Q</sub>.</li>
	<li>You check the states of the light bulbs represented by B<sub>Q</sub>.</li>
	<li>After you operate some switches and check the states of the light bulbs, the states of the switches and the light bulbs are kept for next operations.</li>
</ul>

<p>Can you restore the correspondence between the switches and the light bulbs using the information about the switches you have operated and the states of the light bulbs you have checked?</p>

### 입력 

 <p>The input consists of multiple datasets. The number of dataset is no more than 50 and the file size is no more than 10MB. Each dataset is formatted as follows.</p>

<pre>N M Q
S<sub>1</sub> B<sub>1</sub>
:
:
S<sub>Q</sub> B<sub>Q</sub></pre>

<p>The first line of each dataset contains three integers N (1≤N≤36), M (1≤M≤1,000), Q (0≤Q≤1,000), which denote the number of switches, the number of light bulbs and the number of operations respectively. The following Q lines describe the information about the switches you have operated and the states of the light bulbs you have checked. The i-th of them contains two strings S<sub>i</sub> and B<sub>i</sub> of lengths N and M respectively. Each S<sub>i</sub> denotes the set of the switches you have operated: S<sub>ij</sub> is either 0 or 1, which denotes the j-th switch is not operated or operated respectively. Each B<sub>i</sub> denotes the states of the light bulbs: B<sub>ij</sub> is either 0 or 1, which denotes the j-th light bulb is off or on respectively.</p>

<p>You can assume that there exists a correspondence between the switches and the light bulbs which is consistent with the given information.</p>

<p>The end of input is indicated by a line containing three zeros.</p>

### 출력 

 <p>For each dataset, output the correspondence between the switches and the light bulbs consisting of M numbers written in base-36. In the base-36 system for this problem, the values 0-9 and 10-35 are represented by the characters '0'-'9' and 'A'-'Z' respectively. The i-th character of the correspondence means the number of the switch controlling the i-th light bulb. If you cannot determine which switch controls the i-th light bulb, output '?' as the i-th character instead of the number of a switch.</p>

