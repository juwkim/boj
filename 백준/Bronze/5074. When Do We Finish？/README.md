# [Bronze III] When Do We Finish? - 5074 

[문제 링크](https://www.acmicpc.net/problem/5074) 

### 성능 요약

메모리: 121220 KB, 시간: 104 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>In this problem you are given the starting time of an event and its duration. All you have to do is to say when the event ends.</p>

### 입력 

 <p>Input consists of a number of lines, each line representing an event. The last line of input will be 00:00 00:00 – do not process this line. Each event is represented by two times separated by a space. Each time is in the format hh:mm. The first time is the start time of the event, the second time is its duration. For the start time, a legal time using a 24 hour clock will be supplied. For the duration, the minutes will be from 0 to 59 inclusive, but the hours may be from 0 to 96 inclusive.</p>

### 출력 

 <p>For each line of input, produce one line of output containing a single time, also in the format hh:mm, being the end time of the event as a legal 24 hour time. If this time is not on the same day as the start time, the time will be in the format hh:mm +n, where n is the number of days after the starting day.</p>

