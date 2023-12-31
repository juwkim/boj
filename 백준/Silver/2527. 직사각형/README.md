# [Silver I] 직사각형 - 2527 

[문제 링크](https://www.acmicpc.net/problem/2527) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

많은 조건 분기, 기하학

### 제출 일자

2024년 1월 1일 05:57:25

### 문제 설명

<p>2차원 격자공간에 두 개의 꼭짓점 좌표로 표현되는 직사각형이 있다. 직사각형은 아래와 같이 왼쪽 아래 꼭짓점 좌표 (x, y)와 오른쪽 위 꼭짓점 좌표 (p, q)로 주어진다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/42dae0fc-0b99-4894-9efb-ecbe4f82ddc0/-/preview/" style="width: 250px; height: 213px;"></p>

<p>이 문제에서 모든 직사각형은 두 꼭짓점의 좌표를 나타내는 4개의 정수 x y p q 로 표현된다. 단 항상 x<p, y<q 이다. 예를 들어 위 그림에 제시된 직사각형이라면 아래와 같이 표현된다.</p>

<p style="text-align: center;"><strong>3 2 9 8</strong></p>

<p>두 개의 직사각형은 그 겹치는 부분의 특성에 따라 다음 4가지 경우로 분류될 수 있다. </p>

<p>먼저 두 직사각형의 겹치는 부분이 직사각형인 경우이다. 아래 그림(a)는 공통부분이 직사각형인 경우의 3가지 예를 보여준다,</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/fa199f60-888a-4cbc-ac44-c50bbb3edf10/-/preview/" style="width: 267px; height: 92px;"></p>

<p style="text-align: center;">그림 (a)</p>

<p>또는 겹치는 부분이 아래 그림 (b)와 같이 선분이 될 수도 있고, 그림 (c)와 같이 점도 될 수 있다. </p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/18c85091-ae8c-4380-88b9-5c25026f3af6/-/preview/" style="width: 83px; height: 97px;"></p>

<p style="text-align: center;">그림 (b)</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/9cf6a020-9a7d-4638-afb8-f284ca588b8b/-/preview/" style="width: 106px; height: 97px;"></p>

<p style="text-align: center;">그림 (c)</p>

<p>마지막으로 아래 그림 (d)와 같이 공통부분 없이 두 직사각형이 완전히 분리된 경우도 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/f4d434ee-dee0-42a7-a5b6-a2c12b248fb2/-/preview/" style="width: 146px; height: 68px;"></p>

<p style="text-align: center;">그림 (d)</p>

<p>여러분은 두 직사각형의 겹치는 부분이 직사각형인지, 선분인지, 점인지, 아니면 전혀 없는 지를 판별해서 해당되는 코드 문자를 출력해야 한다. </p>

<table class="table table-bordered table-center-20 th-center td-center">
	<thead>
		<tr>
			<th>공통부분의 특성</th>
			<th>코드 문자</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>직사각형</td>
			<td>a</td>
		</tr>
		<tr>
			<td>선분</td>
			<td>b</td>
		</tr>
		<tr>
			<td>점</td>
			<td>c</td>
		</tr>
		<tr>
			<td>공통부분이 없음</td>
			<td>d</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>4개의 줄로 이루어져 있다. 각 줄에는 8개의 정수가 하나의 공백을 두고 나타나는데, 첫 4개의 정수는 첫 번째 직사각형을, 나머지 4개의 정수는 두 번째 직사각형을 각각 나타낸다. 단 입력 직사각형의 좌표 값은 1이상 50,000 이하의 정수로 제한된다. </p>

### 출력 

 <p>4개의 각 줄에 주어진 두 직사각형의 공통부분을 조사해서 해당하는 코드 문자를 출력파일의 첫 4개의 줄에 각각 차례대로 출력해야 한다.</p>

