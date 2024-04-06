# [Silver III] Zombdar - 9434 

[문제 링크](https://www.acmicpc.net/problem/9434) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

파싱, 문자열

### 제출 일자

2024년 4월 7일 08:37:45

### 문제 설명

<p>You are reading data from a zombie sensor. The sensor scans the area to obtain the number of zombies in the immediate area. The zombie sensor normally writes log entries in the form of "Zombies: <integer>;" or "No Zombies;" to its buffer as it performs scans, but it may also write "RUN;" when the sensor is overloaded. These are the only values that will be written to the buffer.</p>

<p>The zombie sensor's serial port emits a line containing whatever data is in its buffer every second, regardless of whether the buffer contains a complete log entry, or even multiple entries.</p>

<p>A valid sequence of log entries may be:</p>

<pre>Zombies: 5;
Zombies: 1;
No Zombies;
Zombies: 70;
RUN;
RUN;
RUN;</pre>

<p>But the sensor's serial port may emit:</p>

<pre>Zom
bies:
 5;Zombies: 1
;
No Zombies;
Zombies 70;
RUN;
RUN;RUN;Zo</pre>

<p>It is imperative to process the serial port data correctly if you are to survive.</p>

### 입력 

 <p>The first line of input contains the number of data sets, N (1 <= N <= 50). For each data set, the input contains the raw data emitted by the zombie sensor's serial port (see above for details) followed by a line containing only the string "END OF CASE". Since data is emitted by the zombie sensor's serial port once per second, the first line of input is read after 1 second, the 2nd line after 2 seconds, and so on.</p>

### 출력 

 <p>For each complete log entry, you should output a line containing "timestamp: log_entry", where timestamp is the number of seconds elapsed between the start of the data set and the time at which the entry was completely parsed.</p>

