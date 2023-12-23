# [Silver IV] Statystyki - 8609 

[문제 링크](https://www.acmicpc.net/problem/8609) 

### 성능 요약

메모리: 149604 KB, 시간: 324 ms

### 분류

구현

### 제출 일자

2023년 12월 24일 08:16:15

### 문제 설명

<p>W Bajtocji od niedawna wydawana jest nowa gazeta <i>BajtNews</i>. O dziwo, mieszkańcy Bajtocji wcale nie interesują się treścią publikowanych w niej artykułów, a jedynie statystykami, które ich dotyczą. Niektórzy z nich stali się już tak leniwi, że nie chcą sami tworzyć statystyk, dlatego poprosili Ciebie o napisanie programu, który będzie przygotowywał je automatycznie.</p>

<p>Bajtocjanie chcą znać liczby wystąpień następujących obiektów w artykułach:</p>

<ol>
	<li><b>spacji</b>, czyli pojedynczych odstępów;</li>
	<li><b>liczb</b>, czyli ciągłych (tzn. jednokawałkowych) fragmentów tekstu złożonych z cyfr (<code>0</code> - <code>9</code>), sąsiadujących z każdej strony ze znakiem niebędącym cyfrą lub z początkiem lub końcem tekstu;</li>
	<li><b>słów</b>, czyli ciągłych fragmentów złożonych z małych (<code>a</code> - <code>z</code>) lub wielkich (<code>A</code> - <code>Z</code>) liter alfabetu angielskiego, sąsiadujących z każdej strony ze znakiem niebędącym literą lub z początkiem lub końcem tekstu;</li>
	<li><b>zdań</b>, czyli spójnych fragmentów tekstu zakończonych kropką (i niezawierających innych kropek w środku), zawierających co najmniej jedno słowo; każde zdanie sąsiaduje z lewej strony albo z kropką, albo z początkiem tekstu;</li>
	<li><b>palindromów</b>, czyli słów symetrycznych - takich słów (gdzie słowo jest rozumiane w sensie punktu trzeciego), które czytane wprost i wspak mogą się różnić co najwyżej wielkością liter, np. <code>Abba</code>.</li>
</ol>

<p>Napisz program, który:</p>

<ul>
	<li>wczyta ze standardowego wejścia artykuł oraz spis rodzajów obiektów, które mają zostać przeanalizowane,</li>
	<li>wyznaczy żądane statystyki,</li>
	<li>wypisze wynik na standardowe wyjście.</li>
</ul>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba całkowita <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ n ≤ 5$</span></mjx-container>) oznaczająca liczbę żądanych rodzajów statystyk. W drugim wierszu znajduje się <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> liczb całkowitych <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a_i$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msub space="4"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><msub><mi>a</mi><mi>i</mi></msub><mo>≤</mo><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ a_i ≤ 5$</span></mjx-container>), pooddzielanych pojedynczymi odstępami i oznaczających numery typów obiektów, które należy zliczyć. Numery odpowiadają kolejności, w jakiej różne rodzaje obiektów zostały opisane powyżej (np. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>i</mi></msub><mo>=</mo><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a_i = 3$</span></mjx-container> oznacza żądanie zliczenia słów w tekście). Możesz założyć, że liczby <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a_i$</span></mjx-container> są parami różne.</p>

<p>Trzeci wiersz wejścia zawiera całą treść artykułu. Może się ona składać z następujących znaków:</p>

<ul>
	<li>cyfr: <code>0</code> - <code>9</code>;</li>
	<li>liter: <code>a</code> - <code>z</code> oraz <code>A</code> - <code>Z</code>;</li>
	<li>odstępów (spacji) oraz tabulacji;</li>
	<li>znaków interpunkcyjnych: '<code>,</code>' (przecinek), '<code>.</code>' (kropka), '<code>!</code>' (wykrzyknik), '<code>?</code>' (pytajnik).</li>
</ul>

<p>Liczba znaków w treści artykułu nie przekroczy <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\,000\,000$</span></mjx-container>. Możesz również założyć, że:</p>

<ul>
	<li>w co najmniej 20% przypadków testowych należy zliczać tylko statystyki pierwszego rodzaju (spacje),</li>
	<li>w co najmniej 40% przypadków testowych należy zliczać tylko statystyki pierwszego oraz drugiego rodzaju (spacje i liczby),</li>
	<li>w co najmniej 60% przypadków testowych należy zliczać tylko statystyki rodzajów od 1 do 3 (spacje, liczby i słowa),</li>
	<li>w co najmniej 80% przypadków testowych należy zliczać tylko statystyki rodzajów od 1 do 4 (spacje, liczby, słowa oraz zdania).</li>
</ul>

### 출력 

 <p>W pierwszym i jedynym wierszu wyjścia Twój program powinien wypisać <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> liczb całkowitych pooddzielanych pojedynczymi odstępami, oznaczających kolejne żądane rodzaje statystyk.</p>

