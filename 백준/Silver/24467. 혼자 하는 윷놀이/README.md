# [Silver I] 혼자 하는 윷놀이 - 24467 

[문제 링크](https://www.acmicpc.net/problem/24467) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

많은 조건 분기, 구현, 시뮬레이션

### 제출 일자

2025년 4월 12일 22:12:11

### 문제 설명

<p>오전 4시, 민재는 윷놀이를 하고 싶어졌다. 하지만 다들 자는 시간이라 윷놀이를 같이 할 사람은 없었다.</p>

<p>민재는 윷놀이를 혼자 할 수 있는 방법을 생각해냈다.</p>

<p>혼자 하는 윷놀이에 적용되는 규칙은 다음과 같다.</p>

<ul>
	<li>처음에 말은 윷판의 오른쪽 아래에 위치한다.</li>
	<li>열 번의 차례 안에 말 하나가 완주하면 민재가 승리한다.</li>
	<li>차례 한 번에는 윷가락 네 개를 던진 후:
	<ul>
		<li>뒷면이 하나인 경우 말을 한 칸 전진시킨다.</li>
		<li>뒷면이 둘인 경우 말을 두 칸 전진시킨다.</li>
		<li>뒷면이 셋인 경우 말을 세 칸 전진시킨다.</li>
		<li>모두 뒷면인 경우 말을 네 칸 전진시킨 뒤, 윷을 추가로 던진다.</li>
		<li>모두 앞면인 경우 말을 다섯 칸 전진시킨 뒤, 윷을 추가로 던진다.</li>
	</ul>
	</li>
	<li>윷판을 정해진 경로로 한 바퀴를 돌아 윷판의 오른쪽 아래에 도착한 뒤 한 칸 더 움직여야  완주할 수 있다.</li>
	<li>혼자 하나의 말로 하는 게임이므로 상대 말을 잡거나 자신의 말을 업는 경우는 없다.</li>
	<li>일반적인 윷놀이의 낙과 뒷도 등의 룰은 고려하지 않는다.</li>
</ul>

<p>게임이 진행될 윷놀이판은 다음과 같다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/83d426ed-6abf-45eb-a483-26f06c810f9c/-/preview/" style="width: 576px; height: 577px;"></p>

<p>윷판에서 말이 갈 수 있는 길은 그림과 같이 네 가지이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/cf46bde6-7d01-4cba-b3bf-700f2b4b017e/-/preview/" style="width: 720px; height: 179px;"></p>

<p>빈 원으로 표시된 위치에 말이 놓이면 상대적으로 짧은 길로 가야한다. 그 위치에 놓이지 않는다면 상대적으로 먼 길로 가야 한다.</p>

<p>민재의 승리 여부를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄부터 민재가 윷가락을 어떻게 던졌는지 순서대로 주어진다.</p>

<p>각 줄에는 <code>0</code>과 <code>1</code>로 이루어진 길이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container>인 문자열이 주어진다. <code>0</code>은 윷가락 뒷면, <code>1</code>은 윷가락 앞면을 나타낸다.</p>

<p>민재는 완주하더라도 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10$</span></mjx-container>턴을 모두 진행할 때까지 윷을 계속 던진다. 단, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$50$</span></mjx-container>줄을 초과하는 입력은 주어지지 않는다.</p>

<p>마지막 입력은 도, 개, 걸 중 하나로 주어진다.</p>

### 출력 

 <p>민재가 혼자 하는 윷놀이에서 이겼다면 <code>WIN</code>, 졌다면 <code>LOSE</code>를 출력한다.</p>

