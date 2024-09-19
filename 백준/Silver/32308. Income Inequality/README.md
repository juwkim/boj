# [Silver V] Income Inequality - 32308 

[문제 링크](https://www.acmicpc.net/problem/32308) 

### 성능 요약

메모리: 273336 KB, 시간: 616 ms

### 분류

그리디 알고리즘, 구현, 시뮬레이션, 정렬

### 제출 일자

2024년 9월 19일 09:54:21

### 문제 설명

<p>According to Wikipedia, in 2021, the top 1% of households own 32.3% of the wealth in the United States. More generally, for any given percentage x, we could look at the data and state that the top x% of households own y% of the wealth.</p>

<p>It's obvious that for all societies with some inequality, it is always the case that y > x, except for x = 0 and x = 100. Of all possible choices for x, what is the maximum value of y – x?</p>

<p>Given the incomes of all people in a society, determine the maximum value of y – x where the top x% of the people have y% of the society's wealth.</p>

### 입력 

 <p>The first input line contains a single integer, n (2 ≤ n ≤ 10<sup>6</sup>), indicating the number of people in the society.</p>

<p>The second input line contains n integers; each integer, m (1 ≤ m ≤ 10<sup>12</sup>), provides the wealth of a household in the society. Please note that the income values are not necessarily distinct.</p>

### 출력 

 <p>Print the maximum possible value of y – x, where the top x% of households in the society own y% of the society's wealth. Any answer within an absolute or relative error of 10<sup>-6</sup> will be accepted.</p>

