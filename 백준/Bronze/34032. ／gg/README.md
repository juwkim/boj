# [Bronze IV] /gg - 34032 

[문제 링크](https://www.acmicpc.net/problem/34032) 

### 성능 요약

메모리: 109592 KB, 시간: 92 ms

### 분류

분류 없음

### 제출 일자

2025년 6월 26일 03:22:01

### 문제 설명

<h5 style="text-align: center;"><img alt="" src=""></h5>

<p><code>haru_101</code>이 플레이하는 게임에 <strong><code>/gg</code></strong> 명령어가 있다. 이 명령어는 항복 투표를 진행하기 위한 명령어로, 해당 팀의 각 팀원은 <strong><code>/gg</code></strong>를 입력함으로써 항복 의사를 밝힐 수 있다. 팀원 중 절반 이상이 <strong><code>/gg</code></strong> 명령어를 입력하면 팀은 항복하게 된다.</p>

<p>각 팀원의 명령어 입력 여부가 주어졌을 때, 해당 팀이 항복하게 되는지를 알아보자.</p>

### 입력 

 <p>첫째 줄에 팀원의 수를 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>둘째 줄에 길이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>인 알파벳 대문자 <code><span style="color:#e74c3c;">O</span></code>와 <code><span style="color:#e74c3c;">X</span></code>로만 이루어진 문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>가 주어진다.</p>

<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 문자는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 팀원이 <strong><code>/gg</code></strong> 명령어를 입력했다면 <code><span style="color:#e74c3c;">O</span></code>, <strong><code>/gg</code></strong> 명령어를 입력하지 않았다면 <code><span style="color:#e74c3c;">X</span></code>다.</p>

### 출력 

 <p>해당 팀이 항복하게 되면 <code><span style="color:#e74c3c;">Yes</span></code>, 그렇지 않다면 <code><span style="color:#e74c3c;">No</span></code>를 출력한다.</p>

