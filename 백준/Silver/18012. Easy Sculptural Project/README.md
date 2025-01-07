# [Silver II] Easy Sculptural Project - 18012 

[문제 링크](https://www.acmicpc.net/problem/18012) 

### 성능 요약

메모리: 109540 KB, 시간: 92 ms

### 분류

자료 구조, 스택

### 제출 일자

2025년 1월 8일 08:28:43

### 문제 설명

<p>As a sculptor from his youth, da Vinci had designed many sculptures, however few of them had been brought to completion and only one of them, <em>The Virgin with the Laughing Child</em>, survived. It took da Vinci a long time and lots of materials to complete this sculpture.</p>

<p>Specifically, da Vinci planned to spend n days on the first phase of this project. Initially, da Vinci did not have any materials to sculpt. On each day, he would either take a day off (marked as ‘o’) and go to the market to buy 1 unit of materials, or work (marked as ‘w’) on the sculpture and consume 1 unit of materials. However, after creating the schedule, da Vinci noticed that it was not realistic – on some workdays, he might not have any material to work on at all, and finally he might end up with unused materials. To ensure smooth progress on this sculptural project, da Vinci decided to cancel some of his activities on certain days so that:</p>

<ol>
	<li>Starting with no material, da Vinci would have at least 1 unit of materials to sculpt on each workday.</li>
	<li>After n days, da Vinci would end up with no material left.</li>
	<li>The number of canceled activities is minimized. (da Vinci did not want to modify his original schedule too much!)</li>
</ol>

<p>Da Vinci would like to know the minimum number of activities that need to be canceled.</p>

### 입력 

 <p>The first line contains a number 1 ≤ K ≤ 10, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>Each data set is described by a single line containing a non-empty string S, describing da Vinci’s original schedule. The length of S is at most 1000 and it consists of ‘w’ and ‘o’ only. You can compute n by reading the length of S.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number.</p>

<p>Then output the minimum number of activities da Vinci needed to cancel to make the schedule feasible. It is possible that da Vinci did not need to cancel any activities.</p>

<p>Each data set should be followed by a blank line.</p>

