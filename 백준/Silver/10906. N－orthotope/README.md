# [Silver I] N-orthotope - 10906 

[문제 링크](https://www.acmicpc.net/problem/10906) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

애드 혹, 기하학, 4차원 이상의 기하학

### 제출 일자

2025년 4월 17일 22:36:02

### 문제 설명

<p>축에 평행한 N-orthotope란 다음에 속하는 어떤 N 차원 점들의 집합이다.</p>

<p style="text-align: center;">[s<sub>1</sub>, e<sub>1</sub>] × [s<sub>2</sub>, e<sub>2</sub>] × ... × [s<sub>N</sub>, e<sub>N</sub>] (s<sub>i</sub> < e<sub>i</sub>)<br>
(즉, N차원 점 (x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>)의 각 x<sub>i</sub> 가 s<sub>i</sub> ≤ x<sub>i</sub> ≤ e<sub>i</sub> 인 점들의 집합이다.)</p>

<ul>
	<li>N = 0인 경우는 특별히 0차원의 점이라고 정의하자. </li>
	<li>N = 1인 경우는 1차원에서 어느 선분을 의미한다. </li>
	<li>N = 2인 경우는 2차원에서 축에 평행한 어느 직사각형 형태의 영역이 된다. </li>
	<li>N = 3인 경우는 3차원에서 축에 평행한 어느 직육면체 형태의 영역이 된다. </li>
	<li>...</li>
</ul>

<p>조금 더 일반화하면,</p>

<p style="text-align: center;">[s<sub>1</sub>, e<sub>1</sub>] × [s<sub>2</sub>, e<sub>2</sub>] × ... × [s<sub>K</sub>, e<sub>K</sub>] (s<sub>i</sub> ≤ ei)</p>

<p>를 만족하는 점들은 s<sub>i</sub> < e<sub>i</sub>를 만족하는 i의 개수가 N개라면 축에 평행한 N-orthotope가 된다. 앞으로 '평행한'을 생략할 것이지만 앞으로 등장하는 orthotope도 평행한 orthotope라고 생각하면 된다.</p>

<p>어떤 N에 대해 두 개의 N-orthotope가 주어져 있다고 하자. 이때 두 영역에 동시에 속하는 점들이 있다면, 이 점들은 축에 M-orthotope가 된다. 이때 M이 무엇인지 구하는 프로그램을 작성하라. 예를 들어 2-orthotope의 경우 아래의 네 가지 경우가 있을 수 있다.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/10906/ex.png"></p>

<ul>
	<li>A는 두 2-orthotope의 공통된 영역이 똑같이 2-orthotope가 되는 경우이다. </li>
	<li>B는 두 2-orthotope의 공통된 영역이 1-orthotope(선분)가 되는 경우이다.</li>
	<li>C는 두 2-orthotope의 공통된 영역이 0-orthotope(점)가 되는 경우이다.</li>
	<li>D는 두 2-orthotope의 공통된 영역이 없는 경우이다. 이 경우 -1을 출력하면 된다.</li>
</ul>

### 입력 

 <p>첫 번째 줄에 자연수 N이 주어진다.</p>

<p>두 번째 줄에는 첫 번째 영역의 s<sub>1</sub>, e<sub>1</sub>, s<sub>2</sub>, e<sub>2</sub>, ⋯, s<sub>N</sub>, e<sub>N</sub>이 공백으로 구분되어 주어진다.</p>

<p>세 번째 줄에는 두 번째 영역의 s<sub>1</sub>, e<sub>1</sub>, s<sub>2</sub>, e<sub>2</sub>, ⋯, s<sub>N</sub>, e<sub>N</sub>이 공백으로 구분되어 주어진다.</p>

<p>이 수들은 모두 절댓값이 11 이하이며, 각 s<sub>i</sub>, e<sub>i</sub>는 s<sub>i</sub> < e<sub>i</sub>를 만족한다.</p>

<p>1 ≤ N ≤ 11인 입력이 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 두 영역의 공통된 영역이 M-orthotope이면 M을 출력한다. 단 공통된 영역이 없는 경우 -1을 출력한다.</p>

