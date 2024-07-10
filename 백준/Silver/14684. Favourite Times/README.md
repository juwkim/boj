# [Silver III] Favourite Times - 14684 

[문제 링크](https://www.acmicpc.net/problem/14684) 

### 성능 요약

메모리: 108080 KB, 시간: 96 ms

### 분류

브루트포스 알고리즘, 수학

### 제출 일자

2024년 7월 11일 01:41:34

### 문제 설명

<p>Wendy has an LED clock radio, which is a 12-hour clock, displaying times from 12:00 to 11:59. The hours do not have leading zeros but minutes may have leading zeros, such as 2:07 or 11:03.</p>

<p>When looking at her LED clock radio, Wendy likes to spot arithmetic sequences in the digits. For example, the times 12:34 and 2:46 are some of her favourite times, since the digits form an arithmetic sequence.</p>

<p>A sequence of digits is an arithmetic sequence if each digit after the first digit is obtained by adding a constant common difference. For example, 1,2,3,4 is an arithmetic sequence with a common difference of 1, and 2,4,6 is an arithmetic sequence with a common difference of 2.</p>

<p>Suppose that we start looking at the clock at noon (that is, when it reads 12:00) and watch the clock for some number of minutes. How many instances are there such that the time displayed on the clock has the property that the digits form an arithmetic sequence?</p>

### 입력 

 <p>The input contains one integer D (0 ≤ D ≤ 1 000 000 000), which represents the duration that the clock is observed.</p>

<p>For 4 of the 15 available marks, D ≤ 10 000.</p>

### 출력 

 <p>Output the number of times that the clock displays a time where the digits form an arithmetic sequence starting from noon (12:00) and ending after D minutes have passed, possibly including the ending time.</p>

