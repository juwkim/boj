# [Bronze II] Eligibility - 10410 

[문제 링크](https://www.acmicpc.net/problem/10410) 

### 성능 요약

메모리: 28776 KB, 시간: 148 ms

### 분류

구현(implementation)

### 문제 설명

<p>Every year, students across the world participate in the ACM ICPC. In order to participate in this contest, a student must be eligible to compete. In this problem, you will be given information about students and you will write a program to determine their eligibility to participate in the ICPC.</p>

<p>We will start by assuming that each student meets the “Basic Requirements” as specified in the ICPC rules—the student is willing to compete at the World Finals, is a registered student with at least half-time load, competes for only one institution in a contest year, and has not competed in two world finals or five regional contests.</p>

<p>The rules to decide if a student is eligible to compete in the contest year 2014–2015 are as follows:</p>

<ol>
	<li>if the student first began post-secondary studies in 2010 or later, the student is eligible;</li>
	<li>if the student is born in 1991 or later, the student is eligible;</li>
	<li>if none of the above applies, and the student has completed more than an equivalent of 8 semesters of full-time study, the student is ineligible;</li>
	<li>if none of the above applies, the coach may petition for an extension of eligibility by providing the student’s academic and work history.</li>
</ol>

<p>For “equivalent of 8 semesters of full-time study,” we consider each semester of full-time study to be equivalent to a student completing 5 courses. Thus, a student who has completed 41 courses or more is considered to have more than 8 semesters of full-time study.</p>

### 입력 

 <p>The input consists of a number of cases. The first line contains a positive integer, indicating the number of cases to follow. Each of the cases is specified in one line in the following format</p>

<pre>name YYYY/MM/DD YYYY/MM/DD courses</pre>

<p>where name is the name of the student (up to 30 alphabetic characters), the first date given is the date the student first began post-secondary studies, and the second date given is the student’s date of birth. All dates are given in the format above with 4-digit year and 2-digit month and day. courses is a non-negative integer indicating the number of courses that the student has completed.</p>

<p>There are at most 1 000 cases.</p>

### 출력 

 <p>For each line of output, print the student’s name, followed by a space, followed by one of the strings eligible, ineligible, and coach petitions as appropriate.</p>

