# [Bronze II] 돈복사 - 33963 

[문제 링크](https://www.acmicpc.net/problem/33963) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 문자열

### 제출 일자

2025년 5월 26일 01:26:26

### 문제 설명

<p>평소처럼 포스텍 위를 날아다니던 포닉스는, 우연히 땅에 떨어진 돈복사 버튼을 발견했다! 돈복사 버튼은 누르기만 하면 포닉스의 은행 계좌에 든 돈을 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2$</span></mjx-container>배 늘려주는 버튼으로, 이론상 몇 번의 클릭만으로 자신의 재산을 기하급수적으로 늘릴 수 있다.</p>

<p>억만장자가 될 생각에 신이 난 포닉스는 그 자리에서 버튼을 마구 누르고 싶었지만, 아쉽게도 은행은 그렇게 호락호락한 곳이 아니었다. 은행에는 실시간으로 돈을 탐지하는 시스템이 작동하고 있으며, 만약 버튼을 너무 많이 눌러 계좌에 찍힌 금액의 자리수가 변경되는 순간 포닉스가 가진 돈을 모두 압수해버릴 것이다.</p>

<p>포닉스 또한 이런 시스템을 잘 알고 있으므로 돈을 압수당하지 않는 선에서 최대한 많이 자신의 재산을 불리고 싶어한다. 포닉스를 도와 최대 몇 번 버튼을 누를 수 있는지 구해주자.</p>

### 입력 

 <p>첫 번째 줄에 포닉스가 현재 가진 재산을 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3C"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo><</mo><msup><mn>10</mn><mn>9</mn></msup><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \le N < 10^9)$</span> </mjx-container></p>

### 출력 

 <p>포닉스가 버튼을 누를 수 있는 최대 횟수를 출력한다.</p>

