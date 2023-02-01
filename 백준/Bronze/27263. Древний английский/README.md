# [Bronze I] Древний английский - 27263 

[문제 링크](https://www.acmicpc.net/problem/27263) 

### 성능 요약

메모리: 115524 KB, 시간: 140 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Онуфрий изучает древний английский язык. Поскольку он делает это в рамках домашнего задания на завтра, он не успевает детально изучить его грамматику, поэтому он решил для простоты применить следующие правила для перевода современных английских слов в свой вариант древнего английского.</p>

<ul>
	<li>Все буквы <<<code>s</code>>>, после которых не идет <<<code>h</code>>> и которые не являются первыми в слове, заменяются на комбинацию <<<code>th</code>>>.</li>
	<li>Если первая буква в слове <<<code>e</code>>>, то она заменяется на <<<code>ae</code>>>.</li>
	<li>Комбинация <<<code>oo</code>>> заменяется на <<<code>ou</code>>>, причем если в слове идет подряд более двух букв <<<code>o</code>>>, то из них заменяются только первые две.</li>
</ul>

<p>Помогите Онуфрию перевести несколько слов на свою версию древнего английского языка.</p>

### 입력 

 <p>Первая строка ввода содержит <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>  --- количество слов, которые требуется перевести (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 100$</span></mjx-container>). Далее следует <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строк, каждая из которых состоит только из букв латинского алфавита. Все буквы каждого слова строчные, кроме, возможно первой, которая может быть заглавной. Длина каждого слова не превышает 30.</p>

### 출력 

 <p>Выведите <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> строк  --- результат перевода. Если первая буква исходного слова была заглавной, то такой же должна быть и первая буква переведенного слова. Иначе все буквы должны остаться строчными.</p>

