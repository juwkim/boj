# [Silver IV] Думский регламент - 18100 

[문제 링크](https://www.acmicpc.net/problem/18100) 

### 성능 요약

메모리: 114328 KB, 시간: 120 ms

### 분류

자료 구조(data_structures), 스택(stack)

### 문제 설명

<p>В Тридевятом Царстве уже много лет как установилась конституционная монархия. В парламент Тридевятого царства входят 26 партий, обозначаемых строчными буквами английского алфавита от '<code>a</code>' до '<code>z</code>'. Заседание парламента в соответствии с регламентом проходит по следующей схеме:</p>

<ul>
	<li>В начале заседания никаких законопроектов на повестке дня не стоит.</li>
	<li>Любая партия (в том числе и та, которая внесла текущий законопроект) в любой момент времени может внести на обсуждение новый законопроект.</li>
	<li>При вносе партией нового законопроекта обсуждение предыдущего приостанавливается и начинается обсуждение нового. После того, как парламентарии голосуют за новый законопроект, обсуждение законопроекта, прерванного им, продолжается</li>
	<li>Дискуссия по любому законопроекту обязана завершиться голосованием по этому законопроекту.</li>
	<li>В конце заседания не должно остаться внесённых законопроектов, дискуссия по которым не завершена.</li>
</ul>

<p>Вам дана запись сессии парламента. Проверьте, существует ли корректный порядок проведения сессии, соответствующий этой записи.</p>

### 입력 

 <p>Первая строка входных данных содержит одно целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container> --- количество строк в записи сессии (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>K</mi><mo>≤</mo><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le K \le 1000$</span></mjx-container>). Каждая строка соответствует одному из двух событий:</p>

<ul>
	<li><code>Add</code> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container> --- партия <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container> внесла на голосование законопроект.</li>
	<li><code>Vote</code> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container> --- прошло голосование за документ, внесённый партией <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container>.</li>
</ul>

<p>Здесь <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container> --- строчная буква английского алфавита от '<code>a</code>' до '<code>z</code>', задающая партию.</p>

### 출력 

 <p>Выведите <<<code>Yes</code>>>, если существует корректный порядок проведения заседания, который мог привести к такой записи, и <<<code>No</code>>>, если ни при каком корректном порядке проведения заседания данная запись появиться не могла.</p>

