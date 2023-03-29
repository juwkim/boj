# [Silver V] UDPC 파티 - 27919 

[문제 링크](https://www.acmicpc.net/problem/27919) 

### 성능 요약

메모리: 116244 KB, 시간: 148 ms

### 분류

그리디 알고리즘

### 문제 설명

<p>윤이, 포닉스, 달구는 UDPC가 열리는 것을 기념해 한 장소에 모여 파티를 열기로 했다! 수많은 참가자와 함께 즐거운 시간을 보내던 중, 참가자들이 세 마스코트 중 누가 제일 귀여운지 토론하기 시작했다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6520773a-76d2-43dc-a389-0c1fdebaa546/-/preview/" style="width: 250px; height: 250px;"></p>

<p style="color: rgb(170, 170, 170); font-style: italic; text-align: center;">UNIST 마스코트 '윤이' - 출처: 윤찐빵</p>

<p style="text-align: center;">야, 아무리 봐도 우리 윤이가 제일 귀엽지. 앙증맞은 뿔과 매력적인 갈기 좀 봐!</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/89332e51-917c-483a-9c29-aa932fc51738/-/preview/" style="width: 250px; height: 251px;"></p>

<p style="color: rgb(170, 170, 170); font-style: italic; text-align: center;">POSTECH 마스코트 '포닉스' - 출처: POSTECH 홈페이지</p>

<p style="text-align: center;">그렇게 치면 우리 포닉스의 갈기는! 귀여운 날개랑 꼬리도 가지고 있지~</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/d216c4bb-eecf-434b-a01a-dff9065d44b1/-/preview/" style="height: 249px; width: 250px;"></p>

<p style="color: rgb(170, 170, 170); font-style: italic; text-align: center;">DGIST 마스코트 '달구' - 출처: 주식회사 테라핀 홈페이지</p>

<p style="text-align: center;">어차피 우리 달구가 제일 귀엽죠? 이목구비는 물론이고 통통한 몸과 붕어빵마저 귀엽잖아!</p>

<p>토론은 끝날 기미가 없었고, 말하다 지친 참가자들은 누가 제일 귀여운지 투표하기로 했다. 참가자는 종이에 <code>U</code>, <code>D</code>, <code>P</code>, <code>C</code> 중 하나만 적어 투표함에 넣었고, 각각 윤이, 달구, 포닉스, 기권을 의미한다. 한 마스코트가 받은 표의 수가 다른 두 마스코트가 각각 받은 표의 수보다 모두 크다면 그 마스코트가 제일 귀여운 마스코트로 선정된다!</p>

<p>투표가 모두 끝나 세 마스코트가 개표를 시작했다. 그런데 글씨체와 방향이 제각각이라 종이에 적힌 알파벳이 서로 비슷하게 생긴 <code>U</code>와 <code>C</code>, 그리고 <code>D</code>와 <code>P</code> 중 무엇인지 알 수 없어 개표 결과가 엉망이 되었다!</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/2f3c13ef-ee53-4f82-9a8b-d5257224a7a1/-/crop/659x227/73,17/-/preview/" style="height: 150px; width: 435px;"></p>

<p style="text-align: center;">U일까 C일까? 정답은 UUUU!</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/d0b327e9-8c50-4965-8091-dc5fc59c2577/-/crop/574x207/82,249/-/preview/" style="width: 416px; height: 150px;"></p>

<p style="text-align: center;">D일까 P일까? 정답은 DPDP!</p>

<p>참가자가 투표한 결과가 주어질 때, 세 마스코트가 개표할 때 <code>U</code>와 <code>C</code>, <code>D</code>와 <code>P</code>가 서로 바뀔 수 있는 것을 고려하여, 누가 제일 귀여운 마스코트로 선정될 수 있을지 알아내자.</p>

### 입력 

 <p>첫 번째 줄에 참가자가 투표한 결과 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D449 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$V$</span></mjx-container>가 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D449 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$V$</span></mjx-container>는 <span style="color:#e74c3c;"><code>U</code></span>, <span style="color:#e74c3c;"><code>D</code></span>, <span style="color:#e74c3c;"><code>P</code></span>, <span style="color:#e74c3c;"><code>C</code></span>만 포함하는 문자열이고, 길이는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>보다 크고 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mtext class="mjx-n"><mjx-c class="mjx-cA0"></mjx-c></mjx-mtext><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mtext> </mtext><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100\ 000$</span></mjx-container>을 넘지 않는다.</p>

### 출력 

 <p>윤이가 선정될 수 있다면 <span style="color:#e74c3c;"><code>U</code></span>, 달구가 선정될 수 있다면 <span style="color:#e74c3c;"><code>D</code></span>, 포닉스가 선정될 수 있다면 <span style="color:#e74c3c;"><code>P</code></span>를 출력한다.</p>

<p>선정될 수 있는 모든 마스코트의 알파벳을 위 순서대로 출력한다.</p>

<p>만약 <span style="color:#e74c3c;"><code>U</code></span>, <span style="color:#e74c3c;"><code>D</code></span>, <span style="color:#e74c3c;"><code>P</code></span> 중 어느 것도 출력하지 않는다면 <span style="color:#e74c3c;"><code>C</code></span>를 출력한다.</p>

