# [Bronze I] Hot Hike - 18025 

[문제 링크](https://www.acmicpc.net/problem/18025) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>In order to pass time during your vacation, you decided to go on a hike to visit a scenic lake up in the mountains. Hiking to the lake will take you a full day, then you will stay there for a day to rest and enjoy the scenery, and then spend another day hiking home, for a total of three days. However, the accursed weather this summer is ridiculously warm and sunny, and since severe dehydration is not at the top of your priority list you want to schedule the three-day trip during some days where the two hiking days are the least warm. In particular you want to minimize the maximum temperature during the two hiking days.</p>

<p>Given the current forecast of daily maximum temperatures during your vacation, what are the best days for your trip?</p>

### 입력 

 <p>The first line of input contains an integer n (3 ≤ n ≤ 50), the length of your vacation in days. Then follows a line containing n integers t<sub>1</sub>, t<sub>2</sub>, . . . , t<sub>n</sub> (−20 ≤ t<sub>i</sub> ≤ 40), where t<sub>i</sub> is the temperature forecast for the i’th day of your vacation.</p>

### 출력 

 <p>Output two integers d and t, where d is the best day to start your trip, and t is the resulting maximum temperature during the two hiking days. If there are many choices of d that minimize the value of t, then output the smallest such d.</p>

