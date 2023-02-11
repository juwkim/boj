# [Silver V] Spotify Connect - 26883 

[문제 링크](https://www.acmicpc.net/problem/26883) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>Spotify har precis lanserat den nya funktionen Spotify Connect, som möjliggör för en användare att fjärrstyra sin uppspelning från mobiltelefonen. Det medför en mängd nya tekniska utmaningar, och en av dem är hur loggningen av uppspelningsdata görs. För att kunna rapportera till skivbolagen så måste man nämligen veta exakt hur länge en användare har lyssnat på musik.</p>

<p>Du kommer att få loggdata för <code>play</code> och <code>paus</code>-tryckningarna för en användare. Användaren använder både sin laptop för att styra musiken, men fjärrstyr också ibland med mobiltelefonen via Spotify Connect. Loggarna innehåller både datorns och mobilens <code>play</code> och <code>paus</code>-tryckningar. När användaren trycker på mobilen så är det exakt <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container> millisekunder delay tills laptopen (där musiken spelas upp ifrån) reagerar. Ditt uppdrag är att avgöra exakt hur många millisekunder totalt som laptopen spelade upp musik. Innan första kommandot utförs så är spelaren i pausat läge.</p>

### 입력 

 <p>Den första raden innehåller heltalet <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo><</mo><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N < 1000$</span></mjx-container>, antalet loggrader.</p>

<p>De efterföljande <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> raderna innehåller en lista med loggar. Loggarna kommer i den ordning knapptryckningar sker med en tidsstämpel i millisekunder, enhet (<code>laptop</code> eller <code>mobile</code>) och kommando (<code>play</code> eller <code>paus</code>). Den sista loggen kommer alltid vara ett <code>paus</code>-kommnado. Dessutom kommer två loggar aldrig ha samma tidsstämpel eller ligga exakt 100 millisekunder ifrån varandra.</p>

<p>För att göra indatat extra lättläst så är loggradernas fält alignerade. Tidsstämpeln fylls ut med nollor vänsterifrån så att talet alltid blir 7 tecken långt, och mobil stavas istället mobile, alltså med lika många tecken som i laptop. Se indataexemplet.</p>

### 출력 

 <p>Ditt program ska skriva ut ett heltal - antalet millisekunder användaren lyssnat på musik.</p>

