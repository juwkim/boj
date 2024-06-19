# [Silver III] Programmer, Rank Thyself - 4644 

[문제 링크](https://www.acmicpc.net/problem/4644) 

### 성능 요약

메모리: 108080 KB, 시간: 96 ms

### 분류

구현, 수학, 정렬

### 제출 일자

2024년 6월 19일 17:32:21

### 문제 설명

<p>Implement a ranking program similar to the one used for this programming contest.</p>

### 입력 

 <p>The input file contains one or more contests followed by a line containing only zero that signals the end of the file. Each contest begins with a line containing a positive integer c no greater than 20 indicating the number of teams in the contest, and is followed by c lines that contain a team name and the solution times for seven problems, separated by spaces. Team names consist of between one and ten letters. All team names within a contest are unique. Times are nonnegative integers no greater than 500.</p>

<p>As described in the Notes to Teams, teams are ranked first by greatest number of problems solved, then by least total time, then by least geometric mean of all nonzero times. Teams that are still tied are given the same numeric ranking and are listed in alphabetical order, using case-sensitive string comparison. The numeric ranking for a team is always one more than the number of teams ranked ahead of (not tied with) that team. For this problem all geometric means will be rounded to an integer as described below, and only the rounded value will be used when computing rankings and displaying results.</p>

<p>If all times are zero, then the geometric mean is also zero. Otherwise, if there are n nonzero times t<sub>1</sub>, ..., t<sub>n</sub>, then the geometric mean is defined to be</p>

<p>exp ((ln t<sub>1</sub> + ln t<sub>2</sub> + ... + ln t<sub>n</sub>) / n)</p>

<p>where exp x means e<sup>x</sup> and ln x means the natural logarithm of x. (There are other mathematically equivalent definitions of the geometric mean, but they may produce slightly different answers due to roundoff and/or overflow problems. Use this definition to get the same answers as the judges.) After computing the geometric mean, round it to an integer by adding 0.5 and truncating any fractional digits. (C/C++ and Java automatically truncate fractions when casting a floating-point type to an integral type. In Pascal use the trunc function.)</p>

### 출력 

 <p>For each contest you must output the rankings in a table. All tables will have the same width, with the length equal to the number of teams entered in the contest. Use the exact format shown in the examples. Each contest has a numbered header followed by a table with one team entry per line. Each entry contains the ranking, team name, problems solved, total time, geometric mean, and then the individual solution times in the same order they appeared in the input. In the first example all values completely fill their fields. In general you may need to pad values with spaces (never tabs) so that they have the correct field width. The team name is left-justified, and all other fields are right-justified. The ranking always has two digits, including a leading zero if necessary. Spaces will never appear at the beginning or end of lines.</p>

