# [Bronze III] Counting Peaks of Infection - 25527 

[문제 링크](https://www.acmicpc.net/problem/25527) 

### 성능 요약

메모리: 114984 KB, 시간: 136 ms

### 분류

구현(implementation)

### 문제 설명

<p>For the new infectious disease, COVID-99, numbers of new positive cases of PCR tests conducted in the city are reported daily. You are requested by the municipal public relations department to write a program that counts the number of the peaks so far of the positive cases.</p>

<p>Here, the number of peaks is the number of days on which the number of positive cases reported is more than both of the day before and the next day.</p>

<p>As the PCR tests started before the disease started spreading in the city, the number of positive cases is zero on the first day. The last reported day is not counted as a peak. No two consecutive days have the same number of positive cases.</p>

<p style="text-align: center;"><img alt="" src=""></p>

<p style="text-align: center;">Figure A-1: Numbers of positive cases of the last dataset in Sample Input. Red circles indicate the peaks.</p>

### 입력 

 <p>The input consists of multiple datasets. Each dataset is in the following format.</p>

<pre><var>n</var>
<var>v</var><sub>1</sub> ... <var>v</var><sub><var>n</var></sub></pre>

<p><var>n</var> is the number of days on which the numbers of positive cases are reported (3 ≤ <var>n</var> ≤ 1000). <var>v</var><sub><var>i</var></sub> is the number of positive cases on the <var>i</var>-th day, an integer between zero and 1000, inclusive. Note that <var>v</var><sub>1</sub> is zero, and <var>v</var><sub><var>i</var></sub> ≠ <var>v</var><sub><var>i</var>+1</sub> for 1 ≤ <var>i</var> < <var>n</var>, as stated above.</p>

<p>The end of the input is indicated by a line containing a zero. The input consists of at most 100 datasets.</p>

### 출력 

 <p>For each dataset, output the number of peaks in a line.</p>

