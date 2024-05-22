# [Silver III] 교실 배정 - 31803 

[문제 링크](https://www.acmicpc.net/problem/31803) 

### 성능 요약

메모리: 108080 KB, 시간: 104 ms

### 분류

조합론, 수학

### 제출 일자

2024년 5월 22일 12:02:00

### 문제 설명

<p>대구과학고는 현재 독서동을 수리하고 있어서 교실에서 대신 자습을 진행하기로 했다. 선생님들은 학생들이 떠들 것을 우려해 반별로 교실을 두 개씩 사용하기로 했다. 또한 교실마다 크기 차이가 있어 공평하게 사용하기 위해 매일 교실 배치를 바꾸어가며 자습을 진행하기로 하였다. 대구과학고에는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 교실과 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c230A"></mjx-c></mjx-mo><mjx-mfrac><mjx-frac><mjx-num><mjx-nstrut></mjx-nstrut><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-num><mjx-dbox><mjx-dtable><mjx-line></mjx-line><mjx-row><mjx-den><mjx-dstrut></mjx-dstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mo class="mjx-n"><mjx-c class="mjx-c230B"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo fence="false" stretchy="false">⌊</mo><mfrac><mi>N</mi><mn>2</mn></mfrac><mo fence="false" stretchy="false">⌋</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\lfloor \frac{N}{2} \rfloor$</span></mjx-container>개의 반이 있어, 각 반을 홀수 번호인 학생들과 짝수 번호인 학생들로 나누어 서로 다른 교실에서 자습하도록 할 생각이다.</p>

<p>대구과학고의 모범생인 지웅이는 이준구 선생님의 부탁으로 자습 교실 배치를 돕기로 하였다. <strong>지웅이는 반 배정을 고려하지 않은 채, 교실을 두 개씩 짝지어 이준구 선생님에게 전달해 주면 이준구 선생님이 그에 맞춰 반을 배정하는 방식이다.</strong> 이준구 선생님은 교실들을 짝짓는 방법 한 가지당 보상으로 초코파이를 하나씩 주기로 했다. 지웅이는 초코파이를 최대 몇 개 받을 수 있을까?</p>

### 입력 

 <p>첫 번째 줄에 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

### 출력 

 <p>지웅이가 받을 수 있는 초코파이의 최대 개수를 출력한다.</p>

