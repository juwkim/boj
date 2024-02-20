# [Silver III] Rain Gauge - 25936 

[문제 링크](https://www.acmicpc.net/problem/25936) 

### 성능 요약

메모리: 110996 KB, 시간: 656 ms

### 분류

기하학, 구현

### 제출 일자

2024년 2월 21일 02:23:41

### 문제 설명

<p><img alt="" src="https://upload.acmicpc.net/38788f42-3cce-419f-adea-c70a8b74b5a7/-/preview/" style="width: 152px; height: 152px; float: right;">When going to your internship you got a nice apartment with a skylight. However, one crazy party later and you now have a square-shaped hole where your skylight used to be. Rather than telling the landlord, you decided you would “fix” it by putting a circular pot to collect the water but, as the saying goes, round peg square hole. You need to determine how much of the square the circle covers to help you determine if you should buy a larger pot. Don’t worry about the area not covered; you can do multiplication and subtraction easily in your head.</p>

<p>Given the radius of a circular pot and the length of the square skylight, calculate the amount of skylight rain area covered by the pot assuming the two shapes have the same center (i.e., are coaxial) with respect to the direction rain falls from (up). In other words, the center of the square will be directly above the center of the circle. See the picture for an example; let up be the direction from above the page, while the dotted square is the skylight and the solid circle is the pot to collect water.</p>

### 입력 

 <p>The first input line contains a positive integer, n, indicating the number of scenarios to check. Each of the following n lines contains a pair of integers, s, r (1 ≤ s ≤ 100, 1 ≤ r ≤ 100), which represents the length of the side of the skylight and the radius of the pot, respectively.</p>

### 출력 

 <p>For each scenario, output a single decimal representing the area under the skylight that is covered by the pot. Round the answers to two decimal places (e.g., 1.234 rounds to 1.23 and 1.235 rounds to 1.24). For this problem, use 3.14159265358979 as the value of pi.</p>

