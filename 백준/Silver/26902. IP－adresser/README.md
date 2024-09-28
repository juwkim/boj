# [Silver III] IP-adresser - 26902 

[문제 링크](https://www.acmicpc.net/problem/26902) 

### 성능 요약

메모리: 108080 KB, 시간: 84 ms

### 분류

브루트포스 알고리즘, 문자열

### 제출 일자

2024년 9월 28일 16:22:49

### 문제 설명

<p>En IPv4-address består av fyra heltal mellan <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container> och <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>255</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$255$</span></mjx-container> (som vardera inte får ha några inledande nollor), separerade av punkter. T.ex. är <code>1.0.3.255</code> en giltig address, medan <code>1.0.03.255</code>, <code>1.0.3.256</code> och <code>1.0.3</code> inte är giltiga addresser. Givet en sekvens av siffror, hitta alla giltiga IPv4-adresser som kan skapas genom insättning av tre punkter i sekvensen.</p>

### 입력 

 <p>På första raden står en sträng med minst <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container> och max <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$12$</span></mjx-container> siffror.</p>

### 출력 

 <p>Skriv ut ett heltal: antalet giltiga IP-adresser som kan bildas genom att sätta in 3 punkter.</p>

