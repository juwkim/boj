# [Silver I] Gift from the Goddess of Programming - 4938 

[문제 링크](https://www.acmicpc.net/problem/4938) 

### 성능 요약

메모리: 114244 KB, 시간: 140 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 6월 23일 03:49:00

### 문제 설명

<p>The goddess of programming is reviewing a thick logbook, which is a yearly record of visitors to her holy altar of programming. The logbook also records her visits at the altar.</p>

<p>The altar attracts programmers from all over the world because one visitor is chosen every year and endowed with a gift of miracle programming power by the goddess. The endowed programmer is chosen from those programmers who spent the longest time at the altar during the goddess’s presence. There have been enthusiastic visitors who spent very long time at the altar but failed to receive the gift because the goddess was absent during their visits.</p>

<p>Now, your mission is to write a program that finds how long the programmer to be endowed stayed at the altar during the goddess’s presence.</p>

### 입력 

 <p>The input is a sequence of datasets. The number of datasets is less than 100. Each dataset is formatted as follows.</p>

<pre>n
M<sub>1</sub>/D<sub>1</sub> h<sub>1</sub>:m<sub>1</sub> e<sub>1</sub> p<sub>1</sub>
M<sub>2</sub>/D<sub>2</sub> h<sub>2</sub>:m<sub>2</sub> e<sub>2</sub> p<sub>2</sub>
.
.
.
M<sub>n</sub>/D<sub>n</sub> h<sub>n</sub>:m<sub>n</sub> e<sub>n</sub> p<sub>n</sub></pre>

<p>The first line of a dataset contains a positive even integer, n ≤ 1000, which denotes the number of lines of the logbook. This line is followed by n lines of space-separated data, where M<sub>i</sub>/D<sub>i</sub> identifies the month and the day of the visit, h<sub>i</sub>:m<sub>i</sub> represents the time of either the entrance to or exit from the altar, e<sub>i</sub> is either I for entrance, or O for exit, and p<sub>i</sub> identifies the visitor.</p>

<p>All the lines in the logbook are formatted in a fixed-column format. Both the month and the day in the month are represented by two digits. Therefore April 1 is represented by 04/01 and not by 4/1. The time is described in the 24-hour system, taking two digits for the hour, followed by a colon and two digits for minutes, 09:13 for instance and not like 9:13. A programmer is identified by an ID, a unique number using three digits. The same format is used to indicate entrance and exit of the goddess, whose ID is 000.</p>

<p>All the lines in the logbook are sorted in ascending order with respect to date and time. Because the altar is closed at midnight, the altar is emptied at 00:00. You may assume that each time in the input is between 00:01 and 23:59, inclusive.</p>

<p>A programmer may leave the altar just after entering it. In this case, the entrance and exit time are the same and the length of such a visit is considered 0 minute. You may assume for such entrance and exit records, the line that corresponds to the entrance appears earlier in the input than the line that corresponds to the exit. You may assume that at least one programmer appears in the logbook.</p>

<p>The end of the input is indicated by a line containing a single zero.</p>

### 출력 

 <p>For each dataset, output the total sum of the blessed time of the endowed programmer. The blessed time of a programmer is the length of his/her stay at the altar during the presence of the goddess. The endowed programmer is the one whose total blessed time is the longest among all the programmers. The output should be represented in minutes. Note that the goddess of programming is not a programmer.</p>

