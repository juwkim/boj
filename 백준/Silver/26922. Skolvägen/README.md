# [Silver III] Skolvägen - 26922 

[문제 링크](https://www.acmicpc.net/problem/26922) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 2월 6일 01:26:40

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/093f4b27-e33f-454a-a303-f89ed432cd74/-/preview/"></p>

<p style="text-align: center;">Den streckade linjen visar Cissis väg i första exemplet.</p>

<p>Cissi går från sitt hem till skolan längs en lång gata som går i väst-östlig riktning. På sin väg passerar hon ett antal korsningar där tvärgator utgår norrut (<code>N</code>), söderut (<code>S</code>) eller både norrut och söderut (<code>B</code>). Vid varje korsning finns övergångsställen på både tvärgator och huvudgata (se figuren ovan), och dessa måste givetvis följas.</p>

<p>Både hemmet och skolan ligger på norra sidan av gatan. Skriv ett program som hjälper Cissi att beräkna det minsta antalet gator hon måste korsa på sin väg till skolan. </p>

### 입력 

 <p>Indata består av en enda rad med högst <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\,000$</span></mjx-container> bokstäver, som vardera är <code>N</code>, <code>S</code> eller <code>B</code>. Bokstäverna beskriver korsningarna i precis den ordning som Cissi passerar dem.</p>

### 출력 

 <p>En rad med ett heltal, det minsta antalet gator Cissi behöver korsa.</p>

