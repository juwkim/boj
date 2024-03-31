# [Silver III] 특별한 기술력 - 31674 

[문제 링크](https://www.acmicpc.net/problem/31674) 

### 성능 요약

메모리: 145352 KB, 시간: 184 ms

### 분류

애드 혹, 분할 정복을 이용한 거듭제곱, 그리디 알고리즘, 수학, 정렬

### 제출 일자

2024년 4월 1일 07:16:00

### 문제 설명

<p>NLCS의 기술력은 세계 제일이다.</p>

<p>기술력이 뛰어난 NLCS Jeju는 키가 커지고 싶은 학생들을 위해 키가 커지는 도구 "요술 망치"를 개발하였다.</p>

<p>키가 커지고 싶어 요술 망치의 임상실험에 참여한 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>명의 학생들에게 요술 망치를 사용하는 실험을 진행하게 되었다. 어떤 학생에게 요술 망치를 사용하면 그 학생의 키만큼 다른 모든 학생의 키가 커진다. 하지만 요술 망치는 아직 프로토타입 단계라 한 학생에게 최대 한 번밖에 사용할 수 없다.</p>

<p>NLCS Jeju는 요술 망치의 대단함을 강조하기 위해 요술 망치를 사용한 후 키가 가장 큰 학생의 키를 최대로 만들고자 한다.</p>

<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>명의 학생에게 요술 망치를 사용해서 만들 수 있는 가장 큰 키를 구해보자!</p>

### 입력 

 <p>첫 번째 줄에 학생의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>두 번째 줄에 각 학생의 키 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.057em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H_i$</span></mjx-container>가 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>요술 망치를 적절히 사용하여 얻을 수 있는 가장 큰 학생의 키를 출력한다. 단, 학생의 키가 너무 커질 수 있기 때문에 이를 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>9</mn></msup><mo>+</mo><mn>7</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^9+7$</span></mjx-container>로 나눈 나머지를 출력한다.</p>

