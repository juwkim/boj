# [Bronze I] Inteligentna Ines - 31196 

[문제 링크](https://www.acmicpc.net/problem/31196) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

구현, 수학, 문자열

### 제출 일자

2025년 3월 2일 20:09:44

### 문제 설명

<p>Mali Ivica svake večeri šalje maloj Marici tajne podatke e-poštom. Oni znaju da Ivičino e-pismo na putu do Maričinog e-pretinca potpuno nezaštićeno prolazi preko više različitih računala u mreži, pa su se dogovorili da će svaku poruku Ivica šifrirati prema sljedećem algoritmu:</p>

<ul>
	<li>Neka se poruka koju Ivica želi poslati Marici sastoji od <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> znakova.</li>
	<li>Ivica prvo mora pronaći tablicu koja se sastoji od <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$r$</span></mjx-container> redaka i <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> stupaca takvu da je <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>≤</mo><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$r ≤ s$</span></mjx-container> i da je <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mi>r</mi><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n = rs$</span></mjx-container>. Ako postoji više takvih tablica, Ivica treba odabrati onu koja ima što je moguće više redaka.</li>
	<li>Ivica zapisuje poruku u tablicu po recima odozgo prema dolje, a unutar retka slijeva nadesno. Tako u prvi red upisuje prvi dio poruke, u drugi red drugi dio poruke itd.</li>
	<li>Poruka koju Ivica šalje Marici dobiva se čitanjem tablice po stupcima slijeva nadesno, a unutar stupca odozgo prema dolje.</li>
</ul>

<p>Ljubomorna Ines presrela je šifriranu e-poruku koju je Ivica poslao Marici. Napišite program koji će dešifrirati tajnu poruku.</p>

### 입력 

 <p>U prvom je retku niz od barem jednog, a najviše <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container> malih slova engleske abecede koji predstavlja šifriranu poruku koju je Ines presrela.</p>

### 출력 

 <p>U jedini redak potrebno je ispisati dešifriranu poruku.</p>

