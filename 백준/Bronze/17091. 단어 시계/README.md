# [Bronze I] 단어 시계 - 17091 

[문제 링크](https://www.acmicpc.net/problem/17091) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

많은 조건 분기(case_work), 구현(implementation), 문자열(string)

### 문제 설명

<p>단어 시계는 시각을 단어를 이용해서 표현하는 시계이다. 다음은 몇 가지 예시이다.</p>

<ul>
	<li>5:00 → five o' clock</li>
	<li>5:01 → one minute past five</li>
	<li>5:10 → ten minutes past five</li>
	<li>5:15 → quarter past five</li>
	<li>5:28 → twenty eight minutes past five</li>
	<li>5:30 → half past five</li>
	<li>5:40 → twenty minutes to six</li>
	<li>5:45 → quarter to six</li>
	<li>5:47 → thirteen minutes to six</li>
</ul>

<p>분 = 0이면 "o' clock"을 사용하고, 1 ≤ 분 ≤ 30은 "past"를, 30 < 분이면 "to" 를 사용한다.</p>

<p>시각이 주어졌을 때, 단어 시계에서 사용하는 표현으로 출력해보자.</p>

### 입력 

 <p>첫째 줄에 시를 나타내는 h(1 ≤ h ≤ 12), 둘째 줄에 분을 나타내는 m(0 ≤ m < 60)이 주어진다.</p>

### 출력 

 <p>첫째 줄에 입력으로 주어진 시각을 단어 시계에서 사용하는 표현으로 출력한다.</p>

