# [Silver V] High Tide, Low Tide - 14687 

[문제 링크](https://www.acmicpc.net/problem/14687) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현(implementation), 정렬(sorting), 두 포인터(two_pointer)

### 문제 설명

<p>Joe Coder is camping near the Bay of Fundy between Nova Scotia and New Brunswick. When he arrived at the bay, he was told that the difference in height between high tide and low tide at the Bay of Fundy was the largest tidal difference in the world. Ever the skeptic, Joe decided to verify this. He chose a reference point and, after learning from the radio when the tides were highest and lowest, he went with a boat to his reference point and measured the depth of the water. Unfortunately, on the last day of his trip, a strong wind scattered his measurements.</p>

<p>Joe has recovered all of his measurements, but they may not be in their original order. Luckily, he remembers some things about his measurements:</p>

<ul>
	<li>He started measuring water levels at a low tide, his second measurement was of the water level at high tide, and after that the measurements continued to alternate between low and high tides.</li>
	<li>All high tide measurements were higher than all low tide measurements.</li>
	<li>Joe noticed that as time passed, the high tides only became higher and the low tides only became lower.</li>
</ul>

<p>Given Joe’s measurements in no particular order, you must reconstruct the correct order in which the measurements were taken.</p>

### 입력 

 <p>The first line contains the integer N (1 ≤ N ≤ 100). The next line contains N distinct spaceseparated positive integers, where each integer is at most 1 000 000.</p>

### 출력 

 <p>Output the N integers in the unique order that Joe originally took the measurements.</p>

