# [Bronze I] When Can We Meet? - 22810 

[문제 링크](https://www.acmicpc.net/problem/22810) 

### 성능 요약

메모리: 45092 KB, 시간: 252 ms

### 분류

구현(implementation)

### 문제 설명

<p>The ICPC committee would like to have its meeting as soon as possible to address every little issue of the next contest. However, members of the committee are so busy maniacally developing (possibly useless) programs that it is very difficult to arrange their schedules for the meeting. So, in order to settle the meeting date, the chairperson requested every member to send back a list of convenient dates by E-mail. Your mission is to help the chairperson, who is now dedicated to other issues of the contest, by writing a program that chooses the best date from the submitted lists. Your program should find the date convenient for the most members. If there is more than one such day, the earliest is the best.</p>

### 입력 

 <p>The input has multiple data sets, each starting with a line containing the number of committee members and the quorum of the meeting.</p>

<pre><i>N Q</i>
</pre>

<p>Here, <i>N</i>, meaning the size of the committee, and <i>Q</i> meaning the quorum, are positive integers. <i>N</i> is less than 50, and, of course, <i>Q</i> is less than or equal to <i>N.</i></p>

<p><i>N</i> lines follow, each describing convenient dates for a committee member in the following format.</p>

<pre><i>M Date</i><sub>1</sub> <i>Date</i><sub>2</sub> ... <i>Date<sub>M</sub></i>
</pre>

<p>Here, <i>M</i> means the number of convenient dates for the member, which is an integer greater than or equal to zero. The remaining items in the line are his/her dates of convenience, which are positive integers less than 100, that is, 1 means tomorrow, 2 means the day after tomorrow, and so on. They are in ascending order without any repetition and separated by a space character. Lines have neither leading nor trailing spaces.</p>

<p>A line containing two zeros indicates the end of the input.</p>

### 출력 

 <p>For each data set, print a single line containing the date number convenient for the largest number of committee members. If there is more than one such date, print the earliest. However, if no dates are convenient for more than or equal to the quorum number of members, print 0 instead.</p>

