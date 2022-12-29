# [Silver V] Will Rogers fenomen - 26945 

[문제 링크](https://www.acmicpc.net/problem/26945) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>Will Rogers (1879-1935) var en amerikansk komiker känd för bland annat följande citat:</p>

<p><em>"When the Okies left Oklahoma and moved to California, they raised the average intelligence level in both states."</em></p>

<p>Denna skenbara paradox, att flyttning av ett element från en mängd till en annan gör att medelvärdet ökar i båda mängderna, har därför fått namnet Will Rogers fenomen. Du ska skriva ett program som läser in två grupper A och B vardera bestående av minst två och högst tio positiva heltal och avgör huruvida det är möjligt att genom att flytta ett tal från den ena gruppen till den andra få medelvärdet att öka i båda grupperna och i så fall vilket tal som ska flyttas till vilken grupp.</p>

### 입력 

 <p>Den första raden består av två tal: antal tal i första gruppen, och antal tal i andra gruppen (båda mellan 1 och 10). Därefter följer en rad med talen i första gruppen, och en rad med talen i andra gruppen.</p>

<p>Alla tal kommer att vara mellan <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> och <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container>.</p>

### 출력 

 <p>Om det är möjligt att flytta ett tal från ena gruppen till andra för att öka medelvärdet i båda, skriv ut en rad med talet som ska flyttas och vilken grupp det ska flyttas till. Om det finns flera möjligheter så räcker det att skriva ut en av dem.</p>

<p>Om det inte är möjligt, skriv ut <code>NEJ</code>.</p>

