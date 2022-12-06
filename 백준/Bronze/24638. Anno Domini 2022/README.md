# [Bronze II] Anno Domini 2022 - 24638 

[문제 링크](https://www.acmicpc.net/problem/24638) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 많은 조건 분기(case_work), 수학(math), 문자열(string)

### 문제 설명

<p>Soon we will celebrate New Year 2022, but what does this number mean? As you possibly know, this dating system was invented in AD 525 by Dionysius Exiguus. He chose the birth of Jesus Christ as the starting point of the Years of Our Lord (Anno Domini in Latin, AD for short). All the years before that were counted backwards as years Before Christ (BC for short). </p>

<p>An interesting detail of this dating system is that there is no year 0 --- year 1 BC is immediately followed by AD 1. Because of that, sometimes it is quite tricky to find time difference between two dates if these dates belong to two different eras.</p>

<p>To simplify this task, please write a program that computes how many years passed between January 1st of two years given in the input.</p>

### 입력 

 <p>Two years are specified on two sequential input lines. Each year is specified in one of two forms:</p>

<ol>
	<li>as letters <code>AD</code>, followed by a space and a positive integer without leading zeroes in range $1..9999$;</li>
	<li>as a positive integer without leading zeroes in range $1..9999$, followed by a space and letters <code>BC</code>.</li>
</ol>

<p>The years may be specified in arbitrary order --- the earlier year is not necessarily given first.</p>

### 출력 

 <p>The only line of the output must contain one integer: the number of years that passed between January 1st of the earlier year and January 1st of the later year.</p>

