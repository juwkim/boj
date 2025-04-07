# [Silver I] 유전자 조합 - 25758 

[문제 링크](https://www.acmicpc.net/problem/25758) 

### 성능 요약

메모리: 120636 KB, 시간: 256 ms

### 분류

브루트포스 알고리즘, 자료 구조, 해시를 사용한 집합과 맵, 비둘기집 원리

### 제출 일자

2025년 4월 7일 16:40:53

### 문제 설명

<p>서울과기대 학생들은 실험을 하다가 처음보는 생물의 유전자를 발견했다. 이 유전자는 형질 두 개로 나타낼 수 있고 형질은 대문자 알파벳으로 나타낼 수 있다. 유전자는 다른 유전자와 조합할 수 있는데, 두 유전자를 조합하면 첫 번째 유전자의 첫 번째 형질과 두 번째 유전자의 두 번째 형질이 붙은 다음 세대 유전자가 생긴다. 유전자의 두 형질에 있는 알파벳 중 사전순으로 같거나 큰 알파벳을 유전자의 표현형이라고 하자.</p>

<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 1세대 유전자가 주어졌을 때 이들은 서로 다른 모든 1세대 유전자들과 조합할 수 있다. 조합을 통해 생긴 2세대 유전자의 표현형으로 가능한 알파벳의 수와 그 알파벳을 구해보자.</p>

### 입력 

 <p>첫 번째 줄에 유전자의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \le N \le 100\,000$</span></mjx-container>)</p>

<p>두 번째 줄에는 1세대 유전자 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개가 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 2세대 유전자의 표현형으로 가능한 알파벳 수를 출력한다.</p>

<p>두 번째 줄에는 2세대 유전자의 표현형을 알파벳 순서대로 정렬 후 공백으로 구분하여 출력한다.</p>

