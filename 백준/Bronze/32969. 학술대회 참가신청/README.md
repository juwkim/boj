# [Bronze III] 학술대회 참가신청 - 32969 

[문제 링크](https://www.acmicpc.net/problem/32969) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

구현, 문자열

### 제출 일자

2024년 12월 16일 12:55:26

### 문제 설명

<p>한국정보기술진흥원에서는 매 여름과 겨울 학술대회가 개최된다.</p>

<p>2024 하계 학술대회에서는 "디지털인문학" 트랙과 "공공빅데이터" 트랙으로 2개의 트랙이 개설되었다.</p>

<p>진흥이는 이번 학술대회에 참가하고자 하는데 어느 트랙으로 참가해야 할지 몰라 여러분 들의 도움을 받고자 한다.</p>

<p>진흥이의 논문 주제가 주어질 때 어느 트랙으로 참가해야 할지 알려주자.</p>

<p>트랙의 판단 기준은 논문의 주제가 주어졌을 때 특정 단어가 포함되어 있다면 해당 트랙으로 참가하면 된다.</p>

<p>무조건 한 트랙으로만 결정될 수 있는 입력만 주어진다.</p>

<table class="table table-bordered">
	<thead>
		<tr>
			<th>트랙명</th>
			<th>판단 단어</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>디지털인문학</td>
			<td><code>social</code>, <code>history</code>, <code>language</code>, <code>literacy</code></td>
		</tr>
		<tr>
			<td>공공빅데이터</td>
			<td><code>bigdata</code>, <code>public</code>, <code>society</code></td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>입력 첫 줄에 100자 이하의 영어 대소문자와 공백으로 이루어진 논문 주제가 주어진다.</p>

### 출력 

 <p>판단 결과, 디지털인문학에 속하면 <code>digital humanities</code>를, 공공빅데이터에 속하면 <code>public bigdata</code>를 출력한다.</p>

