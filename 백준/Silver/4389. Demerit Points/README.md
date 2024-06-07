# [Silver III] Demerit Points - 4389 

[문제 링크](https://www.acmicpc.net/problem/4389) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

많은 조건 분기, 구현, 파싱, 시뮬레이션, 문자열

### 제출 일자

2024년 6월 7일 22:28:00

### 문제 설명

<p>A province to our west, which shall remain nameless, but whose name does not start with A, B, or S, has a unique system for driver's license demerit and merit points. The system works (more or less) as follows.</p>

<p>A new driver starts with no merit or demerit points. When the driver is convicted of a driving offense, he or she is given between 2 and 15 demerit points, depending on the severity of the offense.</p>

<p>A merit point is given, to a maximum of five, for each interval of two years in which a driver has no offenses and no demerit points. Each merit point cancels up to two demerit points. If a subsequent offense occurs and the number of demerit points exceeds double the number of merit points, the number of demerit points is reduced by double the number of merit points, and the number of merit points is set to 0. If a subsequent offense occurs and the number of demerit points is less than or equal to double the number of merit points, the number of demerit points is reduced to 0, and the number of merit points is reduced by half the number of demerit points. Any fractional merit points are discarded.</p>

<p>Demerit points are reduced whenever a driver has one year free of any driving offense. This reduction decreases the number of demerits by half or by 2, whichever is more. Any fractional or negative demerit points are discarded. This reduction takes place on each anniversary of the most recent offense until no points remain.</p>

<p>If a new offense occurs on the same day as a demerit point reduction or merit point award, the reduction/award is done before the new demerit points are given.</p>

<p>Your job is to read a set of information records for a driver, and to print the number of merit or demerit points at any given time.</p>

### 입력 

 <p>The first line of input contains the date of issue of the license (yyyymmdd) Subsequent lines contain information on offenses, in chronological order. Each such line contains the offense date (yyyymmdd) and the number of points applied (an integer between 2 and 15).</p>

### 출력 

 <p>On the day the license is issued, and on every occasion that the number of merit or demerit points changes, output a line giving the date and the number of points, in the format below. Output terminates when 5 merit points are accumulated following the last offense.</p>

