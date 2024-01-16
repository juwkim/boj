# [Silver III] 스파이 - 28075 

[문제 링크](https://www.acmicpc.net/problem/28075) 

### 성능 요약

메모리: 114200 KB, 시간: 268 ms

### 분류

브루트포스 알고리즘, 구현, 재귀

### 제출 일자

2024년 1월 16일 12:57:53

### 문제 설명

<p>스파이 민겸이는 이웃 나라와의 평화를 위해 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>일간 임무를 수행한다.</p>

<p>민겸이는 정보 수집과 감시 2가지 임무를 수행한다. 각 임무는 수족관, 시청, 학교에서 수행할 수 있다. 두 임무는 성격이 크게 다르기 때문에 하루에 한 가지 임무만 수행할 수 있으며, 수족관, 시청, 학교는 멀리 떨어져 있기 때문에 하루에 한 가지 장소에서만 임무를 수행할 수 있다. 또한, 민겸이는 반드시 하루에 최소 하나의 임무를 수행해야 한다.</p>

<p style="text-align: center;"><img alt="" src=""></p>

<p>다시 말해, 민겸이는 하루에 위 표의 6가지 행동 중 하나를 선택하여 할 수 있다.</p>

<p>민겸이는 각 장소에서 각 임무를 수행할 때, 임무 완수를 위한 진척도를 얻을 수 있다. 그러나 민겸이는 스파이이기 때문에, 같은 장소에서 오래 근무하면 사람들의 눈에 띄어 얻을 수 있는 진척도가 낮아진다. 민겸이가 전날에 임무를 수행한 곳과 같은 장소를 선택하면 그 날은 원래의 절반에 해당하는 진척도만 얻을 수 있다. 이때, 장소가 같다면 임무가 달라도 얻는 진척도는 원래의 절반이 됨에 유의하자.</p>

<p>민겸이의 기여도는 얻은 진척도의 합이다. 각 장소에서 각 임무를 수행했을 때 얻을 수 있는 진척도가 주어질 때 민겸이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> 이상의 기여도를 얻을 수 있는 임무 수행 방법이 몇 가지인지 구하라.</p>

### 입력 

 <p>첫째 줄에는 민겸이가 임무를 수행하는 총 일수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>과 민겸이가 얻고 싶은 최소 기여도 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 공백으로 구분되어 주어진다.</p>

<p>둘째 줄에 민겸이가 정보 수집 임무를 수족관, 시청, 학교에서 수행했을 때 얻을 수 있는 진척도가 순서대로 공백으로 구분되어 주어진다.</p>

<p>셋째 줄에 민겸이가 감시 임무를 수족관, 시청, 학교에서 수행했을 때 얻을 수 있는 진척도가 순서대로 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>민겸이가 기여도를 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> 이상 얻을 수 있는 임무 수행 방법이 몇 가지인지 출력한다.</p>

